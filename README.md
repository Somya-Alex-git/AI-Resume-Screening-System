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
