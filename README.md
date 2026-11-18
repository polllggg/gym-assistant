# Gym Assistant — LLM Telegram Bot

A conversational assistant for a gym in Rome, built on the OpenAI API. It answers
membership, schedule and booking questions in natural, multi-turn dialogue — in
whatever language the user writes in.

## What it does

- Answers questions about membership plans, class schedules, opening hours and location
- Books free trials by collecting name, phone and preferred time
- Holds a coherent multi-turn conversation by keeping per-dialogue history
- Replies in the user's own language automatically

## How it's built

- **LLM:** OpenAI `gpt-4o-mini`, steered by a single system prompt that encodes the
  gym's plans, schedule, hours and booking rules — the behaviour lives in the prompt,
  not in hard-coded branches.
- **Conversation state:** message history is passed back on every turn, so context
  carries across the dialogue instead of each message being answered in isolation.
- **Two entry points:**
  - `gym_assistant.py` — CLI version for fast local iteration on the prompt
  - `telegram_bot.py` — Telegram deployment
- **Config & secrets:** API keys come from environment variables
  (`OPENAI_API_KEY`, `TELEGRAM_TOKEN`) — nothing sensitive in the code.
- **Deployment:** `Procfile` + `runtime.txt` for Railway / Heroku-style hosting.

## Run locally

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="your-openai-key"
export TELEGRAM_TOKEN="your-telegram-bot-token"   # only for telegram_bot.py

python gym_assistant.py     # CLI
python telegram_bot.py      # Telegram
```

## What this project is about

Taking an LLM from a prompt in a notebook to a deployed product: designing a system
prompt that stays on-topic and accurate across turns, managing conversation state,
keeping secrets out of the code, and shipping it somewhere it actually runs.

## Tech stack

Python · OpenAI API · python-telegram-bot · environment-based config · Railway
