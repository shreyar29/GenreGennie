import librosa
import numpy as np
import joblib

# Load the saved model
model = joblib.load("models/genre_classifier.pkl")

def extract_mfcc(file_path):
    y, sr = librosa.load(file_path, duration=30)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_scaled = np.mean(mfcc.T, axis=0)
    return mfcc_scaled.reshape(1, -1)  # Shape (1, 13)

def predict_genre(file_path):
    features = extract_mfcc(file_path)
    prediction = model.predict(features)
    return prediction[0]
