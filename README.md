# Bella - AI Virtual Assistant

Bella is an AI Virtual Assistant, which harnesses the power of AI and Machine Learning in order to help you with anything you need! Bella is based on the GPT-3 Model by OpenAI, allowing it to make use of one of the most powerful AI models to respond to almost any query.

Bella acts as an interface to transform OpenAI's Chat-GPT into a fully functional AI Virtual Assistant, using the whisper package to transcribe user speech into text, which is then interpreted by Chat-GPT, and returned, then displayed in both text, and audio formats using GTTS. The Gradio package is used as the front-facing interface for Bella, allowing for a smooth, and, intuitive user experience.

![program screenshot](/assets/img/sc.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all of the packages required for Bella, by navigating to the project root folder, and using one command:

```bash
pip install .
```

## Usage

From the root project directory.

```python
python src/main.py
#then navigate to http://127.0.0.1:7860/
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
