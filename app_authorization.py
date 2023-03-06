from requests import post
import os
import base64
import json

## from TEST APP in developer Dashboard
CLIENT_ID = "5a7aaaee3e1d455c8d8e14d43fc1d1b0"
CLIENT_SECRET = "8ab3610d092949dd9ebbe6342fdc2e34"

def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def main():
    token = get_token()
    auth_header = get_auth_header(token)


if __name__ == '__main__':
    main()
