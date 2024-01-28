# Face Detection and Information Extraction

This Python script demonstrates how to detect faces in an image, draw red circles around the detected faces, add information about the detected faces to the image, and save this information in a JSON file. It utilizes the InsightFace library for face detection and the PIL library for image manipulation.

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Replace the `image_path` variable with the path to the image you want to process.
4. Run the script using the following command:

```
python face_detection.py
```

5. The script will process the image specified in the `image_path` variable, detect faces, draw red circles around the detected faces, add information about the faces, and save the modified image as well as the face information in a JSON file.

## Example

Consider an example image named `img03.jpg`. The script will process this image, detect faces, draw red circles around the detected faces, add information about the faces (such as the number of faces detected and the date and time of detection), and save the modified image as `processed_images/img_<timestamp>.jpg`. It will also save information about the faces in a JSON file named `faces_info.json`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
