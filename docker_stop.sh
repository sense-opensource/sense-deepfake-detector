#!/bin/bash
echo "🛑 Stopping the container..."
docker compose down --remove-orphans
echo "✅ Container stopped."
