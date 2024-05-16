import json
import os

class AnalyticsTracker:
    def __init__(self, analytics_file='analytics/analytics_data.json'):
        self.analytics_file = analytics_file
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.exists(self.analytics_file):
            os.makedirs(os.path.dirname(self.analytics_file), exist_ok=True)
            with open(self.analytics_file, 'w') as file:
                json.dump([], file)

    def log_question(self, question_type, difficulty_level):
        with open(self.analytics_file, 'r+') as file:
            data = json.load(file)
            data.append({'question_type': question_type, 'difficulty_level': difficulty_level})
            file.seek(0)
            json.dump(data, file, indent=4)

    def assess_question_difficulty(self, question_content):
        # This is a placeholder for the actual implementation
        # The difficulty assessment criteria should be defined here
        # For now, it returns a dummy difficulty level
        return "medium"

    def store_assessed_difficulty(self, question_content, assessed_difficulty):
        with open(self.analytics_file, 'r+') as file:
            data = json.load(file)
            data.append({'question_content': question_content, 'assessed_difficulty': assessed_difficulty})
            file.seek(0)
            json.dump(data, file, indent=4)

    def summarize_data(self):
        with open(self.analytics_file, 'r') as file:
            data = json.load(file)
            summary = {}
            for entry in data:
                question_type = entry.get('question_type')
                difficulty_level = entry.get('difficulty_level', entry.get('assessed_difficulty'))
                if question_type not in summary:
                    summary[question_type] = {'count': 0, 'difficulty_levels': {}}
                summary[question_type]['count'] += 1
                if difficulty_level not in summary[question_type]['difficulty_levels']:
                    summary[question_type]['difficulty_levels'][difficulty_level] = 0
                summary[question_type]['difficulty_levels'][difficulty_level] += 1
            return summary
