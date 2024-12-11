from fastapi import FastAPI
from app.routes.mood_routes import router as mood_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(mood_router, prefix="/mood", tags=["Mood Analysis"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to my API"}