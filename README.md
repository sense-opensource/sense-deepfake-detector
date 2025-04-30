<h1>  🕵️ Detect Deepfakes: Sense</h1>

<p width="100%">
<img width="8%" src="https://badge-generator.vercel.app/api?label=License&status=MIT&color=6941C6"> <img width="12.6%" src="https://badge-generator.vercel.app/api?icon=Github&label=Last%20Commit&status=May&color=6941C6"/> <img width="10%" src="https://badge-generator.vercel.app/api?icon=Discord&label=Discord&status=Live&color=6941C6"> 
</p>

<h2 >Welcome to Sense’s open source repository</h2>

<p width="100%">  
<img width="4.5%" src="https://custom-icon-badges.demolab.com/badge/Fork-orange.svg?logo=fork"> <img width="4.5%" src="https://custom-icon-badges.demolab.com/badge/Star-yellow.svg?logo=star"> <img width="6.5%" src="https://custom-icon-badges.demolab.com/badge/Commit-green.svg?logo=git-commit&logoColor=fff"> 
</p>

<p> Secure your identity verification systems with Sense’s powerful deepfake detection. Prevent spoofing, fraud, and identity theft using advanced machine learning and computer vision</p>

<h2> 🧩 Overview</h2>

<p> As digital identity becomes the cornerstone of secure online interactions, the threat landscape has evolved far beyond password breaches and phishing. </p>

<p> Modern attackers now leverage advanced spoofing techniques—such as printed photos, replayed videos, 3D masks, and AI-generated deepfakes—to trick facial recognition systems. </p>

<p> This calls for a new generation of AI-powered defenses that go beyond static image verification and ensure the authenticity of every face presented in digital workflows.</p>

<h3>🔧 Features</h3>

1. ONNX Runtime for inference 
2. Image upload and classification endpoint (/deepfake) 
3. Cross-Origin support (CORS) for frontend integration 
4. Dockerized for easy deployment 
5. Model visualization support 

<h4> ⏳ Clone the Repository </h4> 

<p> git clone https://github.com/sense-opensource/sense-deepfake-detector.git</p>

<p> cd liveness </p>

<h4> 🧠 Model </h4>

<p> TThe ONNX model file is **not included** in the repository.  
You must download the model file manually or programmatically and place it in the appropriate folder.</p>

<h4> ✅ Download Instructions </h4>

<p> Download the model file from the below link: </p>

<p> [Model] (https://github.com/sense-opensource/sense-deepfake-detector/releases/download/v1.0.0/efficientnet-b7.onnx this file needs to be placed inside the models folder) </p>

<p> Ensure the model is saved in:  <i>models/efficientnet-b7.onnx</i> </p>

<h3> Install Python Dependencies </h3>

<p> pip install -r requirements.txt </p>

<h3> Start the FastAPI Server </h3>

<p> uvicorn app:app --reload </p>

<p> This will start the API server on: http://localhost:3015 </p>

<h3> Running with Docker </h3>
<h3> Build Docker Image </h3>

<p>COMPOSE_BAKE=true docker build -t sense_deepfake_opensource_image</p>

<h3> Run Docker Container </h3>

<p>docker run -d --name sense_deepfake_opensource_container -p 3015:3015 sense_deepfake_opensource_image</p>

<p>docker rm -f sense_liveness_opensource_container</p>

<p>This will start the API server on: http://localhost:3015 </p>

<h3> Run the Frontend </h3>

<p>cd front-end</p>
<p>npm install</p>
<p>npm run dev</p>

<p> By default, the frontend runs on: http://localhost:5000</p>

<h3> Useful Docker Commands</h3>

<h4> Stop container </h4>
<p>docker stop sense_deepfake_opensource_container</p>

<h4> Remove container </h4>
<p>docker rm -f sense_deepfake_opensource_container</p>

<h4> Stop container </h4>
<p>docker stop sense_deepfake_opensource_container</p>

<h4> Remove image </h4>
<p>docker rmi -f sense_deepfake_opensource_image</p>

<h2> View logs </h2>
<p>docker logs sense_deepfake_opensource_container</p>

<p> MIT License — free to use, share, and modify </p>