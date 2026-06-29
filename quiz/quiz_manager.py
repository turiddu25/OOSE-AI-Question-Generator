class QuizManager:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.current_question = None
        self.score = 0

    def select_question(self, difficulty):
        """
        Selects a question from the question bank based on the specified difficulty.
        """
        filtered_questions = [q for q in self.question_bank if q['difficulty'] == difficulty]
        if filtered_questions:
            self.current_question = random.choice(filtered_questions)
        else:
            self.current_question = None

    def assess_difficulty(self, question_content):
        """
        Assess the difficulty of a question based on predefined criteria.
        """
        # Placeholder for difficulty assessment logic
        return "medium"

    def store_assessed_difficulty(self, question_content, assessed_difficulty):
        """
        Stores the assessed difficulty of a question.
        """
        # Placeholder for storing logic
        pass

    def present_question(self):
        """
        Presents the current question to the user.
        """
        if self.current_question:
            print(f"Question: {self.current_question['content']}")
        else:
            print("No question selected.")

    def check_answer(self, user_answer):
        """
        Checks the user's answer against the correct answer.
        """
        if self.current_question and user_answer.lower() == self.current_question['answer'].lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")

    def display_score(self):
        """
        Displays the current score.
        """
        print(f"Your score is: {self.score}")
