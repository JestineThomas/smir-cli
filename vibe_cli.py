import os, sys, traceback
from dotenv import load_dotenv
from openai import OpenAI, APIStatusError, APIConnectionError, OpenAIError

# 1) Load .env and validate key
load_dotenv()
key = os.getenv("OPENAI_API_KEY")
if not key or not key.startswith(("sk-", "sk-proj-")):
    print("❌ OPENAI_API_KEY missing/invalid. Put it in .env (starts with sk-).")
    sys.exit(1)

# 2) Client + model
client = OpenAI()   # reads key from env
MODEL = "gpt-4o-mini"   # change to a model you have access to if needed

SYSTEM_PROMPT = (
    "You are Vibe, a friendly terminal buddy. "
    "Tone: casual, energetic, a bit witty. Use short lines + emojis sometimes. "
    "Be helpful with code, but keep it chill."
)

def ask(messages):
    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=0.6,
        )
        return resp.choices[0].message.content
    except APIStatusError as e:
        print("\n🚨 APIStatusError")
        print("Status:", e.status_code)
        try:
            print("Details:", e.response.json())
        except Exception:
            print("Details:", e.response.text if getattr(e, 'response', None) else str(e))
        return "(error)"
    except APIConnectionError as e:
        print("\n🌐 Network error:", e)
        return "(network error)"
    except OpenAIError as e:
        print("\n‼️ OpenAIError:", e)
        return "(openai error)"
    except Exception as e:
        print("\n💥 Unexpected error:", e)
        traceback.print_exc()
        return "(unexpected error)"

def main():
    print("✨ Vibe CLI on. Type your message. (/exit to quit, /reset to clear)")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "assistant", "content": "Yo! 🌟 I’m Vibe. What are we building today?"}
    ]
    print("Vibe: Yo! 🌟 I’m Vibe. What are we building today?")

    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye! 👋")
            break

        if not user:
            continue
        if user.lower() in {"/exit", "exit", "quit", "/quit"}:
            print("Vibe: Later! Keep the vibes high ✌️")
            break
        if user.lower() == "/reset":
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("Vibe: Fresh start loaded. 🧼")
            continue

        messages.append({"role": "user", "content": user})
        reply = ask(messages)
        print("Vibe:", reply)
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()
