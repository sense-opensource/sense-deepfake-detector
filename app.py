import onnxruntime
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile, Query, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import io
import base64
import os
from utils.visualization import visualize_results

app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dictionary of available models
AVAILABLE_MODELS = {
    "default": "models/efficientnet-b7.onnx",
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

        # Get prediction
        label, confidence = predict(image, model_name)

        # Visualize results
        visualized_image = visualize_results(image, label, confidence)
        print(label)
        # Convert the image to base64
        _, buffer = cv2.imencode('.png', visualized_image)
        image_base64 = base64.b64encode(buffer).decode('utf-8')

        # Return the results
        return JSONResponse(content={
            "label": label,
            "image": f"data:image/png;base64,{image_base64}"
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