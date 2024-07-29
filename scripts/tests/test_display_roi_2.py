import cv2
import matplotlib.pyplot as plt
import easyocr

# screenshot_path = 'data/Frame_1.png'

# img = cv2.imread(screenshot_path)
# roi1 = img[1100:1400, 40:800]

# rois = [roi1]

#reader = easyocr.Reader(['en'], gpu=True)
#results = reader.readtext(rois[0], detail=0) 
#print("Detected Text:", results)

#plt.imshow(rois[0])
#plt.title('Screenshot')
#plt.show() 

screenshot_path = 'data/Frame_1.png'
img = cv2.imread(screenshot_path)
roi = img[1100:1400, 40:800]

reader = easyocr.Reader(['en'], gpu=True)
result = reader.readtext(roi, detail=0)

# Draw text directly on ROI
for detection in result:
    print(detection)

# Display the modified ROI
# plt.imshow(img)
# plt.title('Detected Text on ROI')
# plt.axis('off')
# plt.show()