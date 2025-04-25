import cv2
import numpy as np

def visualize_results(image, label, confidence=None):
    """
    Visualize the prediction results by adding a colored border based on label.
    
    Args:
        image (np.ndarray): Input image
        label (str): Prediction label (REAL/FAKE)
        confidence (float, optional): Not used, kept for compatibility
        
    Returns:
        np.ndarray: Image with visualization (only border)
    """
    # Create a copy of the image
    vis_image = image.copy()

    # Define color based on label
    color = (0, 255, 0) if label == "REAL" else (0, 0, 255)  # Green for REAL, Red for FAKE

    # Add border to the image
    border_thickness = 5
    vis_image = cv2.copyMakeBorder(
        vis_image,
        border_thickness,
        border_thickness,
        border_thickness,
        border_thickness,
        cv2.BORDER_CONSTANT,
        value=color
    )

    return vis_image
