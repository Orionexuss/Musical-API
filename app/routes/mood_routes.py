from fastapi import APIRouter
from app.models.models import MoodRequest
from ..services.mood_analysis import analyze_sentiment



router = APIRouter()


# Here we will get the text from the user and return the mood using analyze_sentiment()
@router.post("/analyze-mood")
async def analyze_mood(text: MoodRequest):
    
    # Placeholder for mood analisys 
    mood = analyze_sentiment(text.text) # Here we will use NLP to analyze the user mood
    return {"text": text.text, "mood": mood}

@router.get("/recommend-playlist")
async def recommend_playlist(mood: str):
    # This endpoint will generate a playlist based on the user's mood
    
    # Placeholder for recommendations 
    playlist = ["song1", "song2", "song3"] #Here we will use the streaming API
    return {"mood": mood, "playlist": playlist}

    