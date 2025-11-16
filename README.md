GenreGennie is a machine learning–based music genre classification system that uses audio signal processing to predict the genre of songs. It extracts MFCC (Mel-frequency cepstral coefficients) features from audio files, trains a Random Forest classifier, and provides predictions through an interactive Streamlit web app.

🚀 Features

🎶 Extracts MFCC features using Librosa

🧠 Trains a Random Forest classifier on labeled datasets

💾 Saves and loads the trained model with Joblib

🎧 Interactive Streamlit app for genre prediction

📊 End-to-end pipeline: preprocessing → training → prediction → deployment

🛠️ Tech Stack

Python

Librosa – audio feature extraction

NumPy, Pandas, Matplotlib – data handling and visualization

Scikit-learn – machine learning

Joblib – model persistence

Streamlit – web app interface

📂 Project Structure
```bash
GenreGennie/
│── data/                 # Dataset (genres_original)
│── models/               # Saved model (genre_classifier.pkl)
│── train.py              # Train the model
│── predict.py            # Predict genre from audio
│── app.py                # Streamlit web app
│── genre_features.csv    # Extracted features (auto-generated)
```

⚙️ Installation
# Clone the repository
```bash
git clone https://github.com/yourusername/GenreGennie.git
cd GenreGennie
```
# Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
# Install dependencies
```
pip install -r requirements.txt
```
requirements.txt should include:

librosa
numpy
pandas
scikit-learn
joblib
streamlit
tqdm
matplotlib

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to add.

📜 License

This project is licensed under the MIT License.

❤️ Author

Shreya R. Devadiga
