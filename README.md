# AI Resume Analyzer

An AI-powered resume analyzer that evaluates resumes for specific job roles using Generative AI.

## 📌 Project Overview

AI Resume Analyzer is a Generative AI application that helps users analyze their resumes according to a target job role.

The application accepts a resume in PDF, JPG, JPEG, or PNG format and uses AI to analyze the resume and provide useful feedback.

## 🎯 Problem Statement

Manual resume screening can take time and may make it difficult for students and job seekers to identify whether their resume matches a particular job role.

This project uses Generative AI to provide automated resume analysis and improvement suggestions.

## ✨ Features

- Upload resume in PDF, JPG, JPEG, or PNG format
- Supports image-based PDF resumes
- Target job role selection
- Resume summary
- Technical skill identification
- Soft skill identification
- Project and experience analysis
- Missing or weak skill identification
- Job role suitability analysis
- Resume improvement suggestions
- Simple Streamlit interface

## 🔄 Project Workflow

```text
Upload Resume
      ↓
Read Resume
      ↓
Convert PDF Pages to Images
      ↓
AI Vision Model
      ↓
Analyze Resume
      ↓
Compare With Target Job Role
      ↓
Generate Feedback
🛠️ Technologies Used
Python
Streamlit
Groq API
Generative AI
Qwen Vision Model
PyMuPDF
Base64
GitHub
🤖 AI Model

The application uses the Groq API with the Qwen vision model:

qwen/qwen3.8-27b

The model is used to understand resume content from uploaded documents/images and generate structured feedback.

📂 Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone https://github.com/Komal0055765/AI-Resume-Analyzer.git

Go to the project folder:

cd AI-Resume-Analyzer

Install the required packages:

pip install -r requirements.txt
🔑 API Key Setup

The application requires a Groq API key.

Run the application:

streamlit run app.py

Enter the Groq API key in the application when prompted.

Do not share or upload your API key to GitHub.

▶️ How to Run

Run the following command:

streamlit run app.py

Then open the Streamlit application in the browser.

Enter the Groq API key.
Upload your resume.
Enter the target job role.
Click Analyze Resume.
View the AI-generated resume analysis.
📊 Output

The application provides:

Resume Summary
Technical Skills
Soft Skills
Relevant Projects / Experience
Missing or Weak Skills
Job Role Suitability
Resume Improvement Suggestions
🚀 Future Scope

The project can be extended with:

RAG-based job description matching
Job description database
Career resource integration
Agentic resume improvement workflow
Resume scoring and comparison
Deployment as a public web application
👩‍💻 Author
Komal singh
(AI & Machine Learning Student)



