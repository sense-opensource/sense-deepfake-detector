#!/bin/bash
#!/bin/bash

IMAGE_NAME="sense_deepfake_opensource_image"

echo "🛑 Stopping and removing containers, volumes, and orphans..."
docker compose down --volumes --remove-orphans

echo "🧽 Removing dangling images..."
dangling_images=$(docker images -f "dangling=true" -q)
if [ -n "$dangling_images" ]; then
    docker rmi $dangling_images
else
    echo "No dangling images to remove."
fi

echo "🧼 Removing custom image: $IMAGE_NAME..."
if docker images "$IMAGE_NAME" | grep -q "$IMAGE_NAME"; then
    docker rmi "$IMAGE_NAME"
    echo "✅ Removed image: $IMAGE_NAME"
else
    echo "ℹ️ Image $IMAGE_NAME not found or already removed."
fi

echo "✅ Full cleanup complete."
