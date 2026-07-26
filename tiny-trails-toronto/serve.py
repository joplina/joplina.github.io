from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
import webbrowser

ROOT = Path(__file__).resolve().parent
PORT = 8000

if __name__ == "__main__":
    os.chdir(ROOT)
    url = f"http://localhost:{PORT}"
    print(f"Tiny Trails Toronto is running at {url}")
    try:
        webbrowser.open(url)
    except Exception:
        pass
    ThreadingHTTPServer(("127.0.0.1", PORT), SimpleHTTPRequestHandler).serve_forever()
