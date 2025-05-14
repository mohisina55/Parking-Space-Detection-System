# 🚗 Parking Space Detection System

A computer vision project that detects free and occupied parking spaces using OpenCV. This project includes a GUI tool to mark parking slots manually on a static image and processes a parking lot video to detect space occupancy in real-time.

---

## 📸 Demo

![Image Alt](https://github.com/mohisina55/Parking-Space-Detection-System/blob/1fd039134ebddd9fdf575e10c6154c869e06edfd/output.png)

---

## 🧰 Technologies Used

- Python 3.x
- OpenCV
- NumPy
- cvzone
- Pickle (Python standard library)

Install dependencies:
```bash
   pip install opencv-python cvzone numpy
```
---

## 🧑‍💻 Setup Instructions
Clone the repo

```bash
 git clone https://github.com/your-username/ParkingSpaceDetection.git
 cd ParkingSpaceDetection

```

## 🗂 Project Structure
```bash
  📦ParkingSpaceDetection
 ┣ 📜main.py              # Main video analysis and parking space detection logic
 ┣ 📜ParkingSpacePicker.py # Tool to manually select parking slot positions
 ┣ 📜CarParkPos            # Binary file storing the selected slot positions
 ┣ 📜carParkImg.png        # Static image used for slot selection
 ┣ 📜carPark.mp4           # Input video used for real-time detection
```
---

# 🖱️ How It Works
## Step 1: Mark Parking Slots

Run ParkingSpacePicker.py:
```bash
   python ParkingSpacePicker.py
```
- Left Click: Add a new parking slot (top-left corner).

- Right Click: Remove a previously added slot.

Selected slot positions will be saved to CarParkPos using pickle.

## Step 2: Detect Parking Availability

Run main.py:
```bash
   python main.py
```
- Processes each video frame to determine the status of each marked slot.

- Shows the number of free slots in real time.

---
## 🧠 How Detection Works
- Convert video frame to grayscale.

- Apply Gaussian blur for noise reduction.

- Apply adaptive thresholding and morphological operations.

- Crop each marked region and count non-zero pixels to determine occupancy.

If the pixel count is below a threshold (e.g., 900), it's considered empty.

---

## 🔧 Features

- Interactive slot selection using mouse events.

- Real-time parking space monitoring via video.

- Adaptive thresholding and contour processing for robust detection.

- Visual indicators for occupied (🔴) and free (🟢) slots.

- Slot count overlay for quick overview. 

---

## 📄 License

MIT License. Feel free to use, modify, and share!

