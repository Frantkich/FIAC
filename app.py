import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

img_file_buffer = st.camera_input("Unlock")

if img_file_buffer:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)
    st.write("TensorFlow")
    st.write(type(img_tensor))
    st.write(img_tensor.shape)
    
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    st.write("OpenCV")
    st.write(type(cv2_img))
    st.write(cv2_img)
