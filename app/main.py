from fastapi import FastAPI
from app.routes.mood_routes import router as mood_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

@app.middleware("http")
async def log_requests(request, call_next):
    # Registrar la solicitud
    body = await request.body()
    print(f"REQUEST METHOD: {request.method}")
    print(f"REQUEST URL: {request.url}")
    print(f"REQUEST HEADERS: {request.headers}")
    print(f"REQUEST BODY: {body.decode('utf-8')}")  # Convertir el cuerpo a texto legible

    # Continuar procesando la solicitud
    response = await call_next(request)

    # Registrar la respuesta
    print(f"RESPONSE STATUS: {response.status_code}")
    return response

@app.get("/")
def root():
    return {"message": "Welcome to my API"}