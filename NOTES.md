# Prompt and Chain Explanation
- The system prompt tells the assistant to answer clearly in simple language, in under 150 words, and to admit when it is unsure instead of guessing.
- A history placeholder inserts the last 5 exchanges, so follow-up questions such as "give me an example of that" work.
- The chain is: prompt template -> Gemini model -> text output parser, written as `prompt | llm | StrOutputParser()`.

# Errors, Risks and Limitations
- The model can give wrong answers that sound confident.
- It only remembers the last 5 exchanges, and the history is lost when the script closes.
- The free tier has rate limits, so many fast questions can cause errors. These are caught and shown as a friendly message.
- It fails without internet access or with an invalid API key or model name.
- Model names change over time, so `MODEL_NAME` in app.py may need updating.
- It has no knowledge of recent events beyond the model's training.
- The API key must never be shared or uploaded to GitHub, so it is stored in `.env`, which is excluded by `.gitignore`.