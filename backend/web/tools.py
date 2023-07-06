import requests


f = dict(open("config.env", "rt").read())
API_ENDPOINT = 'https://discord.com/api/v10'
CLIENT_ID = '1125149818793230447'
CLIENT_SECRET = f["secret_key"]
REDIRECT_URI = 'https://localhost:8000'


def exchange_code(code: str):
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post("%s/oauth2/token" % API_ENDPOINT, data=data, headers=headers)
    r.raise_for_status()
    return r.json()
