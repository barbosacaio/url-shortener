from flask import Flask, request
from app.api.shortener import shorten_url, expand_url

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/urls', methods=['POST'])
def urls():
    base_url = request.host_url
    url = request.args.get('url', '')
    shortened_url = shorten_url(url)
    expanded_url = expand_url(shortened_url)
    return {
        'original_url': url,
        'shortened_url': f'{base_url}{shortened_url}',
        'expanded_url': expanded_url
    }