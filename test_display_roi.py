import cv2
import matplotlib.pyplot as plt

screenshot_path = 'data/Frame_1.png'

img = cv2.imread(screenshot_path)
roi = img[1100:1400, 40:800]

plt.imshow(roi, cmap='gray')
plt.title('Grayscale and Thresholded ROI')
plt.show()