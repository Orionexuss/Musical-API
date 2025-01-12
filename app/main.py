from fastapi import FastAPI
import os
from app.routes.mood_routes import router as mood_router
from app.routes.spotify_routes import router as spotify_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.include_router(mood_router, prefix="/mood", tags=["Mood Analysis"])
app.include_router(spotify_router, tags=["Authorization Flow"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.add_middleware(SessionMiddleware, os.getenv('SECRET_KEY'))

@app.get('/')
def index():
    return RedirectResponse('/mood/analyze-mood')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app.main:app', host="localhost", port=8000, reload=True)