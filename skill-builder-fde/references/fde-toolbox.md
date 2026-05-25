# FDE Toolbox
# The tools FDEs actually use day-to-day.
## Postman — test APIs before writing code
Test any API endpoint visually without writing a single line of Python first.
Set headers, auth, and body in the UI, hit Send, see the response.
**Use when:** you have API docs and want to confirm the endpoint works before scripting it.
**Get started:** download at postman.com, create a free account, create a Collection for each client.
## ngrok — expose localhost to the internet
Gives your local machine a public URL so external services can send webhooks to it during development.
**Use when:** you're building a webhook receiver and need to give a provider a real URL to call.
**Get started:** `brew install ngrok` → `ngrok http 5000` → copy the https URL.
## Retool — build internal dashboards without React
Drag-and-drop UI builder that connects directly to APIs and databases.
Build a working admin dashboard in hours instead of days.
**Use when:** a customer needs a UI to view/manage data and you don't want to build a React app.
**Get started:** retool.com → free tier → connect a database or REST API → drag in a Table component.
## Streamlit — Python-powered data dashboards
Turn a Python script into a shareable web dashboard with almost no extra code.
**Use when:** the customer is technical enough to run Python, or you want a quick demo to share via URL.
**Get started:** `pip install streamlit` → write `dashboard.py` → `streamlit run dashboard.py`.
## n8n — visual automation workflows
Open-source alternative to Zapier. Connect systems with a node-based visual editor.
**Use when:** the integration is straightforward (trigger → transform → send) and doesn't need custom logic.
**Get started:** n8n.io → cloud version or self-host with Docker.
## DBeaver — GUI for querying databases
Free desktop app that connects to PostgreSQL, MySQL, SQLite, and most other databases.
Write and run SQL queries visually without a terminal.
**Use when:** you need to explore a customer's database or run ad-hoc queries.
**Get started:** dbeaver.io → download Community Edition → New Connection → pick your database type.
