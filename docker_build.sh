#!/bin/bash
echo "🔨 Building the Docker image..."
COMPOSE_BAKE=true docker compose build
echo "✅ Build complete."