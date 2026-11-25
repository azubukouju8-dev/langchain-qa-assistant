# LangChain Q&A Assistant

A command-line Q&A assistant built with LangChain and Google Gemini. It uses a prompt template, keeps a short conversation history, and handles empty questions and API errors.

Note: this project uses Gemini's free tier. The same chain works with OpenAI by swapping the model class and API key.

## Setup
1. Clone this repo and open the folder.
2. Create a virtual environment: `python -m venv venv`
3. Activate it (Windows): `venv\Scripts\activate`
4. Install packages: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and put your Gemini API key in it (get one at aistudio.google.com/apikey).

## Run
`python app.py`

Type a question and press Enter. Type `quit` to exit.

## Features
- Prompt template with a clear system instruction
- Short conversation history (last 5 exchanges)
- Handles empty questions and API errors
- API key stored in an environment variable, never in the code

## Files
- `app.py` - the assistant
- `requirements.txt` - dependencies
- `.env.example` - example of the key file (no real key)
- `NOTES.md` - prompt/chain explanation, errors, risks and limitations
- `test_results.md` - five test questions and answers

Author: Azubuko Uju | azubukouju8@gmail.com
