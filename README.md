# Code2Code Translator

Code2Code Translator is a web interface built to showcase the working of Natural Language Processing (NLP) models that translate between Programming Languages (PL). 

## Documentation

The interface was built using Django famework and the frontend was designed using HTML and CSS. 

### Usage

In order to deploy this website, execute the following steps - 

1. Install Python

2. `pip install -r requirements.txt`

3. Create the following folders in translate/model. They have to be added locally since git ignores .bin files. The plbart pre trained checkpoints are more than 500MB so they cannot be pushed.
    ```
    ├── Translate
    |    ├── model
    |    |    ├── plbart
    |    |    |    ├── C++-Python
    |    |    |    |   ├── checkpoint-best-bleu
    |    |    |    |   |    ├── pytorch_model.bin       # Model Checkpoints to translate bw C++ and Python
    |    |    |    |── Python-C++
    |    |    |    |   ├── checkpoint-best-bleu
    |    |    |    |   |    ├── pytorch_model.bin       # Model Checkpoints to translate bw Python and C++
    ```
4. `python manage.py migrate`
    `python manage.py makemigrations`
