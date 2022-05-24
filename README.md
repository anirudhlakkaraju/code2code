# Code2Code Translator

Code2Code Translator is a web interface built to showcase the working of Natural Language Processing (NLP) models that translate between Programming Languages (PL). 

## What does this website do?

This website is an interface that enables users to provide source code by selecting their choice of source and target languages, then request a translation. 

As of now the website supports translation between two languages - `C++` and `Python`. The model used for translation is PLBART. 

This is how the homepage looks.

![Website Homepage](translate/static/media/homepage.png "Website Homepage") 


## Usage

The interface was built using Django famework and the frontend was designed using HTML and CSS. 

In order to deploy this website, execute the following steps - 

1. Install Python

2. `pip install -r requirements.txt`

3. Create the following folders in translate/model. They have to be added locally since git ignores .bin files. The plbart pre trained checkpoints are more than 500MB so they cannot be pushed.
    ```
    ├── translate
    |   ├── model
    |   |   ├── plbart
    |   |   |   ├── C++-Python
    |   |   |   |   ├── checkpoint-best-bleu
    |   |   |   |   |   ├── pytorch_model.bin       # Pretrained checkpoints
    |   |   |   |── Python-C++
    |   |   |   |   ├── checkpoint-best-bleu
    |   |   |   |   |   ├── pytorch_model.bin       # Pretrained checkpoints
    ```
4. Migrate the database \
    `python manage.py migrate` \
    `python manage.py makemigrations`

5. Start server. \
`python manage.py runserver` \



## Starting off

This project requires understanding how the files interact with each other. A great resource to understand the basics of Django is this tutorial - https://tutorial.djangogirls.org/en/. I really recommend trying out this tutorial if you're completely new to Django.

This is the file tree with the important files and their roles.

```
├── code2code                   # Main project app        
|   ├── settings.py             # Contains setting for the entire project
|   ├── urls.py                 # Contains all project URLs
├── translate                   # App for translation
|   ├── model                   # Contains all NLP model related files
|   |   ├── output_processing   # Folder that makes output pretty
|   |   ├── plbart              # Folder that contains pretrained checkpoints
|   |   ├── inference_utils.py  # Utility functions for prediction. Uses model.py and run.py
|   |   ├── model.py            # PLBART model class and methods
|   |   ├── predict.py          # Initializes model and translates code. Uses inference_utils.py
|   |   ├── process_outputs.py  # Formats translated output. Uses files from output_processing
|   |   ├── run.py              # Has classes used by inference_utils.py
|   ├── static                  
|   |   ├── ace                 # Folder contains Ace editor related files 
|   |   ├── css                 
|   |   |   ├── translate.css   # CSS for home.html        
|   ├── templates               # Folder contains HTML files
|   |   ├── base.html           # HTML skeleton
|   |   ├── home.html           # Homepage of website. Takes user input through form and displays translated output.     
|   ├── forms.py                # Defines the input form  
|   ├── models.py               # Defines database and objects
|   ├── urls.py                 # URLs specific to translate app
|   ├── views.py                # Views render html pages and return responses to web requests 
├── manage.py                   # Executes Django specific tasks
```


## Translation

There are three steps while doing the translation.

1. Initializing the model, config and tokenizer from Hugginface.
2. Loading specific model state dictionary based on the languages the user selected. 
3. Making a prediction on one data point (the code inputed by user).

While Steps 2 and 3 are dependent on user inputs, Step 1 is independent of the user. Step 1 is also the most time consuming. Which is why Step 1 (model initialization from Higgingface) is executed only ONCE, when server is started. Steps 2 and 3 happen whenever the user clicks the Translate button. 


## Syntax Highlighting 

Ace editor is used as a widget for syntax highlighting. It supports almost all languages and it provides many themes. The only issue with Ace is choosing the mode (language) beforehand in the backend. Ideally the highlighting should happen based on which languages were selected from the dropdowns.

This is how the website looks with Ace implemented. 

![Website Homepage with Ace](translate/static/media/homepage%20v2.png "Website Homepage with Ace") 


## Future Work 

- Implementing live syntax highlighing in the input textarea, based on the languages selected from the dropdown. Currently, Ace editor is used for syntax highlighting, but the language has to be set in the backend. 
- Compiling source code provided by user to check for errors before translating. 
- Adding fields to input test cases. 
- Compile and run the testcases provided by integrating backend with online code editors (hackerearth api) or a docker container with images for each language. 
- Add translations for new languages and models. The checkpoints can be stored in the server and the state dictionary is loaded for the particular language pair chosen. 