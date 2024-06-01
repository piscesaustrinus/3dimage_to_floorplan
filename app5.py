import cv2
import numpy as np
import streamlit as st
from PIL import Image

def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    return blurred

def detect_edges(image):
    # Use Canny edge detection to find edges
    edges = cv2.Canny(image, 50, 150)
    return edges

def detect_lines(edges):
    # Use Hough Transform to detect lines in the edge image
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=80, maxLineGap=10)
    return lines

def filter_lines(lines):
    if lines is None:
        return []
    
    filtered_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            # Filter lines to keep only those that are close to vertical or horizontal
            if abs(x1 - x2) < 10 or abs(y1 - y2) < 10:
                filtered_lines.append((x1, y1, x2, y2))
    
    return filtered_lines

def draw_lines(image_shape, lines):
    # Create a blank image for drawing the floor plan
    floor_plan = np.zeros(image_shape, dtype=np.uint8)
    
    # Draw the detected lines on the blank image
    for x1, y1, x2, y2 in lines:
        cv2.line(floor_plan, (x1, y1), (x2, y2), 255, 2)
    
    return floor_plan

def main():
    st.title('3D to 2D Floor Plan Conversion')

    # Upload an image
    uploaded_file = st.file_uploader("Choose a 3D image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        image = Image.open(uploaded_file)
        image = np.array(image)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Preprocess the image
        preprocessed_image = preprocess_image(image_rgb)
        
        # Detect edges
        edges = detect_edges(preprocessed_image)
        
        # Detect lines
        lines = detect_lines(edges)
        st.write(f"Number of lines detected: {len(lines) if lines is not None else 0}")
        
        # Filter lines to get only the walls (horizontal/vertical lines)
        filtered_lines = filter_lines(lines)
        st.write(f"Number of filtered lines: {len(filtered_lines)}")
        
        # Draw lines on a blank image
        floor_plan = draw_lines(preprocessed_image.shape, filtered_lines)
        
        # Display the results using Streamlit
        st.image(image, caption='Original Image', use_column_width=True)
        st.image(preprocessed_image, caption='Preprocessed Image', use_column_width=True, clamp=True, channels="GRAY")
        st.image(edges, caption='Edges', use_column_width=True, clamp=True, channels="GRAY")
        st.image(floor_plan, caption='2D Floor Plan', use_column_width=True, clamp=True, channels="GRAY")

if __name__ == "__main__":
    main()
