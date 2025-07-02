import streamlit as st
import cv2
import pickle
import numpy as np
from PIL import Image
import tempfile

st.set_page_config(page_title="Parking Space Detection", layout="wide")
st.title("🅿️ Parking Space Detection System")

# Load slot positions
try:
    with open("CarParkPos", "rb") as f:
        posList = pickle.load(f)
except:
    st.error("Error: CarParkPos file not found.")
    st.stop()

width, height = 107, 48

# Option to upload image or video
mode = st.radio("Choose Input Type", ["Image", "Video"])

if mode == "Image":
    uploaded_image = st.file_uploader("Upload Parking Lot Image", type=['png', 'jpg', 'jpeg'])
    if uploaded_image:
        img = Image.open(uploaded_image)
        img = np.array(img)
        imgOriginal = img.copy()
        
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
        imgThresh = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY_INV, 25, 16)
        imgMedian = cv2.medianBlur(imgThresh, 5)
        kernel = np.ones((3, 3), np.uint8)
        imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

        spaceCounter = 0
        for pos in posList:
            x, y = pos
            imgCrop = imgDilate[y:y + height, x:x + width]
            count = cv2.countNonZero(imgCrop)
            color = (0, 255, 0) if count < 900 else (0, 0, 255)
            if count < 900:
                spaceCounter += 1
            cv2.rectangle(imgOriginal, pos, (pos[0] + width, pos[1] + height), color, 2)
            cv2.putText(imgOriginal, str(count), (x, y + height - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        cv2.putText(imgOriginal, f'Available: {spaceCounter}/{len(posList)}',
                    (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,200,0), 2)

        st.image(imgOriginal, channels="BGR", caption="Processed Image", use_column_width=True)

elif mode == "Video":
    uploaded_video = st.file_uploader("Upload Parking Lot Video", type=['mp4'])
    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        cap = cv2.VideoCapture(tfile.name)

        stframe = st.empty()
        while cap.isOpened():
            success, img = cap.read()
            if not success:
                break

            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
            imgThresh = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY_INV, 25, 16)
            imgMedian = cv2.medianBlur(imgThresh, 5)
            kernel = np.ones((3, 3), np.uint8)
            imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

            spaceCounter = 0
            for pos in posList:
                x, y = pos
                imgCrop = imgDilate[y:y + height, x:x + width]
                count = cv2.countNonZero(imgCrop)
                color = (0, 255, 0) if count < 900 else (0, 0, 255)
                if count < 900:
                    spaceCounter += 1
                cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)
                cv2.putText(img, str(count), (x, y + height - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

            cv2.putText(img, f'Available: {spaceCounter}/{len(posList)}',
                        (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,200,0), 2)

            stframe.image(img, channels="BGR", use_column_width=True)

        cap.release()
