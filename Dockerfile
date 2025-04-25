# ✅ Stage 1: Build environment
FROM python:3.9-slim AS builder

# Avoid prompts during install
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    cmake \
    libopenblas-dev \
    liblapack-dev \
    libx11-dev \
    libgtk-3-dev \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Upgrade pip and install dependencies in isolated build environment
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --prefix=/install -r requirements.txt


# ✅ Stage 2: Runtime environment
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY . .

# Expose the port
EXPOSE 3015

# Run FastAPI with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3015"]