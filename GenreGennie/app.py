import streamlit as st
import os
from predict import predict_genre
import tempfile

st.set_page_config(page_title="🎧 GenreGennie - Let AI Decide the Beat")

st.title("🎵 GenreGennie")
st.subheader("Let AI listen to your song and guess the genre 🎶")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.audio(uploaded_file, format="audio/wav")

    with st.spinner("🎧 Analyzing the beat..."):
        genre = predict_genre(temp_path)
        st.success(f"🎼 The predicted genre is: **{genre.upper()}**")
