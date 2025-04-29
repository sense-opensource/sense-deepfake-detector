<h1 align="center">  🕵️ Detect Deepfakes: Sense</h1>

<p align="center" width="100%">
<img width="8%" src="https://badge-generator.vercel.app/api?label=License&status=MIT&color=6941C6"> <img width="12.6%" src="https://badge-generator.vercel.app/api?icon=Github&label=Last%20Commit&status=May&color=6941C6"/> <img width="10%" src="https://badge-generator.vercel.app/api?icon=Discord&label=Discord&status=Live&color=6941C6"> 
</p>

<h2 align="center">Welcome to Sense’s open source repository</h2>

<p align="center" width="100%">  
<img width="4.5%" src="https://custom-icon-badges.demolab.com/badge/Fork-orange.svg?logo=fork"> <img width="4.5%" src="https://custom-icon-badges.demolab.com/badge/Star-yellow.svg?logo=star"> <img width="6.5%" src="https://custom-icon-badges.demolab.com/badge/Commit-green.svg?logo=git-commit&logoColor=fff"> 
</p>

<p align="center"> Secure your identity verification systems with Sense’s powerful deepfake detection. Prevent spoofing, fraud, and identity theft using advanced machine learning and computer vision</p>

<h2 align="center"> 🧩 Overview</h2>

<p align="center"> As digital identity becomes the cornerstone of secure online interactions, the threat landscape has evolved far beyond password breaches and phishing. </p>

<p align="center"> Modern attackers now leverage advanced spoofing techniques—such as printed photos, replayed videos, 3D masks, and AI-generated deepfakes—to trick facial recognition systems. </p>

<p align="center"> This calls for a new generation of AI-powered defenses that go beyond static image verification and ensure the authenticity of every face presented in digital workflows.</p>

<h3 align="center">🔧 Features</h3>

<h4 align="center">1. ONNX Runtime for inference </h4>
<h4 align="center">2. Image upload and classification endpoint (`/deepfake`) </h4>
<h4 align="center">3. Cross-Origin support (CORS) for frontend integration </h4>
<h4 align="center">4. Dockerized for easy deployment </h4>
<h4 align="center">5. Model visualization support </h4>

<h4 align="center"> 🧠 Model </h4>

<p align="center"> TThe ONNX model file is **not included** in the repository.  
You must download the model file manually or programmatically and place it in the appropriate folder.</p>

<h4 align="center"> ✅ Download Instructions </h4>

<p align="center"> Download the model file from CDN or S3 bucket: </p>

<p align="center"> wget https://cdn-or-s3-link.com/2.7_80x80_MiniFASNetV2.pth -P resources/anti_spoof_models/  </p>

<p align="center"> Ensure the model is saved in:  </p>

<p align="center"> resources/anti_spoof_models/2.7_80x80_MiniFASNetV2.pth </p>

<h4 align="center"> Clone the Repository </h4> 

<p align="center"> git clone https://github.com/your-username/liveness.git </p>

<p align="center"> cd liveness </p>

<h3 align="center"> Install Python Dependencies </h3>

<p align="center"> pip install -r requirements.txt </p>

<h3 align="center"> Start the FastAPI Server </h3>

<p align="center"> uvicorn app:app --reload </p>

<p align="center"> This will start the API server on: http://localhost:3015 </p>

<h3 align="center"> Running with Docker </h3>
<h3 align="center"> Build Docker Image </h3>

<p align="center">COMPOSE_BAKE=true docker build -t sense_deepfake_opensource_image</p>

<h3 align="center"> Run Docker Container </h3>

<p align="center">docker run -d --name sense_deepfake_opensource_container -p 3015:3015 sense_deepfake_opensource_image</p>

<p align="center">docker rm -f sense_liveness_opensource_container</p>

<p align="center">This will start the API server on: http://localhost:3015 </p>

<h3 align="center"> Run the Frontend </h3>

<p align="center">cd front-end</p>
<p align="center">npm install</p>
<p align="center">npm run dev</p>

<p align="center"> By default, the frontend runs on: http://localhost:5000</p>

<h3 align="center"> Useful Docker Commands</h3>

<h4 align="center"> Stop container </h4>
<p align="center">docker stop sense_deepfake_opensource_container</p>

<h4 align="center"> Remove container </h4>
<p align="center">docker rm -f sense_deepfake_opensource_container</p>

<h4 align="center"> Stop container </h4>
<p align="center">docker stop sense_deepfake_opensource_container</p>

<h4 align="center"> Remove image </h4>
<p align="center">docker rmi -f sense_deepfake_opensource_image</p>

<h2 align="center"> View logs </h2>
<p align="center">docker logs sense_deepfake_opensource_container</p>

<p align="center"> MIT License — free to use, share, and modify </p>

