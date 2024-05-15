import json
import os
from openai import OpenAI
from dotenv import load_dotenv

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
        with open(data_path, 'r', encoding='utf-8') as f:
            cheat_sheet += f.read() + "\n"
    
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

def main():
    data_dir = 'data'
    format_dir = 'format'
    output_dir = 'generated_questions'
    
    os.makedirs(output_dir, exist_ok=True)
    
    data_files = list_files(data_dir)
    format_files = list_files(format_dir)

    data_paths = [os.path.join(data_dir, data_file) for data_file in data_files]

    num_questions = int(input("How many questions do you want to generate? "))

    for format_file in format_files:
        format_path = os.path.join(format_dir, format_file)
        
        cheat_sheet, example_questions = load_files(data_paths, format_path)
        new_questions = generate_questions(cheat_sheet, example_questions, num_questions)
        
        output_file_name = f"questions_{os.path.splitext(format_file)[0]}.json"
        output_path = os.path.join(output_dir, output_file_name)
        
        save_questions(new_questions, output_path)
        print(f"Generated questions saved to {output_path}")

if __name__ == "__main__":
    main()
