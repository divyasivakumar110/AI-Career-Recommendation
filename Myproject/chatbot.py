from flask import Blueprint, request, jsonify

chatbot = Blueprint("chatbot", __name__)

def get_response(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to the AI Job Recommendation Platform."

    elif "python" in message:
        return "Python is one of the most valuable programming skills for AI, Data Science, and Web Development."

    elif "ai" in message:
        return "Artificial Intelligence enables computers to perform tasks that normally require human intelligence."

    elif "machine learning" in message:
        return "Machine Learning helps computers learn from data and make predictions."

    elif "skill" in message:
        return "Improve your programming, communication, problem-solving, SQL, Python, and teamwork skills."

    elif "certificate" in message:
        return "You can strengthen your profile with certifications in Python, AI, Data Science, Cloud Computing, or Web Development."

    elif "job" in message:
        return "Complete the recommendation form to discover career options that match your profile."

    elif "thank" in message:
        return "You're welcome! Best wishes for your career."

    else:
        return "Sorry, I didn't understand that. Please ask a career-related question."

@chatbot.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data["message"]

    reply = get_response(user_message)

    return jsonify({"reply": reply})