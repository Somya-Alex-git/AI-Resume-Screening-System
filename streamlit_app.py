import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening System")

st.write("Paste a resume and job description to calculate match score.")

resume_text = st.text_area("Resume Text")
job_text = st.text_area("Job Description")

if st.button("Calculate Match Score"):
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    score = round(similarity * 100, 2)

    st.success(f"Match Score: {score}%")
