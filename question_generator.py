import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from tkinter import Tk, Label, Entry, Button, filedialog
import PyPDF2
import docx

# Load environment variables
load_dotenv()

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def load_files(data_paths, format_path):
    # Concatenate content of all data files
    cheat_sheet = ""
    for data_path in data_paths:
        if data_path.endswith('.txt'):
            with open(data_path, 'r', encoding='utf-8') as f:
                cheat_sheet += f.read() + "\n"
        elif data_path.endswith('.pdf'):
            with open(data_path, 'rb') as f:
                reader = PyPDF2.PdfFileReader(f)
                for page in range(reader.numPages):
                    cheat_sheet += reader.getPage(page).extractText() + "\n"
        elif data_path.endswith('.docx'):
            doc = docx.Document(data_path)
            for para in doc.paragraphs:
                cheat_sheet += para.text + "\n"
    
    with open(format_path, 'r', encoding='utf-8') as f:
        example_questions = json.load(f)
    return cheat_sheet, example_questions

def generate_questions(cheat_sheet, example_questions, num_questions=10):
    example_text = json.dumps(example_questions, indent=2)
    prompt_text = f"Generate {num_questions} questions and answers based on the following cheat sheet and in the format shown in these examples, do not copy questions but only formatting:\n\nExamples:\n{example_text}\n\nCheat Sheet:\n{cheat_sheet}"
    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt_text
            }
        ],
        model="gpt-4o",
    )
    generated_text = response.choices[0].message.content
    return json.loads(generated_text)

def save_questions(questions, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2)

def gui():
    root = Tk()
    root.title("OOSE AI Question Generator")

    Label(root, text="Number of Questions:").grid(row=0, column=0)
    num_questions_entry = Entry(root)
    num_questions_entry.grid(row=0, column=1)

    def generate():
        num_questions = int(num_questions_entry.get())
        data_dir = 'data'
        format_dir = 'format'
        output_dir = 'generated_questions'
        
        os.makedirs(output_dir, exist_ok=True)
        
        data_files = list_files(data_dir)
        format_files = list_files(format_dir)

        data_paths = [os.path.join(data_dir, data_file) for data_file in data_files]

        for format_file in format_files:
            format_path = os.path.join(format_dir, format_file)
            
            cheat_sheet, example_questions = load_files(data_paths, format_path)
            new_questions = generate_questions(cheat_sheet, example_questions, num_questions)
            
            output_file_name = f"questions_{os.path.splitext(format_file)[0]}.json"
            output_path = os.path.join(output_dir, output_file_name)
            
            save_questions(new_questions, output_path)
            print(f"Generated questions saved to {output_path}")

    Button(root, text="Generate", command=generate).grid(row=1, columnspan=2)

    root.mainloop()

def main():
    gui()

if __name__ == "__main__":
    main()
