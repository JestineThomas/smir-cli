\# SMIR – Fast AI CLI Chatbot (Powered by Gemini and uv)



SMIR is a playful, smart, mostly technical terminal‑based AI chatbot built using Google Gemini and uv for dependency and environment management.  

It runs directly from the terminal, responds fast, and helps with coding, debugging, learning, and idea exploration.



---



\## Features



\- Fast replies using `gemini-flash-latest`

\- Higher quality answers using `gemini-pro-latest`

\- Slightly playful but mostly technical tone

\- Adjustable response length (`/short` or `/normal`)

\- Reset conversation any time

\- Switch models instantly

\- Works fully in the terminal using uv



---



\## Tech Stack



| Component | Purpose |

|----------|-----------|

| Python | Core language |

| uv | Dependency and environment manager |

| Google Gemini API | AI model |

| python-dotenv | Loads API key from `.env` |



---



\## Project Structure



```

smir-cli/

│  gemini\_cli.py       # Main SMIR CLI chatbot

│  .env                # Gemini API Key (DO NOT COMMIT)

│  pyproject.toml      # uv project configuration

│  README.md           # Documentation (this file)

└─ logs/               # Optional, stores chat logs

```



---



\## Setup (using uv)



Prerequisite: Install uv from https://docs.astral.sh/uv/



\### 1. Create or open the project



If cloning from GitHub:



```bash

git clone https://github.com/<your-username>/smir-cli.git

cd smir-cli

```



If running locally, open your project folder normally.



---



\### 2. Create `.env` for your Gemini API key



Create a file named `.env` inside the project and add:



```

GOOGLE\_API\_KEY=your\_api\_key\_here

```



Do not share or commit this file.



---



\### 3. Install dependencies



```bash

uv add google-generativeai python-dotenv

```



This updates `pyproject.toml` and installs the required packages.



---



\### 4. Run SMIR



```bash

uv run python gemini_cli.py

```



---



\## Commands



| Command | Description |

|----------|----------------------------|

| `/exit` or `exit` | Quit SMIR |

| `/reset` | Reset the chat context |

| `/fast` | Switch to `gemini-flash-latest` (fast mode) |

| `/quality` | Switch to `gemini-pro-latest` (quality mode) |

| `/short` | Short replies (128 tokens) |

| `/normal` | Normal replies (512 tokens) |

| `/model <name>` | Switch to a specific Gemini model |



---



\## Example Usage



```

/fast

Explain API in 3 lines

/quality

Write a Python function to check prime numbers

```



---



\## Important Notes



\- Do not commit `.env`

\- If replies are slow, use `/fast` and `/short`

\- If a model error occurs, switch to:



```

/model gemini-flash-latest

```



---



\## Future Enhancements



\- `/concise` mode for 5‑line maximum answers

\- `/save` to save selected responses

\- Coloured terminal output

\- Project‑aware mode to reference local code



---



\## Author



Made with Python, uv, and Gemini  

Created by Jestine



