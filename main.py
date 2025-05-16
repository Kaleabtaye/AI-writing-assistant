from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import subprocess
import time
import httpx
from string import Template

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {"model": "mistral:7b-instruct-v0.2-q4_K_M",
                "keep_alive": "5m",
                "stream": False
                }
PROMPT_TEMPLATE = Template(
    """ Fix all spelling mistakes, casing issues, grammar mistakes, and punctuation errors in the provided text. Preserve all newline characters exactly as they are.

        $text

        Return only the corrected text without any explanations or additional comments.
    """
)
key_1  = Key.f9.value
key_2  = Key.f11.value
controller = Controller()

def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT, 
                          json={"prompt": prompt, **OLLAMA_CONFIG},
                          headers={"Content-Type": "application/json"},
                          timeout=10)
    if response.status_code != 200:
        return None
    return response.json()["response"].strip()

def copy_selection():
    # Simulate Ctrl+C with xdotool
    subprocess.run(["xdotool", "key", "ctrl+c"])
    time.sleep(0.1)
    return pyperclip.paste()

def select_current_line():
    print("Selecting the current line...")
    subprocess.run(["xdotool", "key", "Home"])
    time.sleep(0.1)
    subprocess.run(["xdotool", "key", "Shift+End"])
    time.sleep(0.1)

def paste_fixed_text():
    subprocess.run(["xdotool", "key", "ctrl+v"])

def fix_selection():
    # copy to clipboard
    text = copy_selection()
    # fix the text
    fixed_text = fix_text(text)
    print(f"Fixed text: {fixed_text}")
    # copy the fixed text to the clipboard
    pyperclip.copy(fixed_text)
    time.sleep(0.1)
    # insert the fixed text
    paste_fixed_text()

def fix_current_line():
    select_current_line()
    fix_selection()

def fix_all():
    # select all text
    subprocess.run(["xdotool", "key", "ctrl+a"])
    time.sleep(0.1)
    # process the selected text
    fix_selection()

def on_f9():
    fix_current_line()

def on_f11():
    fix_selection()

def on_f12():
    fix_all()

with keyboard.GlobalHotKeys({
        '<f9>': on_f9,
        '<f11>': on_f11,
        '<f12>': on_f12}) as h:
    h.join()


