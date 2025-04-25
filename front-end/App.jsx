import React, {useState, useEffect, useCallback} from 'react';
import './App.css';
import axios from 'axios';
import senselogo from "../front-end/images/sense-js-logo.svg"

function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [dragActive, setDragActive] = useState(false);
  const [scanning, setScanning] = useState(false);

  const addMatrixText = useCallback(() => {
    if (!scanning) return;

    const container = document.querySelector('.image-preview');
    if (!container) return;

    const text = document.createElement('div');
    text.className = 'matrix-text';
    text.style.left = `${Math.random() * 100}%`;
    text.style.top = `${Math.random() * 100}%`;
    text.textContent = Math.random().toString(16).substr(2, 8);

    container.appendChild(text);
    setTimeout(() => text.remove(), 500);
  }, [scanning]);

  useEffect(() => {
    let interval;
    if (scanning) {
      interval = setInterval(addMatrixText, 100);
    }
    return () => clearInterval(interval);
  }, [scanning, addMatrixText]);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);
      setSelectedImage(URL.createObjectURL(file));
      setPrediction(null);
      setScanning(true);
      setTimeout(() => setScanning(false), 3000);
    }
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === "dragenter" || e.type === "dragover") {
      setDragActive(true);
    } else if (e.type === "dragleave") {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
      setSelectedFile(file);
      setSelectedImage(URL.createObjectURL(file));
      setPrediction(null);
      setScanning(true);
      setTimeout(() => setScanning(false), 3000);
    }
  };

  const handlePredict = async () => {
    if (!selectedFile) {
      alert('Please select an image to analyze.');
      return;
    }
  
    setLoading(true);
    setScanning(true);
  
    const formData = new FormData();
    formData.append('file', selectedFile);
  
    try {
      const response = await axios.post(
        `http://localhost:3015/deepfake`, 
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      );
  
      setPrediction({
        label: response.data.label,
        image: response.data.image // This will be the base64 image
      });
    } catch (error) {
      console.error('Error predicting image:', error);
      alert('Failed to analyze the image. Please try again.');
    } finally {
      setLoading(false);
      setScanning(false);
    }
  };

  return (

    <div className="container">
    <header className="header">
      <img src={senselogo} alt="App Logo" className="logo" />
    </header>

    <h1>DeepFake Detection</h1>

    <div className="upload-section">
      <div
        className={`file-input-container ${dragActive ? 'drag-active' : ''}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <input
          type="file"
          accept="image/*"
          onChange={handleImageChange}
          className="file-input"
        />
        <div className="upload-content">
          <div className="upload-icon">🖼️</div>
          <div className="upload-text">
            Drop your image here or click to browse
            <span>Supported formats: JPG, PNG, GIF</span>
          </div>
        </div>
      </div>

      {selectedImage && (
        <div className={`image-preview ${scanning ? 'scanning' : ''}`}>
          <img src={prediction?.image || selectedImage} alt="Preview" />
          {loading ? (
            <div className="loading-spinner" />
          ) : (
            <button
              onClick={handlePredict}
              disabled={loading}
              className="predict-button"
            >
              Analyze Image
            </button>
          )}
        </div>
      )}
    </div>

    {prediction && (
      <div className={`prediction ${prediction.label.toLowerCase()}`}>
        <div className="icon">
          {prediction.label === 'REAL' ? '✅' : '⚠️'}
        </div>
        <h2>{prediction.label}</h2>
      </div>
    )}

    <footer className="footer">
      <p>&copy; {new Date().getFullYear()} Sense. All rights reserved.</p>
    </footer>
  </div>
  );
}

export default App;