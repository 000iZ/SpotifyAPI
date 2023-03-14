from app_authorization import get_token, get_auth_header

from requests import get
import json

def get_artist_ID(token, header, artist_name):
    url = "https://api.spotify.com/v1/search"
    header = header

    query = f"?q={artist_name}&type=artist&limit=1"  # restrict to 1 artist
    query_url = url + query
    result = get(query_url, headers = header)  # a get as opposed to post
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print("No artist found with this name")

        return None
    else:
        return json_result[0]


def get_artist_tracks(token, id, locale):
    url = f"https://api.spotify.com/v1/artists/{id}/top-tracks?country={locale}"
    header = get_auth_header(token)
    result = get(url, headers = header)

    json_result = json.loads(result.content)["tracks"]

    return json_result


def main():
    token = get_token()
    auth_header = get_auth_header(token)

    print(chr(27) + "[2J")  # clear terminal using escape sequences

    artist_ID = get_artist_ID(token, auth_header, "John Frusciante")["id"]
    print(f"Artist ID: {artist_ID}")

    artist_tracks = get_artist_tracks(token, artist_ID, "US")
    for i, track in enumerate(artist_tracks):
        print(f"{(i + 1)}. {track['name']}")


if __name__ == '__main__':
    main()
