# OOSE-AI-Question-Generator

## Overview

OOSE-AI-Question-Generator is a Python-based tool that leverages OpenAI's new GPT-4o model to generate questions and answers based on a given cheat sheet. This tool is particularly useful for creating study materials or quizzes, in this case used for the Object-Oriented Software Engineering (OOSE) course.

## Features

- Loads example questions and a combined cheat sheet from all specified data files.
- Automatically processes all files in the `data` and `format` directories.
- Prompts the user for the number of questions to generate.
- Generates new questions and answers based on the combined cheat sheet.
- Saves the generated questions to output files named based on the format files.

## Prerequisites

- Python 3.6 or higher
- An OpenAI API key

## Installation

1. Clone the repository:
```
git clone https://github.com/turiddu25/OOSE-AI-Question-Generator.git
```
2. Install the required Python packages:
```
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
- Create an account on the [OpenAI website](https://platform.openai.com/signup).
- Create an API key in the OpenAI dashboard.
- Add your API key to the `.env` file:
  ```
  OPENAI_API_KEY=YOURKEYHERE
  ```

## Usage

1. Place your data files in the `data` directory. These files should contain the content you want to generate questions about.
2. Place your format files in the `format` directory. These files should contain example questions that you want to use as a reference.
3. Run the script:
```
python generate_questions.py
```
4. Enter the number of questions you want to generate when prompted.
5. The script will generate questions based on the combined data from all files in the `data` directory and save the generated questions in the `generated_questions` directory. The output files will be named based on the format files.


## Example

If you have the following files:
- `data/cheat_sheet1.txt`
- `data/cheat_sheet2.txt`
- `format/example_format1.json`
- `format/example_format2.json`

Running the script and entering `10` when prompted will generate 10 questions and save them in `generated_questions/questions_example_format1.json` and `generated_questions/questions_example_format2.json`.

## License

This project is licensed under the MIT License.



