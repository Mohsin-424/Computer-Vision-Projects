import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
from pyzbar.pyzbar import decode

# Define the image file path
image_path = r'G:\Computer Vision\PortFolio\qr-reader-attendance-system-master\img-1.jpeg'

# Check if the file exists
if not os.path.exists(image_path):
    print(f"The file {image_path} does not exist.")
else:
    # Read the image
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Failed to load image: {image_path}")
    else:
        # Decode QR codes in the image
        qr_info = decode(img)
        
        for qr in qr_info:
            data = qr.data.decode('utf-8')
            rect = qr.rect
            polygon = qr.polygon

            print(f"Data: {data}")
            print(f"Rect: {rect}")
            print(f"Polygon: {polygon}")

            # Draw a rectangle around the QR code
            img = cv2.rectangle(img, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                                (0, 255, 0), 5)

            # Draw the polygon around the QR code
            img = cv2.polylines(img, [np.array(polygon)], True, (255, 0, 0), 5)

            # Display the image with QR code highlighted
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.show()
