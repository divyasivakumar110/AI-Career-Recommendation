import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import pickle

# Load dataset
df = pd.read_csv("c:\\Users\\Divya S\\Downloads\\career_recommender.csv")

# Fill missing values
df.fillna("", inplace=True)

# Create a combined feature
df["combined"] = (
    df["What was your course in UG?"] + " " +
    df["What is your UG specialization? Major Subject (Eg; Mathematics)"] + " " +
    df["What are your interests?"] + " " +
    df["What are your skills ? (Select multiple if necessary)"] + " " +
    df["If yes, please specify your certificate course title."]
)

# Convert text into vectors
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["combined"])

# Train model
model = NearestNeighbors(n_neighbors=3, metric="cosine")
model.fit(X)

# Save model
pickle.dump(model, open("career_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(df, open("career_data.pkl", "wb"))

print("Model trained successfully!")