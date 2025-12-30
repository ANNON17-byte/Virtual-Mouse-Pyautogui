import mediapipe as mp
import cv2
import pyautogui
cap = cv2.VideoCapture(0)

hand_detector = mp.solutions.hands.Hands()
drawing = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
if not cap.isOpened():
    exit()
index_y = 0
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hand_detector.process(rgb)
    hands = result.multi_hand_landmarks
    frame_height , frame_width, _ = frame.shape
    if not ret:
        break
    if hands:
        for hand in hands:
           drawing.draw_landmarks(frame, hand)
           landmarks = hand.landmark
           for id, landmark in enumerate(landmarks):
               x = int( landmark.x * frame_width)
               y = int(landmark.y * frame_height)
               print(x, y)
               if id == 8:
                   cv2.circle(img=frame, center=(x,y), radius=15, color=(255,0,255), thickness=cv2.FILLED)
                   index_x = screen_width / frame_width * x
                   index_y = screen_height / frame_height * y
                   pyautogui.moveTo(index_x, index_y)
               if id == 4:
                     cv2.circle(img=frame, center=(x,y), radius=15, color=(0,255,255), thickness=cv2.FILLED)
                     thumb_x = screen_width / frame_width * x
                     thumb_y = screen_height / frame_height * y
                     if abs(index_y - thumb_y) < 80:
                          
                          pyautogui.click()
                          pyautogui.sleep(1)
    
    cv2.imshow('Virual Mouse', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
