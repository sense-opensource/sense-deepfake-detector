<h1> 🕵️ Detect Deepfakes: Sense</h1>

<p width="100%">
    <a href="https://github.com/sense-opensource/sense-deepfake-detector/blob/main/LICENSE">
        <img width="8%" src="https://badge-generator.vercel.app/api?label=License&status=MIT&color=6941C6">
    </a>
    <!--<img width="12.6%" src="https://badge-generator.vercel.app/api?icon=Github&label=Last%20Commit&status=May&color=6941C6"/> -->
    <a href="https://discord.gg/hzNHTpwt">
        <img width="10%" src="https://badge-generator.vercel.app/api?icon=Discord&label=Discord&status=Live&color=6941C6"> 
    </a>
</p>

<h2 >Welcome to Sense’s open source repository</h2>

<p width="100%">  
<img width="4.5%" src="https://custom-icon-badges.demolab.com/badge/Fork-orange.svg?logo=fork"> <img width="4.5%" src="https://custom-icon-badges.demolab.com/badge/Star-yellow.svg?logo=star"> <img width="6.5%" src="https://custom-icon-badges.demolab.com/badge/Commit-green.svg?logo=git-commit&logoColor=fff"> 
</p>

<p> Secure your identity verification systems with Sense’s powerful deepfake detection. Prevent spoofing, fraud, and identity theft using advanced machine learning and computer vision</p>

<h2> 🧩 Overview</h2>

<p> As digital identity becomes the cornerstone of secure online interactions, the threat landscape has evolved far beyond password breaches and phishing. </p>

<p> Modern attackers now leverage advanced spoofing techniques like a GAN image which is a synthetic (i.e., fake) image produced by an AI model trained to generate realistic-looking images that resemble real ones, such as human faces—to trick facial recognition systems. </p>

<p> This calls for a new generation of AI-powered defenses that go beyond static image verification and ensure the authenticity of every face presented in digital workflows.</p>

<h3>🔧 Features</h3>

1. ONNX Runtime for inference 
2. Image upload and classification endpoint (/deepfake) 
3. Cross-Origin support (CORS) for frontend integration 
4. Dockerized for easy deployment 
5. Model visualization support 

<h4> ⏳ Clone the Repository </h4> 

```bash
# Clone the repository
git clone https://github.com/sense-opensource/sense-deepfake-detector.git

# Navigate into the project directory
cd sense-deepfake-detector
```

<h4> 🧠 Model </h4>

<p> The ONNX model file is <b>not included</b> in the repository.  
You must download the model file manually or programmatically and place it in the appropriate folder.</p>

<h4> ✅ Download Instructions </h4>

<p> Download the model file from the below link: </p>

```html

[Model] (https://github.com/sense-opensource/sense-deepfake-detector/releases/download/v1.0.0/efficientnet-b7.onnx this file needs to be placed inside the models folder)

Ensure the model is saved in:  models/efficientnet-b7.onnx

```

<h3>2. API Configuration </h3>
<h4>Method 1: Install Python Dependencies </h4>

```bash
pip install -r requirements.txt
```

<h4> Start the FastAPI Server </h4>

```bash
uvicorn app:app --reload
```

This will start the API server on: http://localhost:3015

<h4>Method 2: Running with Docker </h4>
<h4> Build Docker Image </h4>

```bash
docker build -t sense_deepfake_opensource_image .
```

<h4> Run Docker Container </h4>

```docker
docker run -d --name sense_deepfake_opensource_container -p 3015:3015 sense_deepfake_opensource_image
```
This will start the API server on: http://localhost:3015

<h3>3. Run the Frontend </h3>

```bash
cd front-end
npm install
npm run dev
```

<p> By default, the frontend runs on: http://localhost:5000</p>

<h3> Useful Docker Commands</h3>

<h4> Stop container </h4>

```docker
docker stop sense_deepfake_opensource_container
```

<h4> Remove container </h4>

```docker
docker rm -f sense_deepfake_opensource_container
```

<h4> Stop container </h4>

```docker
docker stop sense_deepfake_opensource_container
```

<h4> Remove image </h4>

```docker
docker rmi -f sense_deepfake_opensource_image
```

<h2> View logs </h2>

```docker
docker logs sense_deepfake_opensource_container
```

<p> MIT License — free to use, share, and modify </p>
