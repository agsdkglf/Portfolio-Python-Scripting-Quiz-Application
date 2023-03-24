# Project Name
The quiz application tests a person's knowledge of some English expressions.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
* [License](#license)


## General Information
It offers its users a set of multiple choice questions and an immediate feedback whether their answer is correct or not. After answering all the questions the final summary is presented, informing the player how many of their answers were correct, out of ten possible.


## Technologies Used
JSON is used to exchange the data in the application.
random module is used to generate questions in random order.
ascii_lowercase is used to label the answer alternatives.


## Setup
Download the code from this GitHub repository, the "art.py" and the "q_questions.txt" files. Make sure that you have Python 3.6 or newer installed. When running the code, you get the following error:

    with open('q_questions.txt', 'r') as file:

    FileNotFoundError: [Errno 2] No such file or directory: 'q_questions.txt'

you should use an absolute path instead of a relative one, in the line:

    with open('q_questions.txt', 'r') as file:


## Usage
After fulfilling the instructions described in "Setup" you are ready to use the code.


## Project Status
The project's status is _complete_.


## Room for Improvement
Room for improvement:
- Adding GUI
- Adding different topics
- Adding different questions
- Setting a mulitiplayer mode
- Storing the questions in a database


## Acknowledgements
This project was based on "Build a Quiz Application With Python" (https://realpython.com/python-quiz-application/).
I also used some tips from "100 Days of Code" course (https://www.udemy.com/course/100-days-of-code/). Many thanks to Dr. Angela Yu.


## Contact
Created by Adam Hoppe (adhoppe@poczta.fm) - feel free to contact me!


## License
This project is open source and available under the MIT License.
