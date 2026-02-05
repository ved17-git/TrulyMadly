# GenAI Multi-Agent Assistant — TrulyMadly Assignment

This project is a CLI-based GenAI assistant built using a **multi-agent architecture**.
It accepts natural language tasks, plans actions using an LLM, executes real API calls, and verifies results before producing a final response.

---

## 🧠 Architecture Overview

The system is composed of three agents working sequentially:

### 1️⃣ Planner Agent

* Interprets the user’s natural language request
* Breaks it into structured executable steps
* Outputs a JSON plan
* Selects which tools (APIs) to call

---

### 2️⃣ Executor Agent

* Executes each planned step
* Calls real third-party APIs
* Collects structured outputs
* Handles tool execution errors gracefully

---

### 3️⃣ Verifier Agent

* Reviews execution outputs
* Validates completeness
* Produces a clean, human-readable summary
* Ensures the final response answers the user’s task

---

## 🔌 Integrated APIs

The system integrates real external APIs:

### • GitHub Search API

Used to fetch top repositories based on:

* Stars
* Topics
* Language filters

### • Weather API

Used to fetch:

* Current temperature
* Weather condition
* City-level data

No responses are hardcoded — all data is fetched live.

---

## ⚙️ Setup Instructions (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ved17-git/TrulyMadly.git
cd TrulyMadly
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory.

Use the following structure:

```env
GROQ_API_KEY=your_groq_api_key
GITHUB_TOKEN=your_github_token
WEATHER_API_KEY=your_weather_api_key
```

---

### 4️⃣ Run the Project

```bash
python main.py
```

The assistant runs locally via CLI.

---

## 🧪 Example Prompts

Use the following prompts to test the system:

1. **Find top AI GitHub repos**
2. **Weather in London**
3. **Find top AI GitHub repos and weather in London**
4. **Find popular Python AI repositories**
5. **Weather in New York**

---

### Invalid Prompt Handling

If the user enters unsupported input like:

```
hello
hi
random text
```

The system returns a clean guidance message instead of crashing.

Example:

> “I can currently help with GitHub repo searches and weather lookups…”

---

## ⚠️ Known Limitations / Trade-offs

* Only supports implemented tools (GitHub + Weather)
* General chat is intentionally not supported
* Planner may generate multiple repo queries
* CLI-only interface (no web UI)
* Depends on external API rate limits

---

## 🧩 Project Structure

```
agents/
 ├── planner_agent.py
 ├── executor_agent.py
 └── verifier_agent.py

tools/
 ├── github_tool.py
 └── weather_tool.py

llm/
 └── llm_client.py

main.py
requirements.txt
.env.example
README.md
```

---

## 🔐 Environment File Example


```env
GROQ_API_KEY=your_key_here
GITHUB_TOKEN=your_token_here
WEATHER_API_KEY=your_key_here
```

---

## ✅ Assignment Compliance Checklist

| Requirement                   | Status             |
| ----------------------------- | ------------------ |
| Multi-agent design            | ✔ Implemented      |
| Planner / Executor / Verifier | ✔ Implemented      |
| LLM structured planning       | ✔ Implemented      |
| ≥2 real APIs                  | ✔ GitHub + Weather |
| End-to-end execution          | ✔ Working          |
| No hardcoded responses        | ✔ Confirmed        |
| Local runnable                | ✔ Single command   |

---

