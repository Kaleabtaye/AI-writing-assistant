# AI Writing Assistant

An AI-powered writing assistant for Ubuntu that helps users correct grammar and spelling in selected text or the entire document using a hotkey.

## Features

- Grammar and spelling correction for selected text or the whole text
- Hotkey support for quick corrections

## Requirements

- Ubuntu environment
- `xdotool` installed for simulating copy-paste actions

## Installation

```bash
git clone https://github.com/Kaleabtaye/AI-writing-assistant.git
cd AI-writing-assistant
pip install -r requirements.txt
sudo apt-get install xdotool
```

## Usage

1. Run the assistant:
    ```bash
    python main.py
    ```
2. Use the configured hotkey to correct grammar and spelling in your selected text or the entire document.
