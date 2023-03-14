import os
from dotenv import load_dotenv
from requests import post
import base64
import json

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')


def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    # URL and dictionaries for POST request, as defined in API docs
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # POST request and JSON result, from which a token is obtained
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)  # a dictionary is returned
    token = json_result["access_token"]  # 'token_type', 'expires_in' omitted

    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def main():
    token = get_token()
    auth_header = get_auth_header(token)


if __name__ == '__main__':
    main()
