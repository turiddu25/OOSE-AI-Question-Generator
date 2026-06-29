import tkinter as tk
from quiz_manager import QuizManager
from similarity_checker import SimilarityChecker

class QuizUI:
    def __init__(self, master, quiz_manager: QuizManager):
        self.master = master
        self.quiz_manager = quiz_manager
        self.similarity_checker = SimilarityChecker()
        self.setup_ui()

    def setup_ui(self):
        self.master.title("OOSE Quiz Application")
        self.question_label = tk.Label(self.master, text="Press 'Next' for the first question")
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.check_button = tk.Button(self.master, text="Check Answer", command=self.check_answer)
        self.check_button.pack()

        self.next_button = tk.Button(self.master, text="Next Question", command=self.next_question)
        self.next_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

    def next_question(self):
        self.quiz_manager.select_question('medium')  # Placeholder for dynamic difficulty selection
        if self.quiz_manager.current_question:
            self.question_label.config(text=self.quiz_manager.current_question['content'])
            self.answer_entry.delete(0, tk.END)
            self.result_label.config(text="")

    def check_answer(self):
        user_answer = self.answer_entry.get()
        correct_answer = self.quiz_manager.current_question['answer']
        similarity = self.similarity_checker.check_similarity(correct_answer, user_answer)
        if similarity > 80:  # Assuming 80% similarity as correct
            self.result_label.config(text=f"Correct! Similarity: {similarity}%")
            self.quiz_manager.score += 1
        else:
            self.result_label.config(text=f"Incorrect! Similarity: {similarity}%")

def main():
    root = tk.Tk()
    quiz_manager = QuizManager(question_bank=[])  # Placeholder for actual question bank initialization
    app = QuizUI(root, quiz_manager)
    root.mainloop()

if __name__ == "__main__":
    main()
