from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import os

from scraper import extract_text, text_to_speech

app = FastAPI()

class URLRequest(BaseModel):
  url: str
 
@app.post("/convert")
def convert_url_to_audio(request: URLRequest):
  if not request.url.strip():
    raise HTTPException(status_code=400, detail="URL Cannot Be Empty!")
  print(f"Received request to convert: {request.url}")
  
  text = extract_text(request.url)
  print(f"DEBUG: Scraped text length is {len(text)} chars.")

  if "Error fetching the URL!" in text:
    raise HTTPSException(status_code=400, detail=text)
  if not text.strip():
    raise HTTPSException(status_code=400, detail="Unable to extract readable text from webpage...")
  
  import os
  current_dir = os.path.dirname(os.path.abspath(__file__))
  absolute_file_path = os.path.join(current_dir, "server_output.mp3")
  text_to_speech(text, absolute_file_path)

  return FileResponse(
    path=absolute_file_path,
    media_type="audio/mpeg",
    filename="article_audio.mp3"
  )

@app.get("/", response_class=HTMLResponse)
def read_root():
  with open("index.html", "r") as f:
    return f.read()
