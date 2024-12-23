from fastapi import APIRouter
from app.models.models import MoodRequest
from app.services.spotify_service import get_recommended_tracks
from ..services.mood_analysis import analyze_sentiment

router = APIRouter()


# Here we will get the text from the user and return the mood using analyze_sentiment()
@router.post("/analyze-mood")
async def analyze_mood(text: MoodRequest):
    
    mood = analyze_sentiment(text.text) # Here we will use NLP to analyze the user mood
    return {
    "data": {"text": text.text, "mood": mood},
    "message": "Welcome to my Spotify App <a href='/mood/authorize'>Login with Spotify</a>"
}


@router.get("/recommend-playlist")
async def recommend_playlist(mood: str):
    # This endpoint will generate a playlist based on the user's mood
    
    # Here we will show the recommendations (We will work on this later on)
    playlist = get_recommended_tracks(mood) 
    return {"mood": mood, "playlist": playlist}

    