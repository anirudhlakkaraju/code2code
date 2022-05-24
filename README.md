# Code2Code Translator

Code2Code Translator is a web interface built to showcase the working of Natural Language Processing (NLP) models that translate between Programming Languages (PL). 

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
|   ├── model                   # Contains all NLP model related stuff
|   |   ├── output_processing   # Folder that makes output pretty
|   |   ├── plbart              # Folder that contains pretrained checkpoints
|   |   ├── inference_utils.py  # Utility functions used by predict.py
|   |   ├── model.py            # PLBART model methods
|   |   ├── predict.py          # Initializes model and translates code
|   |   ├── process_outputs.py  # Formats translated output 
|   |   ├── run.py              # Has classes used by inference_utils.py
|   ├── static                  
|   |   ├── ace                 # Folder contains Ace editor related files 
|   |   ├── css                 
|   |   |   ├── translate.css   # CSS for home.html        
|   ├── templates               # Folder contains HTML files
|   |   ├── base.html           # HTML skeleton
|   |   ├── home.html           # Homepage of website    
|   ├── forms.py                # Defines form and    
|   ├── models.py               # Defines database and objects
|   ├── urls.py                 # Translate app specific URLs
|   ├── views.py                # Views return responses for web requests
├── manage.py                   # Executes Django specific tasks
    ```