import requests
from bs4 import BeautifulSoup
from gtts import gTTS

def extract_text(url):
  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
  }
  
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')

    article_text = " ".join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])

    if not article_text:
        article_text = soup.body.get_text().strip() if soup.body else "No readable text found"

    return article_text
  
  except requests.RequestException as error:
    return f"Error fetching the URL! {error}"

def text_to_speech(text, outfilename="output.mp3"):
  print("Converting text to audio...")
  tts = gTTS(text=text, lang='en', slow=False)
  tts.save(outfilename)
  print(f"Audio savd as {outfilename}")

if __name__ == "__main__":
  test_url = "https://example.com"
  print(f"Scraping: {test_url}")
  text = extract_text(test_url)

  print("\nBeginning of text found: ")
  print(text[:300] + "...")

  text_to_speech(text)
