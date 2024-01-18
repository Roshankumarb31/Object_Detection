import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Replace 'IP_ADDRESS' and 'PORT' with the values provided by DroidCam
video_path = 'vid1.mp4'


# Video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not connect to DroidCam.")
    exit()

# Initialize Tkinter
root = tk.Tk()
root.title("DroidCam Viewer with Person Detection")

# Create a label for displaying video frames
video_label = tk.Label(root)
video_label.pack()

# Create buttons
play_button = ttk.Button(root, text="Play", command=lambda: play_pause())
rewind_button = ttk.Button(root, text="Rewind", command=lambda: rewind())
play_button.pack()
rewind_button.pack()

# Video playback control variables
playing = True
frame_counter = 0

def play_pause():
    global playing
    playing = not playing

def rewind():
    global frame_counter
    frame_counter = 0

def update():
    global frame_counter
    if playing:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            bbox, label, conf = cv.detect_common_objects(frame)

            # Filter bounding boxes and labels for "person" objects
            person_indices = [i for i, lbl in enumerate(label) if lbl == 'person']
            filtered_bbox = [bbox[i] for i in person_indices]

            # Draw bounding boxes only for "person" objects
            frame = draw_bbox(frame, filtered_bbox, label, conf)

            photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            video_label.config(image=photo)
            video_label.photo = photo
            frame_counter += 1
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
    root.after(10, update)  # Update every 10 milliseconds

update()  # Start the video update loop

root.mainloop()

# Release the video capture object and close the window when done
cap.release()
cv2.destroyAllWindows()
