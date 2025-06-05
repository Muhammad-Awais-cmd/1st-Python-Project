# ✋ HandTrackingminModule

A Python project that detects and tracks hand landmarks using OpenCV and MediaPipe.  
This module laid the foundation for gesture-controlled projects like volume control,  
keyboard input simulation, and more — all using hand gestures and some creative logic.

---

## 🛠️ Installation & Usage

### 🔹 Requirements

Make sure you're using **Python 3.10** — this version works best with the libraries used.

### 📦 Install Dependencies

Install the required libraries using pip:

#### 🔸 For basic hand tracking:
```
pip install opencv-python mediapipe
```

#### 🔸 For gesture-based control (like volume):
```
pip install opencv-python mediapipe numpy
```

> Note: `math` and `time` are built-in Python libraries — you don't need to install them.

---

## ▶️ How to Run

To test basic hand detection:
```
python HandTrackingmin.py
```

To control volume using hand gestures:
```
python GestureVolumeControl.py
```

> Make sure `HandTrackingminModule.py` is in the same directory, as it is used as a module in 'GestureVolumeControl.py' .

---

## 📌 Notes

- All scripts were written and tested using **Python 3.10**.
- Ensure your installed library versions are compatible with this Python version.
- The idea is modular — you can reuse `HandTrackingminModule` to build more gesture-based applications (e.g., media control, cursor movement, keyboard automation).

---

## 📂 Files Overview

- `HandTrackingminModule.py` – core module that handles hand detection and landmark tracking.
- `HandTrackingmin.py` – simple test file that prints hand landmarks using the module.
- `GestureVolumeControl.py` – uses the module and adds volume control via distance between fingers.

---

## 🙋‍♂️ Why This Project?

I created this project to test my Python skills and explore OpenCV and MediaPipe for the first time.  
It started as an experiment and turned into a reusable module for gesture-based interactions.

---
