import requests

from validator import validate_url


def send_http_request(url: str):
    if not validate_url(to_be_url=url):
        raise ValueError("Invalid string was entered as a url. please try again...")
    requests.get(url, timeout=5)  # waits 5 seconds until connection timeout is raised

