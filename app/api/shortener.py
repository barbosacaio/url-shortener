import base64
import sqlite3
from flask import request

def shorten_url(url: str) -> str:
    try:
        shortened = base64.urlsafe_b64encode(url.encode('utf-8')).decode('ascii')

        conn = sqlite3.connect('app/database/urls.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO urls (shortened_url, expanded_url) VALUES (?, ?)', (shortened, url))
        conn.commit()
        conn.close()

        base_url = request.host_url
        return f'{base_url}{shortened}'
    except Exception as error:
        return f'Error shortening URL: {error}', 500

def expand_url(shortened_url: str) -> str:
    try:
        conn = sqlite3.connect('app/database/urls.db')
        cursor = conn.cursor()
        cursor.execute('SELECT expanded_url FROM urls WHERE shortened_url = ?', (shortened_url,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0]
        else:
            return 'Not found', 404
    except Exception as error:
        return f'Error expanding URL: {error}', 500