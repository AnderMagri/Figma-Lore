---
name: forward-deployed-engineer
description: >
  Learning companion and execution guide for a product designer becoming a Forward Deployed Engineer (FDE).
  Assumes full design knowledge and customer empathy — never explains UX or discovery concepts.
  Fills the gap between understanding systems conceptually and being able to build integrations,
  scripts, and data tooling from scratch in customer-facing contexts.
  Covers the FDE process: scoping a customer problem, designing a solution, building it fast,
  and presenting it. Includes ready-to-use Python, SQL, and API patterns for common FDE tasks.
  Use this skill whenever Ander is working on customer integrations, API connections, data scripts,
  internal tooling, automation workflows, or asking "how do I build X for a client fast".
  Also trigger for questions about Python setup, SQL queries, REST APIs, JSON data, or
  "how do I connect system A to system B".
---
# Forward Deployed Engineer Skill
## For: Product designer with full design + discovery knowledge, building technical execution fluency
---
## Core Principle
You already know how to talk to customers, frame problems, and design solutions. The gap is
**technical execution** — how to turn a scoped problem into working code that connects real systems.
Every response should:
1. Give the **process first** (what to do, in order)
2. Give the **pattern second** (the actual code to use)
3. Never explain discovery or design decisions — assume they're already made
---
## The FDE Build Process
### Scoping a customer problem → solution
```
1. Identify the data sources (what systems does the customer use?)
2. Identify the desired output (dashboard? export? automation? alert?)
3. Check what APIs/connections are available
4. Choose the simplest possible implementation
5. Build a working prototype in <1 day
6. Present, get feedback, iterate
```
FDE principle: **working beats polished**. Ship something real, then refine.
### Building a customer integration
```
1. Read the API docs for both systems
2. Get credentials — test them first in isolation
3. Fetch data from source system
4. Transform it into the shape the target system needs
5. Push or display the result
6. Add error handling last
```
---
## Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests python-dotenv pandas openpyxl
pip freeze > requirements.txt
```
```bash
# .env file (never commit this)
API_KEY=your-key-here
DATABASE_URL=your-db-url
```
```python
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('API_KEY')
```
---
## Core Patterns
### Call a REST API
```python
import requests, os
def get_data(endpoint: str) -> dict:
    response = requests.get(
        f"https://api.example.com/{endpoint}",
        headers={"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    )
    response.raise_for_status()
    return response.json()
```
### POST data to an API
```python
def create_record(payload: dict) -> dict:
    response = requests.post(
        "https://api.example.com/records",
        headers={"Authorization": f"Bearer {os.getenv('API_KEY')}", "Content-Type": "application/json"},
        json=payload
    )
    response.raise_for_status()
    return response.json()
```
### Transform JSON data
```python
raw = [{"id": 1, "full_name": "Ander", "status": "active"}, {"id": 2, "full_name": "Jane", "status": "inactive"}]
active = [{"id": u["id"], "name": u["full_name"]} for u in raw if u["status"] == "active"]
```
### Read/write CSV or Excel
```python
import pandas as pd
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
active = df[df["status"] == "active"]
df["full_label"] = df["first_name"] + " " + df["last_name"]
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
```
### Quick data dashboard (Streamlit)
```python
import streamlit as st
import pandas as pd
st.title("Customer Dashboard")
df = pd.read_csv("data.csv")
st.dataframe(df)
st.bar_chart(df.groupby("status")["id"].count())
# Run: streamlit run dashboard.py
```
---
## When You're Stuck
- **"I don't know where to start"** → Get one API call working. Just print the raw JSON. Everything else comes after.
- **"The API is returning an error"** → Print `response.status_code` and `response.text` to see why.
- **"I don't know how to transform the data"** → Print the raw data first. Understand its shape. Then describe what you want it to look like.
- **"Script, API, or dashboard?"** → Script = one-time or scheduled. API = continuous connection. Dashboard = someone needs to see it regularly.
---
## FDE Presentation Pattern
```
1. Show the output first
2. Briefly explain what it connects
3. Point out what's configurable
4. Ask: "Does this solve what you described?"
```
Never lead with architecture. Lead with the result.
---
## Design-to-FDE Translation
| Design skill | FDE equivalent |
|---|---|
| Discovery workshop | Technical scoping session |
| User flow | Data flow / integration map |
| Component | Reusable function |
| Prototype | Working script / proof of concept |
| Design tokens | Config file / .env variables |
| States (default, error) | Error handling + edge cases |
---
## Reference Files
- `references/python-essentials.md` — loops, functions, error handling, file I/O
- `references/api-patterns.md` — OAuth, pagination, rate limiting, webhooks
- `references/sql-recipes.md` — filtering, joins, aggregations, CTEs
- `references/fde-toolbox.md` — Postman, ngrok, Retool, Streamlit, n8n, DBeaver
