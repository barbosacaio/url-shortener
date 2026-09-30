import base64

def shorten_url(url: str) -> str:
    shortened = base64.urlsafe_b64encode(url.encode('utf-8')).decode('ascii')
    return shortened

def expand_url(shortened_url: str) -> str:
    try:
        expanded = base64.urlsafe_b64decode(shortened_url).decode('utf-8')
        return expanded
    except Exception:
        return None