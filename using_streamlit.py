# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# import streamlit as st

# # Threshold for triggering an alert
# threshold = 5

# # Path to your recorded video file
# video_path = 'vid2.mp4'

# # Open the video file for reading
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     st.error("Error: Could not open video file.")
#     st.stop()

# count = 0
# alert_displayed = False  # Flag to track whether the alert is displayed

# st.title("Real-Time Video Analysis")

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     count += 1
#     if count % 8 != 0:
#         continue

#     frame = cv2.resize(frame, (1020, 600))
#     bbox, label, conf = cv.detect_common_objects(frame)

#     # Create a list to store the indices of "person" labels
#     person_indices = [i for i, lbl in enumerate(label) if lbl == 'person']

#     # Filter bounding boxes and labels for "person" objects
#     filtered_bbox = [bbox[i] for i in person_indices]
#     filtered_label = [label[i] for i in person_indices]
#     filtered_conf = [conf[i] for i in person_indices]

#     # Draw bounding boxes only for "person" objects
#     frame = draw_bbox(frame, filtered_bbox, filtered_label, filtered_conf)

#     headcount = len(person_indices)  # Calculate the number of persons
#     st.markdown(f"Headcount: {headcount}")

#     # Check if headcount exceeds the threshold and display alert
#     if headcount > threshold:
#         alert_text = f"ALERT: Headcount ({headcount}) exceeds the threshold ({threshold})!"
#         if not alert_displayed:
#             alert_displayed = True
#         else:
#             alert_displayed = False

#     if alert_displayed:
#         # Blink the alert text by toggling its visibility
#         if count % 12 < 6:  # Blink at 2 Hz (6 frames on, 6 frames off)
#             st.error(alert_text)

#     st.image(frame, channels="BGR")
#     if st.button("Stop Analysis"):
#         break

# cap.release()

# st.success("Video analysis completed.")


##### PROGRESS BAR

# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# import streamlit as st

# # Threshold for triggering an alert
# threshold = 10

# # Path to your recorded video file
# video_path = 'vid2.mp4'

# # Open the video file for reading
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     st.error("Error: Could not open video file.")
#     st.stop()

# count = 0
# alert_displayed = False  # Flag to track whether the alert is displayed

# st.title("Real-Time Video Analysis")

# output_frame = st.empty()

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     count += 1
#     if count % 8 != 0:
#         continue

#     frame = cv2.resize(frame, (1020, 600))
#     bbox, label, conf = cv.detect_common_objects(frame)

#     # Create a list to store the indices of "person" labels
#     person_indices = [i for i, lbl in enumerate(label) if lbl == 'person']

#     # Filter bounding boxes and labels for "person" objects
#     filtered_bbox = [bbox[i] for i in person_indices]
#     filtered_label = [label[i] for i in person_indices]
#     filtered_conf = [conf[i] for i in person_indices]

#     # Draw bounding boxes only for "person" objects
#     frame = draw_bbox(frame, filtered_bbox, filtered_label, filtered_conf)

#     headcount = len(person_indices)  # Calculate the number of persons
#     st.markdown(f"Headcount: {headcount}")
    
#     try:
#         progress_value = headcount
#         if 0 <= progress_value <= 20:
#             st.progress(progress_value / 20)
#     except ValueError:
#         pass
    
#     # if headcount > threshold:
#     #     alert_text = f"ALERT: Headcount ({headcount}) exceeds the threshold ({threshold})!"
#     #     if not alert_displayed:
#     #         alert_displayed = True
#     #     else:
#     #         alert_displayed = False

#     # if alert_displayed:
#     #     if count % 12 < 6:
#     #         st.error(alert_text)

#     output_frame.image(frame, channels="BGR")

# cap.release()

# st.success("Video analysis completed.")


# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# import streamlit as st

# # Threshold for triggering an alert
# threshold = 5

# # Path to your recorded video file
# video_path = 'vid2.mp4'

# # Open the video file for reading
# cap = cv2.VideoCapture(video_path)

# if not cap.isOpened():
#     st.error("Error: Could not open video file.")
#     st.stop()

# count = 0
# alert_displayed = False  # Flag to track whether the alert is displayed

# st.title("Real-Time Video Analysis")

# output_frame = st.empty()

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     count += 1
#     if count % 8 != 0:
#         continue

#     frame = cv2.resize(frame, (1020, 600))
#     bbox, label, conf = cv.detect_common_objects(frame)

#     # Create a list to store the indices of "person" labels
#     person_indices = [i for i, lbl in enumerate(label) if lbl == 'person']

#     # Filter bounding boxes and labels for "person" objects
#     filtered_bbox = [bbox[i] for i in person_indices]
#     filtered_label = [label[i] for i in person_indices]
#     filtered_conf = [conf[i] for i in person_indices]

#     # Draw bounding boxes only for "person" objects
#     frame = draw_bbox(frame, filtered_bbox, filtered_label, filtered_conf)

#     headcount = len(person_indices)  # Calculate the number of persons
#     st.markdown(f"Headcount: {headcount}")

#     # Check if headcount exceeds the threshold and display alert
#     if headcount > threshold:
#         alert_text = f"ALERT: Headcount ({headcount}) exceeds the threshold ({threshold})!"
#         alert_displayed = True
#     else:
#         alert_text = ""
#         alert_displayed = False

#     if alert_displayed:
#         st.button("Alert!", key="alert_button", on_click=None, args=(alert_text,)).button_style("color: red;")

#     output_frame.image(frame, channels="BGR")

# cap.release()

# st.success("Video analysis completed.")

import pandas as pd
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import streamlit as st
import altair as alt

# Threshold for triggering an alert
threshold = 10

# Path to your recorded video file
video_path = 'vid2.mp4'

# Open the video file for reading
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    st.error("Error: Could not open video file.")
    st.stop()

count = 0
alert_displayed = False  # Flag to track whether the alert is displayed

st.title("Real-Time Video Analysis")

output_frame = st.empty()

data = pd.DataFrame(columns=['x', 'y'])
chart_container = st.empty()

num_data_points = 6

while True:
    ret, frame = cap.read()

    if not ret:
        break

    count += 1
    if count % 10 != 0:
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
    # st.markdown(f"Headcount: {headcount}")
    
    new_data = pd.DataFrame({'x': [count], 'y': [headcount]})
    data = data.append(new_data, ignore_index = True)
    # data = pd.concat(data, new_data, ignore_index = True)
    colors_list = [['rgba(55, 0, 0)','rgba(121, 0, 0)','rgba(187, 0, 0)','rgba(255, 0, 0)', 'red'], 
                ['rgba(0, 38, 52)','rgba(0, 84, 114)','rgba(0, 129, 176)','rgba(0, 176, 240)', 'rgba(0, 176, 240)']]
    
    color = colors_list[0] if headcount > threshold else colors_list[1]
    
    gradient = alt.Gradient(
        gradient='linear',
        stops=[
            alt.GradientStop(color = 'black', offset = 0),  
            alt.GradientStop(color = color[0], offset = 0.25),
            alt.GradientStop(color = color[1], offset = 0.5),
            alt.GradientStop(color = color[2], offset = 0.75),
            alt.GradientStop(color = color[3], offset = 1)],
        x1=1,
        x2=1,
        y1=1,
        y2=0
    )
    
    chart = alt.Chart(data).mark_area(
        line = {'color': color[4]},
        color = gradient
    ).encode(x = 'x', y = alt.Y('y', scale = alt.Scale(domain = [0, headcount])))
    
    data = data.tail(num_data_points)
    
    # Display the Altair chart
    chart_container.altair_chart(chart, use_container_width = True)
    
    # try:
    #     progress_value = headcount
    #     if 0 <= progress_value <= 20:
    #         st.progress(progress_value / 20)
    # except ValueError:
    #     pass
    
    # if headcount > threshold:
    #     alert_text = f"ALERT: Headcount ({headcount}) exceeds the threshold ({threshold})!"
    #     if not alert_displayed:
    #         alert_displayed = True
    #     else:
    #         alert_displayed = False

    # if alert_displayed:
    #     if count % 12 < 6:
    #         st.error(alert_text)

    output_frame.image(frame, channels="BGR")

cap.release()

st.success("Video analysis completed.")