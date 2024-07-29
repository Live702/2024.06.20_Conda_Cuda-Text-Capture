import cv2
import matplotlib.pyplot as plt
import easyocr
import torch

cuda_available = torch.cuda.is_available()
if cuda_available:
    print("CUDA is available and will be used by EasyOCR.")
else:
    print("CUDA is not available. EasyOCR will use the CPU.")

screenshot_path = 'data/Frame_1.png'
img = cv2.imread(screenshot_path)
roi = img[1100:1400, 40:800]

reader = easyocr.Reader(['en'])
results = reader.readtext(roi, detail=0)

print("Detected Text:", results)

for detection in reader.readtext(roi):
    text, bbox = detection[1], detection[0]
    cv2.rectangle(roi, (int(bbox[0][0]), int(bbox[0][1])), (int(bbox[2][0]), int(bbox[2][1])), (0, 255, 0), 2)
    cv2.putText(roi, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

plt.imshow(roi, cmap='gray')
plt.title('ROI with Detected Text')
plt.show()