import importlib
import subprocess
import sys

# -----------------------------------------
# 1. Define your required libraries
# -----------------------------------------
REQUIRED_LIBRARIES = [
    "numpy",
    "requests",
    "torch",        # remove if not using PyTorch
    "transformers"  # remove if not using HuggingFace
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
# 3. Safe import wrapper
# -----------------------------------------
def safe_import(lib):
    try:
        return importlib.import_module(lib)
    except ImportError:
        print(f"[ERROR] Failed to import {lib} even after installation")
        return None

# -----------------------------------------
# 4. Your AI logic lives here
# -----------------------------------------
def run_ai():
    np = safe_import("numpy")
    torch = safe_import("torch")
    transformers = safe_import("transformers")

    print("\n[AI] Running your AI logic...")
    # -------------------------------------
    # Add your model loading, inference, etc.
    # -------------------------------------
    # Example placeholder:
    print("[AI] Placeholder: model would run here")

# -----------------------------------------
# 5. Main entry point
# -----------------------------------------
if __name__ == "__main__":
    print("[SYSTEM] Checking dependencies...")
    install_missing_libraries()

    print("\n[SYSTEM] Starting AI program...")
    run_ai()