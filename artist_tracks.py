from app_authorization import get_token, get_auth_header

from requests import get
import json

def get_artist_tracks(token, header, artist_name):
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


def main():
    token = get_token()
    auth_header = get_auth_header(token)

    result = get_artist_tracks(token, auth_header, "John Frusciante")
    print(result)
    

if __name__ == '__main__':
    main()


