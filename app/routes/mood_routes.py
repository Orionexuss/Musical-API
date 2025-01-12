from fastapi import APIRouter, Depends, Request, HTTPException, status
from app.models.models import MoodRequest
from app.services.spotify_service import get_recommended_tracks
from app.services.mood_analysis import analyze_sentiment
from app.services.redis_service import RedisService
from app.utils.dependencies import get_redis_service

router = APIRouter()

# Get the text from the user and return the mood using analyze_sentiment()
@router.post("/analyze-mood")
async def analyze_mood(text: MoodRequest, redis_mood: RedisService = Depends(get_redis_service)):
    
    mood = analyze_sentiment(text.text) # The NLP analyzes the user's mood
    
    # Save mood in Redis
    redis_mood.set_value('mood', mood)

    return {
    "data": {"text": text.text, "mood": mood},
    "message": "Welcome to my Spotify App <a href='/mood/authorize'>Login with Spotify</a>"
    }   


@router.get("/recommend-playlist")
async def recommend_playlist(request: Request, redis_mood: RedisService = Depends(get_redis_service)):
    
    # Cannot access the endpoint if not authenticated with Spotify
    if 'access_token' not in request.session:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= 'You are not logged in to Spotify')
        
    access_token = request.session['access_token']
    
    # Get mood from Redis
    mood = redis_mood.get_value('mood')
    
    recommendations = get_recommended_tracks(mood, access_token) # Get 3 songs based on mood
    
    return {"mood": mood, "playlist": recommendations}

