import random

greeting_keywords = ["hi", "hello", "hey", "good morning", "good evening"]
intro_questions = ["how are you", "how are you doing", "what's up", "how’s it going"]

def is_greeting(text):
    return any(greet in text for greet in greeting_keywords)

def is_intro_question(text):
    return any(q in text for q in intro_questions)

def get_therapist_response(user_input, sentiment, mood_history):
    user_input = user_input.lower()

    if is_greeting(user_input):
        return "Hello! 😊 I'm here to listen. How are you feeling today?"

    if is_intro_question(user_input):
        return "I'm just a bunch of code, but I'm happy to talk to you. How have *you* been feeling?"

    mood_summary = summarize_mood(mood_history)

    if sentiment == "positive":
        return random.choice([
            f"That's wonderful to hear. The entirety of your day appears to be filled with brightness.",
            "Glad you’re feeling great! What else has been going well?",
            f"You've been sounding pretty upbeat. What’s helping you feel positive today?"
        ])

    elif sentiment == "negative":
        return random.choice([
            f"I'm sorry you're feeling this way. I'm noticing some heavy moments today.",
            f"It seems you've been feeling low. Want to talk more about what's been bothering you?",
            "That sounds tough. I'm here to listen if you want to talk about it.",
            f"The state of your well-being brings me joy! What else has been going well?"
        ])

    else:
        return random.choice([
            "Hmm, feels fine. Anything bothering you under the surface?",
            "I see. Feel free to open up and talk a little more when you're ready.",
            f"Oh!! It looks like you’ve had a mix of feelings today. Do you want to reflect more deeply on any one?"
        ])

def summarize_mood(mood_list):
    from collections import Counter
    if not mood_list:
        return "neutral"
    count = Counter(mood_list)
    return count.most_common(1)[0][0]
