🖱️ Virtual Mouse using MediaPipe & Python

A real-time AI-based virtual mouse that allows you to control the system cursor using hand gestures captured through a webcam.
The project uses MediaPipe Hand Tracking, OpenCV, and PyAutoGUI to move the mouse and perform click actions without any physical device.

🚀 Features

📷 Real-time webcam hand tracking

✋ Index finger controls mouse movement

👆 Thumb + index finger gesture performs mouse click

🪞 Mirror-corrected movement (natural control)

⚡ Smooth and responsive cursor control

🛠️ Tech Stack

Python 3.10

MediaPipe – Hand landmark detection

OpenCV – Webcam input & visualization

PyAutoGUI – Mouse control

NumPy – Numerical operations

📂 Project Structure
virtual-mouse-mediapipe/
│
├── mouse.py          # Main application file
├── README.md         # Project documentation
├── requirements.txt  # Project dependencies
└── .gitignore        # Ignored files (venv, cache)

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/virtual-mouse-mediapipe.git
cd virtual-mouse-mediapipe

2️⃣ Create & activate virtual environment
python -m venv mp_env
mp_env\Scripts\activate    # Windows

3️⃣ Install dependencies
pip install mediapipe==0.10.20
pip install opencv-contrib-python==4.11.0.86
pip install pyautogui


Or using requirements.txt:

pip install -r requirements.txt

▶️ Run the Project
python mouse.py


Show your hand to the camera

Move index finger → move cursor

Bring thumb close to index finger → click

Press Q to exit

🧠 How It Works

Webcam captures live video frames

MediaPipe detects 21 hand landmarks

Index finger tip (landmark 8) controls cursor position

Distance between thumb (landmark 4) and index finger triggers click

PyAutoGUI maps finger position to screen coordinates

📌 Gesture Logic
Gesture	Action
Index finger movement	Cursor movement
Thumb close to index finger	Mouse click
Press Q	Exit program
⚠️ Notes

Ensure good lighting for better hand detection

Avoid sudden hand movements for smooth control

Project tested on Windows

📈 Future Enhancements

Right-click & scroll gestures

Cursor smoothing (reduce jitter)

Multi-hand support

Gesture-based drag & drop

UI overlay with FPS & gesture status

🎓 Use Cases

Touchless computer interaction

Assistive technology

AI/ML academic projects

Computer vision learning

Demo project for resume & portfolio

🧑‍💻 Author

Ashmit Yadav
Computer Science & AI/ML Enthusiast

⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork it

📢 Share it
