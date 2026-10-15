# Performance_Review_Writer_Agent - LangChain Single Agent Project

A beginner-friendly project that teaches you how to build a **single agent** using **LangChain + OpenAI**. The agent takes a brief email idea and generates a natural, human-sounding email.

## What You'll Learn

- How LangChain works (LLMs, prompts, tools, agents)
- How to create tools using the `@tool` decorator
- How an agent decides which tools to call and in what order
- How `PromptTemplate` shapes LLM output
- How the agent's tool-calling loop works (think -> act -> observe -> repeat)

## How It Works

```
User's Performance accomplishments
       |
       v
  [Agent thinks: "I need to provide performance review on accomplishments"]
       |
       v
  [Tool: draft_performance_review] --> creates a formal, structured performance review draft
       |
       v
  [Agent thinks: "Now I should humanize this draft"]
       |
       v
  [Tool: write_review_narrative] --> rewrites it to sound natural and warm
       |
       v
  Final humanized performance review returned to user
```

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/bharathradharapu/AI-AMC-Assignment-2---LangChain-Assignment
cd Performance Review Writer Agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate
  ```
- **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example env file and add your real key:

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual OpenAI API key:

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Run

```bash
python Performance_Review_Writer_Agent.py
```

You'll see an interactive prompt:

```
Performance Review Agent (LangChain + OpenAI)
Describe the accomplishments you want to write. Type 'quit' to exit.

Your accomplishments:
```

Type accomplishments  (e.g.,`write your accomplishments` ) and the agent will generate a humanized review. You'll also see a log line for each tool the agent calls.

## Example

**Input:**
```
`i have successfully implemented end to end automation projects to clients from multiple doimains such as banking, finance, manufacturing and insurance industries. i have also provided technical training to one of the telecom client.`
```

**Output:**
```
Over the past review period, I’ve successfully delivered end-to-end automation projects for clients across different industries like banking, finance, manufacturing, and insurance. These projects didn’t just streamline their operations—they also boosted efficiency and accuracy, leading to real, measurable improvements. Handling complex projects in such varied areas really shows how adaptable I am and highlights my technical skills and project management strengths.

Beyond just delivering projects, I also took some time to provide targeted technical training to a telecom client. This wasn’t just about sharing knowledge—it helped empower their team with new skills and brought us closer as partners through solid collaboration. I see this as a reflection of my commitment to leadership and helping others grow, both within client teams and in my own professional journey.

Looking ahead, I want to build on these wins by getting involved in more cross-team projects and mentoring colleagues to boost our overall capabilities. I’m excited to keep pushing for innovative solutions that make a real difference and align well with what our organization aims to achieve.
```

## Project Structure

```
.
├── Performance_Review_Writer_Agent.py   # Main agent code
├── requirements.txt           # Python dependencies
├── .env.example               # API key template
├── .gitignore                 # Keeps secrets and venv out of git
└── README.md                  # This file
```

## Tech Stack

- [LangChain](https://python.langchain.com/) - Framework for building LLM applications
- [OpenAI GPT-4.1-mini](https://platform.openai.com/) - The LLM powering the agent
- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment variable management
