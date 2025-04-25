# sense-deepfake-detector

This project provides a FastAPI-based backend for image classification using an ONNX model (e.g., EfficientNet). It detects whether an uploaded image is a **REAL** or **Deepfake**. The response includes a prediction label, and a visualized image with the result overlay.

---

## 🔧 Features

- ONNX Runtime for inference
- Image upload and classification endpoint (`/predict`)
- Cross-Origin support (CORS) for frontend integration
- Dockerized for easy deployment
- Model visualization support

---

## 🧠 Model

The ONNX model file is **not included** in the repository.  
You must download the model file manually or programmatically and place it in the appropriate folder.

### ✅ Download Instructions

Download the model file from CDN or S3 bucket:

wget https://cdn-or-s3-link.com/efficientnet-b7.onnx -P models/

Ensure the model is saved in:

models/efficientnet-b7.onnx

### Clone the Repository

git clone https://github.com/your-username/deepfake-api.git
cd deepfake

### Install Python Dependencies
pip install -r requirements.txt

### Start the FastAPI Server
uvicorn app:app --reload

This will start the API server on:
http://localhost:3015


### Running with Docker
### Build Docker Image
COMPOSE_BAKE=true docker build -t sense_deepfake_opensource_image .

### Run Docker Container
docker run -d --name sense_deepfake_opensource_container -p 3015:3015 sense_deepfake_opensource_image

This will start the API server on:
http://localhost:3015


### 4. Run the Frontend

cd front-end
npm install
npm run dev

By default, the frontend runs on:
http://localhost:5000


### Project Structure
.
├── Dockerfile
├── docker-compose.yml
├── app.py/              # FastAPI app entrypoint
├── src/                 # Anti-spoofing model logic
├── resources/           # Pretrained model files
└── front-end/           # Frontend application (optional)


### Useful Docker Commands

# Stop container
docker stop sense_deepfake_opensource_container

# Remove container
docker rm -f sense_deepfake_opensource_container

# Remove image
docker rmi -f sense_deepfake_opensource_image

# View logs
docker logs sense-deepfake-opensource


### License
MIT License — free to use, share, and modify.


