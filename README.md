# QUIZLESS
Flashcards made easy!

## Running Quizless
1. Install pygame and pygame_widgets
2. Run the main.py script in GUIStuff with Quizless as your working directory

## Choosing a quiz
1. Open the dropdown menu and scroll through the list of quizes.
2. Select a quiz by clicking on it.
3. Click Begin to Enter the Quiz Screen.

## Quizing
Once a quiz is selected, you will enter the quiz screen. A random card will be selected from the quiz. Flip between the question and answer using /italic{space} (or f) or by clicking the flip button. Click correct or press /italic{Right Arrow} (or c) if you got the question right, your score will increase by one and that question will not come up again. Click incorrect or press /italic{Left Arrow} (or i) if you got it wrong and the question will come up again later for you to try again. 

When you have completed all the questions correctly, you will be returned to the home page.

Press "q" to quit quizless.

## Creating a Quiz
\*\* Currently the quiz folders are a bit funky. This will be resolved soon with a nested folder selection in the dropdown. The quizes are taken from the "sll" folder. Add your quiz there and it will come up in the dropdown. \*\*

Quizzes are read from text files and the text files are located in the File Handling folder. 

The Quizzes do support Images and Diagrams. Add '!' infront of the relative path to the Picture in the text file.

### Quiz Format
The standard format for all quizes are as follows:

\#\
\<Question\>\
\<Answer\>\
\#

### Special characters
"|" - this will add a new line in the flash card
"~" - this creates a bullet by replacing it with "\n• " when printing to the flash card

### File Errors
\*\* more file error handling is planned to be built in the near future to make creators aware of where the errors are in thier files. use the current quizes as refernce for now \*\*

1. Dont leave any extra empty lines at the end of the file [this may be fixed soon]
2. Make sure that all questions have a corresponding answer below it.
3. Only use one "#" between questions and answers.
4. Questions and answers must only be on one line each. New lines can be added with "|"

## Why Quizless
The creators were tired of using online flash cards that require you to enter each question and answer individually which takes more time than the flashcards are worth. By storing the quizes as a text file with a standard format, notes/documents can be copied and pasted into a text file and with some formating you can have a 200 question quiz in no time! Saving quizes as text files also allows you to take school documents and format them into a quizless quiz by using basic string handling in a python script.

##Suggestions or Ideas? Want to Contribute?
Please email stocks.net-0n@icloud.com

