# Link2Listen

Link2Listen is a full-stack web application built with Python, FastAPI, and Tailwind CSS.

Link2Listen converts any article URL into an audio format to allow users to multitask their studying.

It scrapes and cleans the article contents and uses Google's Text-to-Speech engine to play audio.

## Features
* **Sraping:** Dynamically isolates the article body text using BeautifulSoup4.
* **Text-to-Speech:** Uses Google TTS (gTTS) to read the text.
* **Dashboard:** Stylized with Tailwind CSS
* **Loading:** Loading states to notify the audio is being created.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Frontend:** HTML5, JavaScript (Fetch API), Tailwind CSS v4
* **Scraper & Audio:** BeautifulSoup4, Requests, gTTS

## Local Setup

To run this project locally, have Python 3.10+ installed:

1. **Clone the repository:**
```bash
   git clone [https://github.com/YOUR_USERNAME/Link2Listen.git](https://github.com/YOUR_USERNAME/Link2Listen.git)
   cd Link2Listen
```
2. **Install Python Packages:**
```bash
pip install fastapi uvicorn requests beautifulsoup4 gtts
```
3. **Start FastAPI Backend Server:**
```bash
uvicorn main:app --reload
```
4. **Launch:***
Open your browser and navigate to http://127.0.0.1:8000
