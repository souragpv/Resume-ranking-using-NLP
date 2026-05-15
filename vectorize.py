# tfidf_vectorizer.py

from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_documents(job_description, resumes):

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),  # Unigrams + Bigrams
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    job_vector = tfidf_matrix[0]
    resume_vectors = tfidf_matrix[1:]

    return job_vector, resume_vectors
