#runs on test_cuda_ocr

import cv2
import easyocr
import torch
import numpy as np
import pygetwindow as gw
from mss import mss
import time

# Check for CUDA availability (same as before)
cuda_available = torch.cuda.is_available()
if cuda_available:
    print("CUDA is available and will be used by EasyOCR.")
else:
    print("CUDA is not available. EasyOCR will use the CPU.")

# Initialize OCR reader
reader = easyocr.Reader(['en'])

def capture_and_ocr(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[ 0]
        left, top, width, height = window.left, window.top, window.width, window.height
        with mss() as sct:
            while True:
                # Capture window region
                monitor = {"top": top, "left": left, "width": width, "height": height}
                img = np.array(sct.grab(monitor))

                # Convert to BGR and apply OCR
                frame = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
                results = reader.readtext(frame, detail=0)

                # Display detected text (console output)
                print("Detected Text:", results)

                # Draw bounding boxes and text on the frame (for visualization if needed)
                for detection in reader.readtext(frame):
                    text, bbox = detection[1], detection[0]
                    cv2.rectangle(frame, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
                    cv2.putText(frame, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                # Show the captured window (uncomment if you want to see it)
                # cv2.imshow('Captured Window with Detected Text', frame)

                # Check for stop signal (press 'q' to quit)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()  
                    break
    except IndexError:
        print(f"Window with title '{window_title}' not found.")

while True:
    window_title = input("Enter the application window title (or 'q' to quit): ")
    if window_title.lower() == 'q':
        break
    capture_and_ocr(window_title)
