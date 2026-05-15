def rank_candidates(filenames, scores):
    ranked = sorted(
        zip(filenames, scores),
        key=lambda x: x[1],
        reverse=True
    )
    return ranked
