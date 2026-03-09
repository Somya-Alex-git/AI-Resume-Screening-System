# AI Resume Screening System

## Overview
The AI Resume Screening System is a Python-based application that evaluates how well
a candidate’s resume matches a given job description using Natural Language Processing (NLP).

It simulates the core logic of an Applicant Tracking System (ATS) by combining
text similarity analysis with skill-based matching.

---

## Features
- Resume and job description comparison
- NLP-based text vectorization using TF-IDF
- Cosine similarity for relevance scoring
- Skill-based weighting for improved accuracy
- Identification of matched and missing skills

---

## Technologies Used
- Python
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Cosine Similarity
- scikit-learn
- NumPy

---

## How It Works
1. Resume and job description text are loaded
2. Text is converted into numerical vectors using TF-IDF
3. Cosine similarity computes the base relevance score
4. A curated skill vocabulary is used to match key technical skills
5. A final match percentage is generated

---

## Project Structure

AI-Resume-Screening-System
│
├── app.py
├── README.md
├── requirements.txt
│
└── sample_data
     ├── resume.txt
     └── job_description.txt

## Example Output
     ====== AI RESUME SCREENING RESULT ======

Base Match Score     : 32.21%
Skill Match Boost    : +25.00%
Final Match Score    : 57.21%

Matched Skills:
data analysis, machine learning, natural language processing, python, scikit-learn

Missing Skills (to improve resume):
None

---

## How to Run the Project

1. Clone the repository

git clone https://github.com/Somya-Alex-git/AI-Resume-Screening-System.git

2. Navigate to the project folder

cd AI-Resume-Screening-System

3. Install required dependencies

pip install -r requirements.txt

4. Run the application

python app.py
