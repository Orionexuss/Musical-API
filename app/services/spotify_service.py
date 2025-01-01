import requests

# Playlists IDs
SAD = '0qaIzNNRaEZzkG0bfYlYg3'
NEUTRAL = '48gsC1F8hqKTfsuvLnvZbW'
HAPPY = '3Hs562oYeOsTcNmiUSj0f8'

# Asigning a playlist to each possible mood
MOOD_PLAYLISTS  = {
    "sad":       {f'https://api.spotify.com/v1/playlists/{SAD}'},
    "very sad":  {f'https://api.spotify.com/v1/playlists/{SAD}'},
    "neutral":   {f'https://api.spotify.com/v1/playlists/{NEUTRAL}'},
    "happy":     {f'https://api.spotify.com/v1/playlists/{HAPPY}'},
    "very happy":{f'https://api.spotify.com/v1/paylists/{HAPPY}'},
}


def get_recommended_tracks(mood: str, access_token: str):
    
    headers = {'authorization' f'Bearer {access_token}'}
    response = requests.get(f'{MOOD_PLAYLISTS[mood]}', headers= headers)
    result = response.json()
    items = response['tracks']['items']

    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get("sad", headers=headers)
    response.raise_for_status()
    return response.json()

    """
    Get a list of recommended tracks based on the user's mood.
    """
    mood_to_genre = {
        "happy": "pop",
        "very happy": "dance",
        "neutral": "acoustic",
        "sad": "piano",
        "very sad": "ambient"
    }
    
    # implement logic with Spotify API to return the accurate tracks based on mood...

    