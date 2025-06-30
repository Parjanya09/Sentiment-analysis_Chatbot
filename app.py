from flask import Flask, render_template, request, session
from textblob import TextBlob
from response_engine import get_therapist_response

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if 'chat_history' not in session:
        session['chat_history'] = []
    if 'mood_history' not in session:
        session['mood_history'] = []

    user_text = ""
    sentiment = ""
    response = ""

    if request.method == 'POST':
        user_text = request.form['message']
        blob = TextBlob(user_text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "positive"
        elif polarity < 0:
            sentiment = "negative"
        else:
            sentiment = "neutral"

        session['mood_history'].append(sentiment)
        response = get_therapist_response(user_text, sentiment, session['mood_history'])

        session['chat_history'].append({
            "user": user_text,
            "bot": response,
            "sentiment": sentiment.capitalize()
        })

    mood_map = {'positive': 1, 'neutral': 0, 'negative': -1}
    mood_values = [mood_map[m] for m in session['mood_history']]
    mood_labels = list(range(1, len(mood_values) + 1))

    return render_template(
        'index.html',
        chat_history=session['chat_history'],
        mood_values=mood_values,
        mood_labels=mood_labels
    )

@app.route('/reset')
def reset():
    session.pop('chat_history', None)
    session.pop('mood_history', None)
    return "Chat reset! <a href='/'>Start over</a>"

if __name__ == '__main__':
    app.run(debug=True)
