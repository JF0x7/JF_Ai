import importlib
import subprocess
import sys
import requests

# -----------------------------------------
# 1. Required libraries
# -----------------------------------------
REQUIRED_LIBRARIES = [
    "requests"
]

# -----------------------------------------
# 2. Auto-installer
# -----------------------------------------
def install_missing_libraries():
    for lib in REQUIRED_LIBRARIES:
        try:
            importlib.import_module(lib)
            print(f"[OK] {lib} already installed")
        except ImportError:
            print(f"[INSTALL] {lib} not found — installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# -----------------------------------------
# 3. Simple built-in knowledge base
# -----------------------------------------
def local_answers(question):
    q = question.lower()

    knowledge = {
        "your name": "I'm a simple Python AI you built.",
        "who made you": "You did — and you're upgrading me fast.",
        "weather": "I can't fetch live weather yet, but Calgary is usually cold this time of year.",
        "hello": "Hey! Ask me anything.",
        "hi": "Hi there!"
    }

    for key in knowledge:
        if key in q:
            return knowledge[key]

    return None  # means “I don’t know this one yet”

# -----------------------------------------
# 4. Internet search fallback
# -----------------------------------------
def search_internet(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1&no_html=1"
        response = requests.get(url).json()

        # Try to extract a meaningful answer
        if response.get("AbstractText"):
            return response["AbstractText"]

        if response.get("RelatedTopics"):
            for item in response["RelatedTopics"]:
                if "Text" in item:
                    return item["Text"]

        return "I searched the internet but couldn't find a clear answer."
    except Exception:
        return "Internet search failed — maybe no connection."

# -----------------------------------------
# 5. AI brain: multi-question loop
# -----------------------------------------
def run_ai():
    print("\n[AI] Ask me anything. Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("[AI] Goodbye.")
            break

        # 1. Try local knowledge
        local = local_answers(user_input)
        if local:
            print(f"[AI] {local}")
            continue

        # 2. Otherwise search the internet
        print("[AI] Let me check the internet...")
        answer = search_internet(user_input)
        print(f"[AI] {answer}")

# -----------------------------------------
# 6. Entry point
# -----------------------------------------
if __name__ == "__main__":
    print("[SYSTEM] Checking dependencies...")
    install_missing_libraries()

    print("\n[SYSTEM] Starting AI program...")
    run_ai()