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

- [ ] `POST /urls` accepts a valid original URL and creates a short code associated with it.
- [ ] `GET /:code` finds the original URL and responds with an HTTP redirect.
- [ ] Invalid URLs are rejected with a clear error response.
- [ ] Saved links remain available after the application restarts.
- [ ] Each code identifies at most one URL; creating new links must preserve this rule.

I'll define and document the JSON request and response formats for `POST /urls`, the HTTP status codes, and the behavior for an unknown code. I'll choose a response format and use it consistently throughout the API.

## Optional extensions

After completing the core requirements, I may add:

- Link expiration.
- Access counts and a statistics endpoint.
- Custom codes supplied by the client.
- Automated tests for the main flows and error cases.
- Handling concurrent code creation.

I'll document the behavior of any extensions I implement.

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
6. flask --app app run

## Usage examples

> I'll add real request and response examples for the endpoints I implement.

## Decisions and lessons learned

> I'll explain how I validate URLs, generate codes, prevent conflicts, and persist data. I'll also record difficulties, known limitations, and what I'd do differently in a future version.