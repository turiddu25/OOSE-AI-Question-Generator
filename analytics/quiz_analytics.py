import json
import os

class QuizAnalytics:
    def __init__(self, analytics_file='analytics/quiz_analytics_data.json'):
        self.analytics_file = analytics_file
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.analytics_file):
            os.makedirs(os.path.dirname(self.analytics_file), exist_ok=True)
            with open(self.analytics_file, 'w') as file:
                json.dump([], file)

    def log_quiz_attempt(self, question_difficulty, question_correct):
        with open(self.analytics_file, 'r+') as file:
            data = json.load(file)
            data.append({'question_difficulty': question_difficulty, 'question_correct': question_correct})
            file.seek(0)
            json.dump(data, file, indent=4)

    def summarize_attempts(self):
        with open(self.analytics_file, 'r') as file:
            data = json.load(file)
            summary = {'total_attempts': len(data), 'correct_attempts': 0, 'difficulty_summary': {}}
            for entry in data:
                if entry['question_correct']:
                    summary['correct_attempts'] += 1
                difficulty = entry['question_difficulty']
                if difficulty not in summary['difficulty_summary']:
                    summary['difficulty_summary'][difficulty] = {'attempts': 0, 'correct': 0}
                summary['difficulty_summary'][difficulty]['attempts'] += 1
                if entry['question_correct']:
                    summary['difficulty_summary'][difficulty]['correct'] += 1
            return summary
