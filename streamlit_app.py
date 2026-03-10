import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="AI Resume Screening System", layout="wide")

# Styling
st.markdown("""
<style>
.stApp {
    background-color: #f5f7fb;
}

h1 {
    text-align:center;
    color:#1f77b4;
}

.stButton button {
    background-color:#1f77b4;
    color:white;
    border-radius:8px;
}

.result-box {
    padding:20px;
    border-radius:10px;
    background-color:#ffffff;
}
</style>
""", unsafe_allow_html=True)

# Skill list
skills = [
    "python",
    "machine learning",
    "data analysis",
    "natural language processing",
    "nlp",
    "scikit-learn",
    "numpy",
    "sql",
    "deep learning"
]

# Session login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Login page
def login():

    st.title("🔐 AI Resume Screening Login")

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid username or password")


# Main application
def app():

st.title("🤖 AI Resume Screening System")

st.image("banner.png", use_column_width=True)

st.write("Upload your resume and compare it with a job description to calculate match score.")

    # Optional image placeholder
    # st.image("assets/banner.png", use_column_width=True)

    col1, col2 = st.columns(2)

    with col1:
        uploaded_file = st.file_uploader("Upload Resume (TXT)", type=["txt"])

    with col2:
        job_description = st.text_area("Paste Job Description")

    if st.button("🚀 Calculate Match Score"):

        if uploaded_file is not None and job_description != "":

            resume_text = uploaded_file.read().decode("utf-8")

            documents = [resume_text, job_description]

            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform(documents)

            similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
            score = round(similarity * 100, 2)

            st.subheader(f"🎯 Match Score: {score}%")

            resume_lower = resume_text.lower()
            job_lower = job_description.lower()

            matched_skills = []
            missing_skills = []

            for skill in skills:

                if skill in resume_lower and skill in job_lower:
                    matched_skills.append(skill)

                elif skill in job_lower and skill not in resume_lower:
                    missing_skills.append(skill)

            col3, col4 = st.columns(2)

            with col3:
                st.subheader("✅ Matched Skills")

                if matched_skills:
                    for skill in matched_skills:
                        st.write("✔", skill)
                else:
                    st.write("No matched skills")

            with col4:
                st.subheader("❌ Missing Skills")

                if missing_skills:
                    for skill in missing_skills:
                        st.write("✖", skill)
                else:
                    st.write("No missing skills")

            # Chart visualization
            labels = ["Matched Skills", "Missing Skills"]
            values = [len(matched_skills), len(missing_skills)]

            fig, ax = plt.subplots()
            ax.pie(values, labels=labels, autopct="%1.1f%%")
            ax.set_title("Skill Match Distribution")

            st.pyplot(fig)

        else:
            st.warning("Please upload resume and paste job description")


# Run app
if st.session_state.logged_in:
    app()
else:
    login()
