import difflib

class SimilarityChecker:
    def __init__(self):
        pass

    @staticmethod
    def check_similarity(answer, user_response):
        """
        Checks the similarity between the correct answer and the user's response.
        Uses the SequenceMatcher from the difflib module to calculate similarity.
        Returns a percentage representing the similarity.
        """
        similarity_ratio = difflib.SequenceMatcher(None, answer.lower(), user_response.lower()).ratio()
        return round(similarity_ratio * 100, 2)
