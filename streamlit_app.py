import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("AI Resume Screening System")

st.write("Upload your resume and paste a job description to check the match score.")

# Upload resume file
uploaded_file = st.file_uploader("Upload Resume (TXT)", type=["txt"])

# Job description input
job_description = st.text_area("Paste Job Description")

if st.button("Calculate Match Score"):
    if uploaded_file is not None and job_description != "":
        resume_text = uploaded_file.read().decode("utf-8")

        documents = [resume_text, job_description]

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
        score = round(similarity * 100, 2)

        st.success(f"Match Score: {score}%")

    else:
        st.warning("Please upload a resume and enter a job description.")
