import cv2
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

def detect_skin_tone(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Crop region manually or use face detection
    face_crop = image_rgb[80:200, 100:250]
    pixels = face_crop.reshape((-1, 3))

    kmeans = KMeans(n_clusters=1)
    kmeans.fit(pixels)
    dominant_color = kmeans.cluster_centers_.astype(int)[0]

    def classify(rgb):
        r, g, b = rgb
        if r > 200 and g > 180:
            return "fair"
        elif r > 120:
            return "medium"
        else:
            return "deep"

    return classify(dominant_color)

def process_batch(csv_input_path, csv_output_path):
    df = pd.read_csv(csv_input_path)
    df['detected_skin_tone'] = df['image_path'].apply(detect_skin_tone)
    df.to_csv(csv_output_path, index=False)

if __name__ == "__main__":
    proce
