from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_jobs(resume_text, job_descriptions):
    corpus = [resume_text] + job_descriptions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])
    return similarities[0]

resume_text = "Experienced in Python, ML, and Cloud"
job_descriptions = ["Looking for Python developer", "ML engineer role with cloud experience"]
print(match_jobs(resume_text, job_descriptions))