# 🎵 GenreGennie – Music Genre Classification using ML & Audio Processing

**GenreGennie** is a machine learning–powered music genre classification system that analyzes audio files and predicts their genre.  
It uses **MFCC feature extraction**, a **Random Forest classifier**, and a clean **Streamlit web interface** to deliver fast and accurate predictions.

This project demonstrates end-to-end ML development — from preprocessing and model training to deployment.

---

## 🚀 Features

- 🎶 **Automatic MFCC feature extraction** using Librosa  
- 🧠 **Random Forest classifier** trained on labeled audio datasets  
- 💾 **Model saving & loading** with Joblib  
- 🎧 **Streamlit-based interactive web app** for genre prediction  
- 📊 **Complete ML pipeline** → preprocessing → feature extraction → training → prediction  
- 🧱 Modular & easy-to-extend project structure  

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Librosa** – Audio feature extraction  
- **NumPy, Pandas** – Data processing  
- **Matplotlib** – Visualization  
- **Scikit-learn** – Machine Learning  
- **Joblib** – Model persistence  
- **Streamlit** – Web app interface  

---

## 📂 Project Structure

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
```
librosa
numpy
pandas
scikit-learn
joblib
streamlit
tqdm
matplotlib
```
▶️ Running the Application


🧠 Train the model
```
python train.py
```
🎵 Predict genre from an audio file
```
python predict.py path/to/audiofile.wav
```
🌐 Launch the Streamlit Web App
```
streamlit run app.py
```
🤝 Contributing

Contributions are welcome!
If you’d like to add new features or improve existing ones:

Fork the repo

Create a new branch

Make your changes

Submit a pull request

For major changes, please open an issue first to discuss them.

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this software with attribution.

❤️ Author

Shreya R

