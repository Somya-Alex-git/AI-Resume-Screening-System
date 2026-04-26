import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Resume Screening System", layout="wide")

page = st.sidebar.selectbox("Navigation", ["Home", "Resume Analyzer"])

if page == "Home":
    st.title("🤖 AI Resume Screening System")

    try:
        st.image("banner.png", use_column_width=True)
    except:
        pass

    st.write("Upload your resume and compare it with a job description.")

elif page == "Resume Analyzer":
    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader("Upload Resume", type=["txt"])
    job_description = st.text_area("Paste Job Description")

    if st.button("Calculate Match Score"):

        if uploaded_file and job_description:

            resume = uploaded_file.read().decode("utf-8")

            docs = [resume, job_description]

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform(docs)

            score = cosine_similarity(vectors[0], vectors[1])[0][0]
            score = round(score * 100, 2)

            st.success(f"Match Score: {score}%")

        else:
            st.warning("Upload resume and enter job description")
