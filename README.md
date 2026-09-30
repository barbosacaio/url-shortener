# Challenge #01 — URL Shortener

I'm building an API that accepts an original URL, creates a short code, and uses that code to redirect visitors. This is an individual learning project that I'll complete at my own pace while investigating implementation decisions as I go.

## Learning rules

- I won't use AI to write code, plan the solution, or answer questions. I can consult official documentation and search the web.
- I'll focus on understanding my decisions and being able to explain them afterward.
- Once the project is complete, I'll update this README with instructions for running the application, what I implemented, and the choices I made.

## Tech stack

- Python
- Flask
- SQLite

## Core requirements

- [x] `POST /urls` accepts a valid original URL and creates a short code associated with it.
- [x] `GET /:code` finds the original URL and responds with an HTTP redirect.
- [x] Invalid URLs are rejected with a clear error response.
- [x] Saved links remain available after the application restarts.
- [x] Each code identifies at most one URL; creating new links must preserve this rule.

I'll define and document the JSON request and response formats for `POST /urls`, the HTTP status codes, and the behavior for an unknown code. I'll choose a response format and use it consistently throughout the API.

## How I'll verify the project

Before considering the project complete, I'll verify:

1. Creating a short link from a valid URL.
2. Redirecting to the saved URL.
3. Rejecting an invalid URL and handling an unknown code.
4. Retrieving a link that was created before restarting the application.
5. Ensuring that different URLs never share a code, including after creating several links.

I'll use an HTTP client to check these cases and add reproducible commands or examples below.

## Running the project

> I'll add prerequisites, dependency installation, database setup, and the command to start the API once they're defined.
1. ``git clone https://github.com/barbosacaio/url-shortener``
2. ``cd url-shortener``
3. For macOS/Linux: ``python3 -m venv .venv`` — For Windows: ``py -3 -m venv .venv``
4. For macOS/Linux: ``. .venv/bin/activate`` — For Windows: ``.venv\Scripts\activate``
5. pip install Flask
6. python app/database/init_db.py
7. flask --app app/app run

## Usage examples

- ```GET http://127.0.0.1:5000/<shortened_url>``` — Expands the generated code and does a 302 redirect to the original URL
- ```POST http://127.0.0.1:5000/urls?url=<url>``` — Shortens the provided URL, assigns it's code and returns the new code

## Decisions and lessons learned

I opted for a direct URL validation using ```validators``` to simplify the process, with a direct ```UNIQUE``` constraint at the database-level to avoid conflicts while providing data persistance. Main difficulty was to simplify the conversion from URL to shortened code while keeping code simplicity. I moved forward with ```encode()``` and ```decode()``` using ```utf-8``` with ```ASCII``` for byte to string conversion, but I would focus on code simplicity in a future version.