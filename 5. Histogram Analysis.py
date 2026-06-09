import cv2
import matplotlib.pyplot as plt

image = cv2.imread("sample.jpg")

colors = ('b','g','r')

for i,color in enumerate(colors):
    hist = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(hist,color=color)

plt.show()