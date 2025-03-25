# Face Sort: A Python-based Face Recognition and Image Sorting Tool

## Overview

Face Sort is a Python application designed to analyze images within a directory and determine if they contain faces similar to a designated "base" image. It leverages the `face_recognition` library for face detection and encoding, and the `Pillow` (PIL) library for image handling. This tool is useful for organizing large image collections based on facial similarity.

## Features

*   **Face Detection:** Identifies faces within images using the `face_recognition` library's powerful face detection capabilities.
*   **Face Encoding:** Generates numerical encodings (vectors) representing the unique features of each detected face.
*   **Face Comparison:** Compares the face encodings of images in a target directory against a designated "base" image's encoding to determine similarity.
*   **Directory Traversal:** Recursively traverses a directory and its subdirectories, processing all valid image files it encounters.
*   **Image Validation:** Checks if a file is a valid image (e.g., PNG, JPG, JPEG, WEBP) before attempting to process it, preventing errors.
*   **Skip Folders:** Allows you to specify folders to be skipped during directory traversal, providing flexibility in processing.
*   **Clear Output:** Provides clear and informative output on the progress of the program, including which images are being processed and the results of the face comparisons.

## Prerequisites

Before running Face Sort, ensure you have the following installed:

*   **Python 3.6+:** The application is written in Python and requires a compatible version (3.6 or later).
*   **Dependencies:** The required Python libraries are listed in the `requirements.txt` file. These include:
    *   **face_recognition:** The core library for face detection and encoding.
    *   **Pillow (PIL):** For image handling and manipulation.
    *   **NumPy:** For numerical operations, particularly with face encodings (vectors).
    *   **dlib** A modern C++ toolkit containing machine learning algorithms and tools.
    *   **Cmake** CMake is used to build and manage C++ project like **dlib** above

## Installation

1.  **Clone the repository (if applicable):** If you have this code in a Git repository, clone it to your local machine:

    ```bash
    git clone https://github.com/amaechijude/face_sort
    cd face_sort
    ```

2.  **Otherwise, download the files:** If you don't have a repository, download the `main.py` and `requirements.txt` files and place them in the same directory.

3.  **Install Dependencies:** Navigate to the directory containing `requirements.txt` in your terminal and install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```
    This command will read the `requirements.txt` file and install all the listed packages and their dependencies.

## Usage

1.  **Prepare your images:**
    *   Place the image you want to use as the "base" image in the same directory as `main.py` and name it `base.jpg`.
    *   Create a folder named `images` in the same directory as `main.py`. Place all the images you want to compare against the base image inside this `images` folder. You can organize them into subfolders if needed.

2.  **Run the application:**

    ```bash
    python main.py
    ```

3.  **Interpreting the output:**
    *   The application will first traverse the `images` directory and generate encodings for all valid images. It will print out the progress of the encoding generation.
    *   Then, it will compare each image's encoding against the `base.jpg` encoding.
    *   The output will indicate whether each image in the `images` folder contains a face similar to the one in `base.jpg`.

## Example Directory Structure
face_sort/ 
    ├── main.py 
    ├── requirements.txt 
    ├── base.jpg # Your base image 
    
    └── images/ # Folder containing images to compare 
        ├── image1.jpg
        ├── image2.png 
        
        ├── subfolder/ 
            ├── image3.jpg
            ├── image4.webp