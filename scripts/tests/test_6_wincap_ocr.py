import cv2
import easyocr
import torch
import pyautogui
import numpy as np
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
        # Find the window by title (you might need to adjust the title)
        window = pyautogui.getWindowsWithTitle(window_title)[0]

        while True:
            # Take a screenshot of the specified window
            screenshot = pyautogui.screenshot(region=(window.left, window.top, window.width, window.height))

            # Convert screenshot to OpenCV format (numpy array)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # Apply OCR to the captured frame
            results = reader.readtext(frame, detail=0)

            # Display detected text (console output)
            print("Detected Text:", results)

            # Draw bounding boxes and text on the frame (for visualization if needed)
            # (This part is similar to the previous code and can be uncommented if you want to display the image)

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
