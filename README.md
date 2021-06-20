# 2. Word Count Challenge

# Full Stack Word Count App

[Please use this hyperlink to interact with the project.](https://nadiarichards.github.io/word-count-challenge/)

## Background
---
This project's main purpose was to make a full stack app that utilizes multiple tools including Python, JavaScript and HTML, CSS. 

Premise: The word count app can be a writer's best friend. One can quickly upload their file to get a number of useful metrics. 

I have written code in Python first, please see my ["py" folder](https://github.com/nadiarichards/word-count-challenge/tree/main/py). In Python I have prmarily used RegEx and NLTK Tokenizer. Python code includes the following: 

* Classic Word Count
* Unique Word Count (currently set to show words repeated over 5 times to minimize the output)
* Classic Character Count
* Unique Character Count (count per each letter of the alphabet in the alpabetical order)
* Sentence Count
* Paragraph Count
* Bigram Count (currently set to show bigrams repeated over 2 time sto minimize the output)
* Word Ocurrence Count (takes text file and word to count occcurrences for as an input)

I have later used JavaScript to rewrite function to be easier used by front end without involving running Pythn script through a Flask app. Please see my [js folder here.](https://github.com/nadiarichards/word-count-challenge/tree/main/js)
JavaScript front end app includes the following functions: 

* Classic Word Count
* Classic Character Count
* Character Count Including spaces
* Sentence Count
* Paragraph Count

## Tools and Technology Used for the Project
---
* Visual Studio Code
* Python
* Regex
* Tokenizer (nltk library)
* Javascript
* CSS
* HTML


## Process Flow
---
1. Create each function and test it on the sample txt file
2. Pull data into browser using JavaScript
3. Generate front end using JavaScript
4. HTML and CSS formatting / organization


## Summary
---
This is a simple app and definitely could useimprovement on styling, can also take paragraph counts in to account a bit different (not by extra space between text like it does now). It also can be reworked to understand that a "." can be an abbreviation vs always the end of sentence. 
