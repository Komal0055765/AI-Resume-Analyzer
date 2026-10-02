import streamlit as st
import base64
import fitz
from groq import Groq

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-powered feedback for your target job role.")

# API KEY
api_key = st.text_input(
    "Groq API Key",
    type="password"
)

# Resume
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "jpg", "jpeg", "png"]
)

# Job role
job_role = st.text_input(
    "Target Job Role",
    placeholder="Example: Data Analyst"
)


def pdf_to_images(pdf_bytes):
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    images = []

    for page_number in range(min(len(pdf), 3)):
        page = pdf[page_number]

        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2),
            alpha=False
        )

        images.append(pix.tobytes("png"))

    pdf.close()

    return images


def image_to_base64(image_bytes):
    return base64.b64encode(image_bytes).decode("utf-8")


if st.button("🔍 Analyze Resume"):

    if not api_key:
        st.warning("Please enter your Groq API key.")

    elif not uploaded_file:
        st.warning("Please upload your resume.")

    elif not job_role:
        st.warning("Please enter the target job role.")

    else:

        try:

            client = Groq(api_key=api_key)

            file_bytes = uploaded_file.read()

            # PDF → Images
            if uploaded_file.name.lower().endswith(".pdf"):

                st.info("📄 Reading PDF...")

                images = pdf_to_images(file_bytes)

            # JPG/PNG
            else:

                st.info("🖼️ Reading image...")

                images = [file_bytes]

            if not images:
                st.error("Could not read the uploaded file.")
                st.stop()

            # Create image messages
            content = [
                {
                    "type": "text",
                    "text": f"""
You are an AI Resume Analyzer.

Analyze this resume for the following target job role:

{job_role}

Read the resume carefully.

Give the answer in this exact structure:

## 1. Resume Summary

Give a short summary of the candidate.

## 2. Technical Skills

List the technical skills visible in the resume.

## 3. Soft Skills

List the soft skills visible in the resume.

## 4. Projects / Experience

Mention relevant projects, internships, education and experience.

## 5. Missing or Weak Skills

Mention important skills for {job_role} that are missing or weak.

## 6. Job Role Suitability

Give an approximate suitability percentage and explain why.

## 7. Resume Improvement Suggestions

Give practical suggestions to improve this resume for {job_role}.

IMPORTANT:
- Only use information visible in the resume.
- Do not invent information.
- Keep the answer simple and student-friendly.
"""
                }
            ]

            # Add resume pages
            for image_bytes in images:

                encoded = image_to_base64(image_bytes)

                content.append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{encoded}"
                        }
                    }
                )

            st.info("🤖 AI is analyzing your resume...")

            response = client.chat.completions.create(
                model="qwen/qwen3.8-27b",
                messages=[
                    {
                        "role": "user",
                        "content": content
                    }
                ],
                temperature=0.2,
                max_completion_tokens=2500
            )

            result = response.choices[0].message.content

            st.success("✅ Resume analyzed successfully!")

            st.markdown("## 📊 Resume Analysis")
            st.markdown(result)

        except Exception as e:

            st.error("❌ Error occurred")

            st.code(str(e))