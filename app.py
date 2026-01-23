from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load resume and job description
with open("sample_data/resume.txt", "r", encoding="utf-8") as f:
    resume_text = f.read().lower()

with open("sample_data/job_description.txt", "r", encoding="utf-8") as f:
    job_text = f.read().lower()

# ---------------- TF-IDF Similarity ----------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)
vectors = vectorizer.fit_transform([resume_text, job_text])
base_similarity = cosine_similarity(vectors)[0][1]

# ---------------- Curated Skill Vocabulary ----------------
skill_vocabulary = [
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

resume_skills = {skill for skill in skill_vocabulary if skill in resume_text}
job_skills = {skill for skill in skill_vocabulary if skill in job_text}

matched_skills = resume_skills & job_skills
missing_skills = job_skills - resume_skills

# Skill-based boost (capped for realism)
skill_boost = min(len(matched_skills) * 0.05, 0.25)
final_score = min(base_similarity + skill_boost, 1.0)

# ---------------- Output ----------------
print("====== AI RESUME SCREENING RESULT ======\n")
print(f"Base Match Score     : {base_similarity * 100:.2f}%")
print(f"Skill Match Boost    : +{skill_boost * 100:.2f}%")
print(f"Final Match Score    : {final_score * 100:.2f}%\n")

print("Matched Skills:")
print(", ".join(sorted(matched_skills)) if matched_skills else "None")

print("\nMissing Skills (to improve resume):")
print(", ".join(sorted(missing_skills)) if missing_skills else "None")
