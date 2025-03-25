import os
from PIL import Image
import face_recognition
import numpy as np

def is_valid_image_file(file_path: str) -> bool:
    """
    Checks if a file is an image based on its content.

    Args:
        file_path: The path to the file.

    Returns:
        True if the file is an image, False otherwise.

    """
    if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', 'webp')):
        return False
    if not os.path.isfile(file_path):
        return False
    try:
        with Image.open(file_path) as img:
            img.verify()
            return True
    except FileNotFoundError:
        return False
    except Exception:
        return False


def generate_image_encodings(image_path: str) -> list:
    """
    Generates image encodings for a given image.

    Args:
        image_path (str): The path to the image.
    """
    if not is_valid_image_file(image_path):
        return []
    image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) > 0:
        return np.array(face_encodings).tolist()
    return []


def compare_face_encodings(base_encoding: list[float], target_encoding: list[float]) -> bool:
    """
    Compares two face encodings to determine if they are similar.

    Args:
        base_encoding (list): The base face encoding.
        target_encoding (list): The target face encoding.

    Returns:
        True if the face encodings are similar, False otherwise.
    """
    base_image_encoding = np.array(base_encoding)
    target_image_encoding = np.array(target_encoding)
    results = face_recognition.compare_faces(base_image_encoding, target_image_encoding[0])
    return results[0]
    

def traverse_image_directory_and_generate_encodings(directory_path: str, skip_folder: list[str] = None) -> dict:
    """
    Traverses a directory and generates image encodings for all images.

    Args:
        directory_path (str): The path to the directory.
        skip_folder (list[str]): A list of folder names to skip (default: None).
    Returns:
        Dictionary with int as key and image encodings as values.
    """
    image_encodings = {}
    print(f"Traversing directory: {directory_path}")
    print("Generating image encodings...")
    i = 1
    for root, dirs, files in os.walk(directory_path):
        dirs[:] = [d for d in dirs if d not in skip_folder]
        print(f"Traversing directory: {root}")
        for file in files:
            image_path = os.path.join(root, file)
            if not is_valid_image_file(image_path):
                continue
            encodings = generate_image_encodings(image_path)
            if len(encodings) > 0:
                image_encodings[i] = encodings
                print("." * i)
                i =+ 1
    print("Done")
    return image_encodings


def main(base_encoding: list[float], target_encoding: dict) -> None:
    for k, v in target_encoding.items():
        if compare_face_encodings(base_encoding, v):
            print(f"Face {k} is similar to the base image.")
        else:
            print(f"Face {k} is not similar to the base image.")
        

    

if __name__ == "__main__":
    base_image_encoding = generate_image_encodings(os.path.join(os.getcwd(), "base.jpg"))
    if len(base_image_encoding) == 0:
        print("No faces found in base.jpg")
        exit(1)
    target_image_encodings = traverse_image_directory_and_generate_encodings(os.path.join(os.getcwd(), "images"))
    main(base_image_encoding, target_image_encodings)
    

    