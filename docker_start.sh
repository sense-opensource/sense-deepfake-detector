#!/bin/bash

echo "🚀 Starting the container..."
docker compose up -d --no-build
echo "✅ Container is running at http://localhost:3015"
