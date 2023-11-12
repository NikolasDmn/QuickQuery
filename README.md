# QuickQuery

QuickQuery is a Python utility that enhances your productivity by allowing you to search the web or ask questions to AI models like ChatGPT instantly. With a simple keybind, it captures any highlighted text, opens a specified webpage, and submits the text as a search query or a question.

## Features

Instantly opens a predefined URL in a new browser tab.
Automatically copies highlighted text and pastes it into the web page.
Simulates an Enter key press to submit the text as a query.
Ideal for quick Google searches or querying AI models like ChatGPT.

## Installation

To set up QuickQuery, clone the repository and install necessary dependencies.

```bash
# Clone the repository
git clone [URL]
# Navigate to the project directory
cd QuickQuery

# Install dependencies
pip install -r requirements.txt
```

## Configuration

Create a configuration file from the provided example and customize it as needed:

```bash
cp config.example.conf config.conf
```

Edit `config.conf` to specify the URL where the query will be sent:

```bash
# config.conf
URL = https://www.google.com
```

Alternatively, set the URL to an AI model or any other search service that accepts input:

```bash
# config.conf
URL = https://chat.openai.com/?model=gpt-4
```

Usage
Run main.py to start listening for the keybind (`Ctrl + Alt + Space`). Highlight any text and press the keybind to trigger a search or query.

```bash
python3 main.py
```

Make sure the script is running in the background for the keybind to work.

# Future Improvements

Allow customization of the keybind through the configuration file.
Implement a GUI for easier configuration and real-time feedback.
