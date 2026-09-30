from flask import Flask, redirect, request
from app.api.shortener import shorten_url, expand_url
import validators

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/urls', methods=['POST'])
def urls():
    url = request.args.get('url', '')

    if validators.url(url):
        shortened_url = shorten_url(url)
        return shortened_url
    else:
        return '<p>Invalid URL</p>', 400

@app.route('/<shortened_url>', methods=['GET'])
def redirect_to_original(shortened_url):
    expanded_url = expand_url(shortened_url)
    if expanded_url:
        return redirect(expanded_url, code=302)
    else:
        return '<p>Invalid shortened URL</p>', 404