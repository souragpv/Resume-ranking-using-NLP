def extract_keywords(text):
    words = text.split()
    keywords = set(words)
    return keywords


def skill_match_score(resume_text, jd_keywords):
    resume_words = set(resume_text.split())
    matched = resume_words.intersection(jd_keywords)

    if len(jd_keywords) == 0:
        return 0

    return len(matched) / len(jd_keywords)