"""
################### TEXT DETECTION ################################
In this Project we have used Opencv and easyocr to very easily build a simple ready to go ocr solution for text detection.

"""
import cv2 as cv
import easyocr
import matplotlib.pyplot as plt

img_path = "./data/test3.png"


def make_inference(image_path):
    img = cv.imread(img_path)
    reader = easyocr.Reader(['en'])
    text_ = reader.readtext(img)
    threshold = 0.26
    for t in text_:
        print(t)
        bbox, text, score = t
        if score >= threshold:
            cv.rectangle(img, bbox[0], bbox[2], (0, 255, 0), 5)
            cv.putText(img, text, bbox[0],
                       cv.FONT_HERSHEY_SIMPLEX, 0.65, (255, 0, 0), 2)
    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()


# TODO: Build Streamlit App for this
