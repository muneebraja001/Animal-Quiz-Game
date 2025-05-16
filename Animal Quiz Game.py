import tkinter as tk
from tkinter import messagebox

class AnimalQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Quiz Game")
        self.root.geometry("500x400")

        self.question_index = 0
        self.score = 0

        self.questions = [
            {
                "question": "Which animal is known as the king of the jungle?",
                "options": ["Elephant", "Tiger", "Lion", "Giraffe"],
                "answer": "Lion"
            },
            {
                "question": "Which animal is the largest mammal?",
                "options": ["Blue Whale", "Elephant", "Hippopotamus", "Shark"],
                "answer": "Blue Whale"
            },
            {
                "question": "Which bird is a symbol of peace?",
                "options": ["Crow", "Sparrow", "Dove", "Owl"],
                "answer": "Dove"
            },
            {
                "question": "What do pandas primarily eat?",
                "options": ["Bamboo", "Meat", "Fish", "Grass"],
                "answer": "Bamboo"
            },
            {
                "question": "Which animal is the fastest land animal?",
                "options": ["Lion", "Horse", "Cheetah", "Leopard"],
                "answer": "Cheetah"
            }
        ]

        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=450, justify="center")
        self.question_label.pack(pady=20)

        self.option_vars = []
        self.radio_buttons = []
        for i in range(4):
            var = tk.StringVar(value="")
            rb = tk.Radiobutton(self.root, text="", variable=var, value="", font=("Arial", 12), anchor="w", width=30, justify="left")
            rb.pack(anchor="w", padx=70, pady=5)
            self.option_vars.append(var)
            self.radio_buttons.append(rb)

        self.submit_btn = tk.Button(self.root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_btn.pack(pady=20)

    def load_question(self):
        if self.question_index < len(self.questions):
            q = self.questions[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}: {q['question']}")

            for i, opt in enumerate(q['options']):
                self.radio_buttons[i].config(text=opt, value=opt, variable=self.option_vars[0])
                self.option_vars[0].set("")  # Reset selection
        else:
            self.show_result()

    def check_answer(self):
        selected = self.option_vars[0].get()
        if selected == "":
            messagebox.showwarning("No Selection", "Please select an answer.")
            return

        correct_answer = self.questions[self.question_index]['answer']
        if selected == correct_answer:
            self.score += 1

        self.question_index += 1
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz Finished", f"Your score is {self.score} out of {len(self.questions)}.")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    quiz = AnimalQuiz(root)
    root.mainloop()
