import streamlit as st
import pandas as pd

from extraction import extract_text
from preprocess import clean_text
from vectorize import vectorize_documents
from similarity import calculate_similarity
from skill_matching import extract_keywords, skill_match_score

st.title("📄 Resume Ranking System using TF-IDF")

jd_text = st.text_area("Paste Job Description Here")

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("Rank Candidates"):

    if not jd_text:
        st.warning("Please enter a job description.")
        st.stop()

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    with st.spinner("Processing resumes..."):

        cleaned_resumes = []
        filenames = []

        for file in uploaded_files:
            text = extract_text(file, file.name)
            cleaned = clean_text(text)

            cleaned_resumes.append(cleaned)
            filenames.append(file.name)

        cleaned_jd = clean_text(jd_text)

        st.write("Cleaned JD:", cleaned_jd[:200])
        st.write("First Resume Sample:", cleaned_resumes[0][:200])

        # TF-IDF Vectorization
        job_vector, resume_vectors = vectorize_documents(
            cleaned_jd,
            cleaned_resumes
        )

        # Cosine Similarity
        scores = calculate_similarity(job_vector, resume_vectors)

        jd_keywords = extract_keywords(cleaned_jd)

        final_results = []

        for i in range(len(filenames)):
            tfidf_score = scores[i]
            skill_score = skill_match_score(cleaned_resumes[i], jd_keywords)

            # Hybrid score
            final_score = (0.6 * tfidf_score) + (0.4 * skill_score)

            final_results.append((filenames[i], final_score))

            ranked = sorted(final_results, key=lambda x: x[1], reverse=True)

    st.success("Ranking Complete!")

    df = pd.DataFrame(ranked, columns=["Resume", "Similarity Score"])
    df.insert(0, "Rank", range(1, len(df) + 1))

    st.dataframe(df, use_container_width=True)
