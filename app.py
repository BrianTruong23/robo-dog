# import streamlit as st
# import cv2
# import numpy as np

# st.title("OpenCV Video Stream in Streamlit")

# # Create a VideoCapture object to capture video from your camera (usually camera index 0)
# cap = cv2.VideoCapture(0)

# # Check if the camera is opened successfully
# if not cap.isOpened():
#     st.error("Error: Could not open the camera.")
# else:
#     st.success("Camera is ready!")

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Display the video frame in Streamlit
#     st.image(frame, channels="BGR", use_column_width=True)

# # Release the VideoCapture and close the OpenCV window
# cap.release()

# st.warning("Video feed stopped.")

import streamlit as st
import cv2
import numpy as np

st.title("OpenCV Video Stream in Streamlit")

# Create a VideoCapture object to capture video from your camera (usually camera index 0)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    st.error("Error: Could not open the camera.")
else:
    st.success("Camera is ready!")

# Create an empty placeholder to display the video feed
video_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Update the video feed in the placeholder without displaying individual frames
    video_placeholder.image(frame, channels="BGR")

    

# Release the VideoCapture and close the OpenCV window
cap.release()

st.warning("Video feed stopped.")
