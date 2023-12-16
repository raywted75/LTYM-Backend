import requests
import base64


# Put your Spotify API id and secret here
# client_id = ""
# client_secret = ""


def get_access_token():
    encoded = base64.b64encode((client_id + ":" + client_secret).encode("ascii")).decode("ascii")
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic " + encoded
    }
    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post("https://accounts.spotify.com/api/token", data=payload, headers=headers)
    token_info = response.json()
    return token_info.get('access_token')


def get_seeds(emotion):
    match emotion:
        case 'sadness':
            # Adele, Bon Iver, Elliot Smith
            return ["sad"], ['4dpARuHxo51G3z768sgnrY', '4LEiUm1SRbFMgfqnQTwUbQ', '2ApaG60P4r0yhBoDCGD8YG']
        case 'joy':
            # Pharrell Williams, Katy Perry, Bruno Mars
            return ["happy"], ['2RdwBSPQiwcmiDo9kixcl8', '6jJ0s89eD6GaHleKKya26X', '0du5cEVh5yTK9QJze8zA0C']
        case 'love':
            # Ed Sheeran, Beyoncé, John Legend
            return ["romance"], ['6eUKZXaKkcviH0Ku9w2n3V', '6vWDO969PvNqNYHIOW5v0m', '5y2Xq6xcjJb2jVM54GHK3t']
        case 'anger':
            # Metallica, Rage Against The Machine, Slipknot
            return ["hard-rock"], ['2ye2Wgw4gimLv2eAKyk1NB', '2d0hyoQ5ynDBnkvAbJKORj', '05fG473iIaoy82BF1aGhL8']
        case 'surprise':
            # Björk, Radiohead, Frank Zappa
            return ["experimental"], ['7w29UYBi0qsHi5RTcv3lmA', '4Z8W4fKeB5YxbusRsdQVPb', '6ra4GIOgCZQZMOaUECftGN']


def get_tracks(emotion):
    limit = 3
    market = 'US'

    seed_genres, seed_artists = get_seeds(emotion)
    seed_tracks = ['5Eevxp2BCbWq25ZdiXRwYd']

    seed_artists = '%2C'.join(seed_artists)
    seed_genres = '%2C'.join(seed_genres)
    seed_tracks = '%2C'.join(seed_tracks)

    response = requests.get(
        f"https://api.spotify.com/v1/recommendations?limit={limit}&market={market}&seed_artists={seed_artists}&seed_genres={seed_genres}&seed_tracks={seed_tracks}", 
        headers={"Authorization": f"Bearer {get_access_token()}"}
    )

    tracks = list()
    for track in response.json()['tracks']:
        tracks.append({
            'album_image': track["album"]["images"][0]["url"],
            'artist': track["artists"][0]["name"],
            'name': track["name"],
            'spotify_url': track["external_urls"]["spotify"],
            'preview_url': track["preview_url"]
        })
    
    for track in tracks:
        print("Track:", track['name'], track['artist'])

    return tracks
