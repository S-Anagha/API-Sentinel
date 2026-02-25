import requests
from config import DEFAULT_TIMEOUT

def send_get(url, params=None, headers=None):
    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=DEFAULT_TIMEOUT
        )
        return response
    except requests.RequestException:
        return None