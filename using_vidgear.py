import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear
import numpy as np

# Threshold for triggering an alert
threshold = 5

# live footage --> https://www.youtube.com/live/-hGxbIZxZxk?si=Ch8Jplajy2MZ9c76

stream = CamGear(source='http://192.168.217.232:8080/', stream_mode=True, logging=True).start()  # YouTube Video URL as input
count = 0
alert_displayed = False  # Flag to track whether the alert is displayed

while True:
    frame = stream.read()
    count += 1
    if count % 6 != 0:
        continue

    frame = cv2.resize(frame, (1020, 600))
    bbox, label, conf = cv.detect_common_objects(frame)

    # Create a list to store the indices of "person" labels
    person_indices = [i for i, lbl in enumerate(label) if lbl == 'person']

    # Filter bounding boxes and labels for "person" objects
    filtered_bbox = [bbox[i] for i in person_indices]
    filtered_label = [label[i] for i in person_indices]
    filtered_conf = [conf[i] for i in person_indices]

    # Draw bounding boxes only for "person" objects
    frame = draw_bbox(frame, filtered_bbox, filtered_label, filtered_conf)

    headcount = len(person_indices)  # Calculate the number of persons
    cv2.putText(frame, f"Headcount: {str(headcount)}", (60, 500), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    # Check if headcount exceeds the threshold and display alert
    if headcount > threshold:
        alert_text = f"ALERT: Headcount ({headcount}) exceeds the threshold ({threshold})!"
        if not alert_displayed:
            alert_displayed = True
        else:
            alert_displayed = False

    if alert_displayed:
        # Blink the alert text by toggling its visibility
        if count % 12 < 6:  # Blink at 2 Hz (6 frames on, 6 frames off)
            cv2.putText(frame, alert_text, (60, 100), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow("FRAME", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

stream.release()
cv2.destroyAllWindows()
