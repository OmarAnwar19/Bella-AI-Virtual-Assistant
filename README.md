# Chloe - AI Virtual Assistant

Chloe is an AI Virtual Assistant, which harnesses the power of AI and Machine Learning in order to help you with anything you need! Chloe is based on the GPT-3 Model by OpenAI, allowing it to make use of one of the most powerful AI models to respond to almost any query.

Chloe acts as an interface to transform OpenAI's Chat-GPT into a fully functional AI Virtual Assistant, using the whisper package to transcribe user speech into text, which is then interpreted by Chat-GPT, and returned, then displayed in both text, and audio formats using GTTS. The Gradio package is used as the front-facing interface for Chloe, allowing for a smooth, and, intuitive user experience.

![program screenshot](/assets/img/sc.png)

## Installation

After obtaining your Chat-GPT Session Token;

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all of the packages required for Chloe.

```bash
pip install .
touch /src/secret.py
#Create a new variable for the secret session token
SESSION_TOKEN = "your_session_token"
```

## Usage

From the root project directory.

```python
python src/main.py
#then navigate to http://127.0.0.1:7860/
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
