from flask import Flask, render_template, request
from chatbot import chatbot
import pickle

# Create Flask App
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Register chatbot
app.register_blueprint(chatbot)

# Load model and data
model = pickle.load(open("career_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
df = pickle.load(open("career_data.pkl", "rb"))

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Recommendation Page
@app.route("/recommend", methods=["POST"])
def recommend():

    course = request.form["course"]
    specialization = request.form["specialization"]
    interests = request.form["interests"]
    skills = request.form["skills"]
    certificate = request.form["certificate"]

    user_input = (
        course + " " +
        specialization + " " +
        interests + " " +
        skills + " " +
        certificate
    )

    vector = vectorizer.transform([user_input])

    distances, indices = model.kneighbors(vector)

    jobs = []

    for i in indices[0]:
        jobs.append({
            "course": df.iloc[i]["What was your course in UG?"],
            "specialization": df.iloc[i]["What is your UG specialization? Major Subject (Eg; Mathematics)"],
            "interest": df.iloc[i]["What are your interests?"],
            "skills": df.iloc[i]["What are your skills ? (Select multiple if necessary)"],
            "certificate": df.iloc[i]["If yes, please specify your certificate course title."]
        })

    return render_template("result.html", jobs=jobs)
    print(jobs)

# Run Application
if __name__ == "__main__":
    app.run(debug=True)