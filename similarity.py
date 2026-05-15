# similarity.py

from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_vector, resume_vectors):

    scores = cosine_similarity(job_vector, resume_vectors)

    return scores.flatten()
