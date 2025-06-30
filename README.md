# MoodBot - Smart Sentiment Chatbot

MoodBot is designed to serve as an online Sentiment Analysis chatbot, which could further assist in analyzing and visualizing user moods over time during emotional conversations. MoodBot has been provided with your everyday TextBlob sentiment analysis and material coding with Flask for web services. MoodBot also impersonates empathetic conversation while synthesizing a dynamic mood graph based on user's response.

## Features

- Chatbot responses will be sentiment-aware by TextBlob
- Records the conversation history with sentiment classification
- Emotional trendographs as mood will be displayed
- The interactive web interface will be made using HTML, CSS, Chart.js
- Flask back-end for session handling, as well as creating answers to the users

## Files Overview

- `app.py`: Flask backing Following routes, session management, and sentiment Analyzing
- `response_engine.py`: Analyses user input and gives appropriate answers
- `templates/index.html`: The front-end chat interface with sentiment visualization
- `static/style.css`: Contains all the styling rules for the UI layout and appearance

## Technologies Used

- Python 3
- Flask
- TextBlob
- HTML
- CSS
- JavaScript
- Chart.js

## How it Works

1. A message is submitted by the user via the interface.
2. The message enters a calculation to get the TextBlob sentiment polarity.
3. The sentiment is broken down into positive, neutral, or negative.
4. The chatbot will answer based on the sentiment and context.
5. The mood curve, provided by Chart.js, is updated in an ongoing manner.

## Running the Application

1. Install the required libraries
2. Run the Flask app
3. Open up your browser and navigate to http://localhost:5000

## Future Improvements

- Add user authentication
- Add a machine-learning algorithm for improved sentiment predictions
- Establish export of chat logs
- Deploy on cloud platform
