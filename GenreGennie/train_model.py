import os
import librosa
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from tqdm import tqdm

# Change to your actual data path
DATASET_PATH = "C:\\Users\\Admin\\Desktop\\GenreGennie\\GenreGennie\\data\\Data\\genres_original"
GENRES = os.listdir(DATASET_PATH)

def extract_features(file_path):
    y, sr = librosa.load(file_path, duration=30)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs.T, axis=0)

def prepare_dataset():
    features, labels = [], []

    for genre in GENRES:
        genre_folder = os.path.join(DATASET_PATH, genre)
        if not os.path.isdir(genre_folder): continue
        for file in tqdm(os.listdir(genre_folder), desc=f"Processing {genre}"):
            if file.endswith(".wav"):
                try:
                    path = os.path.join(genre_folder, file)
                    mfcc = extract_features(path)
                    features.append(mfcc)
                    labels.append(genre)
                except:
                    print(f"Failed on file: {file}")
    
    return np.array(features), np.array(labels)

def main():
    print("🔍 Extracting features...")
    X, y = prepare_dataset()

    print("🧠 Training model...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    acc = accuracy_score(y_test, clf.predict(X_test))
    print(f"✅ Accuracy: {acc:.2f}")

    # Save model and dataset
    joblib.dump(clf, "models/genre_classifier.pkl")
    pd.DataFrame(X).assign(label=y).to_csv("genre_features.csv", index=False)
    print("✅ Model and features saved!")

if __name__ == "__main__":
    main()
