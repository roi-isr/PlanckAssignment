import requests

from utility.validator import validate_url


def send_http_request(url: str):
    if not validate_url(to_be_url=url):
        raise ValueError(f"Invalid string was entered as a url ({url}). Please try again with a valid URL...")
    response = requests.get(url, timeout=5)  # waits 5 seconds until connection timeout is raised

    return response.content  # returns responded HTML/JSON data
