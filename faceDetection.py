from insightface.app import FaceAnalysis
import numpy as np
from PIL import Image, ImageDraw
import json
from datetime import datetime
import os

# Load an image
image_path = 'images/img03.jpg'
image = Image.open(image_path)

# Get the file name
file_name = os.path.basename(image_path)

# Initialize the face analysis model
fa = FaceAnalysis()

# Prepare the model
fa.prepare(ctx_id=0, det_size=(640, 640))

# Detect faces in the image
faces = fa.get(np.array(image))

# Draw red circles around the detected faces
if faces is not None:
    draw = ImageDraw.Draw(image)
    for face in faces:
        bbox = face.bbox.astype(int)
        draw.ellipse([bbox[0], bbox[1], bbox[2], bbox[3]], outline='red', width=4)
    del draw
    
    # Add date and time to the image
    draw = ImageDraw.Draw(image)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_timestamp = datetime.now().strftime("%Y-%m-%d%H-%M-%S")
    draw.text((10, 10), f"Detected faces: {len(faces)}", fill="white")
    draw.text((10, 30), f"Date time: {current_time}", fill="white")
    del draw

    # Save the image with red circles around the faces
    processed_image_path = f'processed_images/img_{current_timestamp}.jpg'
    image.save(processed_image_path)
    print("Image saved with red circles around the detected faces.")

    # Save information in a JSON file
    json_data = {
        "image": processed_image_path,
        "num_faces": len(faces),
        "date_time": current_time
    }
    with open('faces_info.json', 'w') as json_file:
        json.dump(json_data, json_file)
    print("Information about the faces saved in faces_info.json.")
else:
    print("No face detected.")
