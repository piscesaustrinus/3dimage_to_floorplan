# 3D to 2D Floor Plan Conversion

## Overview
This project is a Streamlit web application that converts a 3D image of a floor plan into a 2D representation. The application processes the uploaded image, detects edges, identifies significant lines representing walls, and then draws these lines to create a 2D floor plan.

## Features
- Upload a 3D image file (JPG, JPEG, PNG)
- Preprocess the image (convert to grayscale and apply Gaussian blur)
- Detect edges using Canny edge detection
- Detect and filter lines using Hough Transform
- Draw the filtered lines to create a 2D floor plan

## Requirements
- Python 3.x
- Streamlit
- OpenCV
- NumPy
- Pillow

## Installation
1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:
    ```sh
    streamlit run app4.py
    ```

## Usage
1. Run the Streamlit application:
    ```sh
    streamlit run app4.py
    ```

2. Open the provided URL in your web browser.

3. Upload a 3D image file (JPG, JPEG, PNG).

4. The application will display:
   - Original image
   - Preprocessed image (grayscale and blurred)
   - Edges detected in the image
   - 2D floor plan with detected walls

## Project Structure
- `app.py`: Main application file containing the Streamlit app logic.
- `requirements.txt`: List of required Python packages.

## Functions
- `preprocess_image(image)`: Converts the image to grayscale and applies Gaussian blur.
- `detect_edges(image)`: Detects edges using Canny edge detection.
- `detect_lines(edges)`: Detects lines using Hough Transform.
- `filter_lines(lines)`: Filters lines to keep only horizontal and vertical ones.
- `draw_lines(image_shape, lines)`: Draws detected lines on a blank image.

## Example
![Original Image](example/original_image.jpg)
![Preprocessed Image](example/preprocessed_image.jpg)
![Edges](example/edges.jpg)
![2D Floor Plan](example/floor_plan.jpg)

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgments
- [OpenCV](https://opencv.org/)
- [Streamlit](https://www.streamlit.io/)
- [GraphQL](https://graphql.org/)

---

This README provides a comprehensive guide to understanding, installing, and using the 3D to 2D Floor Plan Conversion application. Enjoy transforming your 3D floor plans into 2D with ease!
