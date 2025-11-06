import os, sys
import google.generativeai as genai
from dotenv import load_dotenv

# --- Setup env & API ---
load_dotenv()
gkey = os.getenv("GOOGLE_API_KEY")
if not gkey:
    print("❌ GOOGLE_API_KEY missing. Put it in .env (GOOGLE_API_KEY=...)")
    sys.exit(1)

genai.configure(api_key=gkey)

# Start solid; switch with /model gemini-flash-latest for speed
MODEL = "gemini-pro-latest"

# --- Personality: Playful + Smart, ~80% Nerdy ---
SYSTEM_PROMPT = (
    "You are SMIR, a playful and smart terminal coding buddy.\n"
    "Tone: 80% technical depth, 20% light humor. Friendly, confident, a bit nerdy.\n"
    "Rules:\n"
    "• Lead with the solution. Keep lines short; avoid rambles.\n"
    "• Use precise, correct tech details; cite assumptions.\n"
    "• Sprinkle small, tasteful jokes or metaphors—never spammy.\n"
    "• When code helps, provide runnable, fenced code blocks with language tags.\n"
    "• Prefer bullet points, edge cases, and a quick 'Next steps' section.\n"
    "• If user asks for commands, show exact commands.\n"
    "• Avoid slang overload; emojis okay but minimal (e.g., 0–2 per answer).\n"
)

def new_chat(model_name: str):
    model = genai.GenerativeModel(
        model_name=model_name,
        system_instruction=SYSTEM_PROMPT
    )
    return model, model.start_chat(history=[])

def main():
    global MODEL
    print("✨ SMIR online — playful + smart, ~80% nerdy.")
    print("Tips: /exit, /reset, /model gemini-flash-latest  or  /model gemini-pro-latest")

    model, chat = new_chat(MODEL)
    print("SMIR: Hey! What shall we build or debug today? 🔧🧠")

    while True:
        try:
            u = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nSMIR: Bye! 👋")
            break

        if not u:
            continue

        # exit in both forms
        if u.lower() in {"/exit", "exit", "/quit", "quit"}:
            print("SMIR: Later! Ship it like a pro ✌️")
            break

        # reset session
        if u.lower() == "/reset":
            model, chat = new_chat(MODEL)
            print("SMIR: Fresh context loaded. 🧼")
            continue

        # switch model quickly
        if u.lower().startswith("/model"):
            parts = u.split(maxsplit=1)
            if len(parts) == 1:
                print("SMIR: Use /model gemini-flash-latest  or  /model gemini-pro-latest")
                continue
            new_model = parts[1].strip()
            try:
                model, chat = new_chat(new_model)
                MODEL = new_model
                print(f"SMIR: Model switched → {MODEL}. Context reset.")
            except Exception as e:
                print("‼️ Error switching model:", e)
            continue

        # normal chat
        try:
            resp = chat.send_message(u)
            text = (resp.text or "(no response)").strip()
            print("SMIR:", text)
        except Exception as e:
            msg = str(e)
            if "404" in msg and "model" in msg.lower():
                print("‼️ Model not found/allowed. Try: /model gemini-flash-latest")
            elif "Permission" in msg or "permission" in msg.lower():
                print("‼️ Permission error. Your key may not have access. Try flash-latest.")
            else:
                print("‼️ Error:", e)

if __name__ == "__main__":
    main()
