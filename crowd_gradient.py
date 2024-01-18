import pandas as pd
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import streamlit as st
import altair as alt

threshold = 10

video_path = 'vid2.mp4'


cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    st.error("Error: Could not open video file.")
    st.stop()

count = 0
alert_displayed = False

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
    
    person_indices = [i for i, lbl in enumerate(label) if lbl == 'person']
    
    filtered_bbox = [bbox[i] for i in person_indices]
    filtered_label = [label[i] for i in person_indices]
    filtered_conf = [conf[i] for i in person_indices]
    
    frame = draw_bbox(frame, filtered_bbox, filtered_label, filtered_conf)
    
    headcount = len(person_indices)
    # st.markdown(f"Headcount: {headcount}")
    
    new_data = pd.DataFrame({'x': [count], 'y': [headcount]})
    data = pd.concat([data, new_data], ignore_index=True)
    
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
    
    chart_container.altair_chart(chart, use_container_width = True)
    
    output_frame.image(frame, channels="BGR")

cap.release()

st.success("Video analysis completed.")