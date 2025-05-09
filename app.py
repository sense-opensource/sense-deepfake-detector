import onnxruntime
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import base64
import os
from utils.visualization import visualize_results
from PIL import Image
from io import BytesIO

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5000",  # Alternative Vite port
        "http://127.0.0.1:5000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dictionary of available models
# AVAILABLE_MODELS = {
#     "default": "models/efficientnet-b7.onnx",
# }
AVAILABLE_MODELS = {
    "default": "models/model.onnx",
    "fp16": "models/model_fp16.onnx",
    "efficientnet": "models/efficientnet-b7.onnx",
}

# Initialize session as None
session = None

def load_model(model_name="default"):
    """Load the ONNX model and verify it exists"""
    global session
    
    if model_name not in AVAILABLE_MODELS:
        raise HTTPException(status_code=400, detail=f"Model {model_name} not available")
    
    model_path = AVAILABLE_MODELS[model_name]
    
    if not os.path.exists(model_path):
        raise HTTPException(
            status_code=500,
            detail=f"Model file not found. Please ensure {model_path} exists."
        )
    
    try:
        session = onnxruntime.InferenceSession(model_path)
        return True
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to load model: {str(e)}"
        )

# Try to load the default model at startup
try:
    load_model("default")
except HTTPException as e:
    print(f"Warning: {e.detail}")

def analyze_metadata(exif_data):
    """Analyze metadata for originality, AI generation, and tampering."""
    issues = []
    risk_score = 0
    analyze_metadata_status = 1
    if not exif_data:
        issues.append("No EXIF data found - Could be AI-generated or manipulated.")
        risk_score += 2
        analyze_metadata_status = 0
        return issues, risk_score, analyze_metadata_status

    camera_make = exif_data.get('Make', None)
    camera_model = exif_data.get('Model', None)
    creation_date = exif_data.get('DateTime', None)
    modification_date = exif_data.get('DateTimeDigitized', None)

    if camera_make is None or camera_model is None:
        issues.append("Camera make/model missing - Could indicate tampering or AI generation.")
        #analyze_metadata_status = 0
        risk_score += 2

    if creation_date and modification_date:
        try:
            creation_dt = datetime.strptime(creation_date, "%Y:%m:%d %H:%M:%S")
            modification_dt = datetime.strptime(modification_date, "%Y:%m:%d %H:%M:%S")
            if (modification_dt - creation_dt).total_seconds() > 60:
                issues.append("Significant modification after creation")
                risk_score += 1
        except Exception as e:
            issues.append(f"Date parsing issue: {e}")
            risk_score += 1
    else:
        issues.append("Missing creation or modification date")
        risk_score += 1

    gps_info = exif_data.get('GPSInfo', None)
    if not gps_info:
        issues.append("No GPS location data")
        risk_score += 1

    software = exif_data.get('Software', None)
    if software:
        # if "Adobe" in software or "GIMP" in software or "Photoshop" in software:
        #     issues.append(f"Edited with {software}")
        #     risk_score += 2
        if any(keyword in software for keyword in ("Adobe", "GIMP", "Photoshop")):
            issues.append(f"Edited with {software}")
            risk_score += 2
            #analyze_metadata_status = 0
    else:
        issues.append("No editing software info")

    return issues, risk_score, analyze_metadata_status

def predict(image, model_name="default"):
    global session
    
    # Ensure model is loaded
    if session is None:
        load_model(model_name)
    
    # Preprocess the image
    try:
        image = cv2.resize(image, (224, 224))
        image = image / 255.0
        image = np.transpose(image, (2, 0, 1))
        image = np.expand_dims(image, axis=0).astype(np.float32)

        # Get model input and output names
        input_name = session.get_inputs()[0].name
        output_name = session.get_outputs()[0].name

        # Run inference
        prediction = session.run([output_name], {input_name: image})[0][0][0]
        label = "Deepfake detected" if prediction > 0.5 else "REAL"
        confidence = prediction if prediction > 0.5 else 1 - prediction

        return label, confidence
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

@app.post("/deepfake")
async def predict_image(file: UploadFile = File(...), model_name: str = Query("default")):
    try:
        # Read and decode the image
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        if image is None:
            raise HTTPException(
                status_code=400,
                detail="Invalid image file or format not supported"
            )
        pil_image = Image.open(BytesIO(contents))
        exif_data = pil_image._getexif()
        metadata_issues, metadata_score, analyze_metadata_status = analyze_metadata(exif_data)
        if analyze_metadata_status:
            # List of models to validate one after another
            model_sequence = [ "efficientnet"]
            results = []
            # Default final label
            final_label = "REAL"

            # Validate with each model
            for model_name in model_sequence:
                # Load and predict with each model
                load_model(model_name)
                label, confidence = predict(image, model_name)
                if label == "Deepfake detected":
                    final_label = "Deepfake detected"
                    break  # No need to check further models

            # Visualize results
            visualized_image = visualize_results(image, label, confidence)
            
            # Convert the image to base64
            _, buffer = cv2.imencode('.png', visualized_image)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
        else:
            final_label = 'Deepfake Detected'
        # Return the results along with intermediate model outputs
        return JSONResponse(content={
            "label": final_label
        })

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process the image: {str(e)}"
        )

@app.get("/health")
async def health_check():
    """Check if the model is loaded and working"""
    if session is None:
        try:
            load_model("default")
            return {"status": "healthy", "message": "Model loaded successfully"}
        except HTTPException as e:
            return {"status": "unhealthy", "message": e.detail}
    return {"status": "healthy", "message": "Service is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3015)