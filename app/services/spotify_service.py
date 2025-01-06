import requests
import random

# Playlists IDs
SAD = '0qaIzNNRaEZzkG0bfYlYg3'
NEUTRAL = '48gsC1F8hqKTfsuvLnvZbW'
HAPPY = '3Hs562oYeOsTcNmiUSj0f8'

# Assign a playlist ID to each possible mood
MOOD_PLAYLISTS  = {
    "sad":       SAD,
    "very sad":  SAD,
    "neutral":   NEUTRAL,
    "happy":     HAPPY,
    "very happy": HAPPY,
}


# Filter Spotify response to get 3 random songs
def filter_spotify_songs(playlist_response:dict):
    tracks = random.sample(playlist_response['tracks']['items'], k= 3)
    result = []
    
    for item in tracks:
        track_info = {
            'track_name' : item['track']['name'],
            'artist_name' : [artist['name'] for artist in item['track']['artists']],
            'spotify_url' : item['track']['external_urls']['spotify']
        }
        
        result.append(track_info)
        
    return result

    
def get_recommended_tracks(mood: str, access_token: str):
    headers = {'Authorization': f'Bearer {access_token}'}
    
    response = requests.get(f'https://api.spotify.com/v1/playlists/{MOOD_PLAYLISTS[mood]}', headers= headers)
    
    result = response.json()
    
    filtered = filter_spotify_songs(result)
    
    return filtered





    