import validators


def validate_url(to_be_url: str):
    return validators.url(to_be_url) is True
