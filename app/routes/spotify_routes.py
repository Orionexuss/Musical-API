from urllib.parse import urlencode
from fastapi import APIRouter, Request
from fastapi.applications import JSONResponse
from fastapi.responses import RedirectResponse


import requests
import os

router = APIRouter()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/callback" 
TOKEN_URL = "https://accounts.spotify.com/api/token"
AUTH_URL = 'https://accounts.spotify.com/authorize'
API_URL = "https://api.spotify.com/v1"

@router.get('/mood/authorize')
def request_auth():
    auth_data = {
        'response_type' : 'code',
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'scope': 'user-top-read',
        'show_dialog': True
    }
    auth_url = f'{AUTH_URL}?{urlencode(auth_data)}'
    
    return RedirectResponse(auth_url)

@router.get("/callback")
async def callback(request: Request):
    params = request.query_params
    
    if 'error' in params:
        return JSONResponse(content={'error':params['error']})
    
    if 'code' in params:
        req_body = {
            'code': params['code'],
            'grant_type': 'authorization_code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        
    response = requests.post(TOKEN_URL, data=req_body)
    token_info = response.json()
    request.session['access_token'] = token_info['access_token']
    
    return RedirectResponse("/mood/recommend-playlist")