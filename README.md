# Golden Globes Tweet Mining Project

## Setup Instructions

## 1. Create a virtual environment:

    python -m venv venv

### Activate the virtual environment:

### On Windows:

    venv\Scripts\activate

### On macOS/Linux:

    source venv/bin/activate

## 2. Install the required packages:

    pip install -r requirements.txt

## 3. Download NLTK Data :

    python -m nltk.downloader brown punkt averaged_perceptron_tagger

## 4. Download TextBlob Corpora:

    python -m textblob.download_corpora

## 5. Run Your Script

    python main.py
