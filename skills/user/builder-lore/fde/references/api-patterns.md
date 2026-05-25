# API Patterns Reference
# OAuth, pagination, rate limiting, and webhooks.
## API Key auth (most common)
```python
headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
# or
headers = {"X-API-Key": os.getenv('API_KEY')}
```
## OAuth 2.0 (conceptual flow)
```
1. Redirect user to provider login URL (with client_id, scope, redirect_uri)
2. User logs in → provider sends back a `code`
3. Exchange `code` for access_token (POST to token endpoint)
4. Use access_token in Authorization header for all future requests
5. Refresh with refresh_token when access_token expires
```
```python
# Exchange code for token
response = requests.post("https://provider.com/oauth/token", data={
    "grant_type": "authorization_code",
    "code": code,
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "redirect_uri": "https://yourapp.com/callback"
})
token = response.json()["access_token"]
```
## Pagination (offset-based)
```python
def get_all_records(base_url: str) -> list:
    all_records = []
    page = 1
    while True:
        response = requests.get(base_url, params={"page": page, "per_page": 100}, headers=headers)
        data = response.json()
        if not data:  # empty page = done
            break
        all_records.extend(data)
        page += 1
    return all_records
```
## Rate limiting (handle 429 errors)
```python
import time
def get_with_retry(url: str, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 429:
            wait = int(response.headers.get("Retry-After", 5))
            print(f"Rate limited. Waiting {wait}s...")
            time.sleep(wait)
            continue
        response.raise_for_status()
        return response.json()
    raise Exception("Max retries exceeded")
```
## Webhook receiver (Flask)
```python
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def handle():
    data = request.json
    print("Received:", data)
    # process data here
    return jsonify({"status": "ok"}), 200
if __name__ == '__main__':
    app.run(port=5000)
```
## Test with ngrok (expose localhost)
```bash
ngrok http 5000
# Gives you: https://abc123.ngrok.io → your localhost:5000
# Use that URL as your webhook endpoint in the provider's dashboard
```
