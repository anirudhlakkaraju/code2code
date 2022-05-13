from codegen_sources.preprocessing.lang_processors.cpp_processor import CppProcessor
from codegen_sources.preprocessing.lang_processors.python_processor import PythonProcessor
from codegen_sources.preprocessing.lang_processors.java_processor import JavaProcessor
from codegen_sources.preprocessing.lang_processors.lang_processor import LangProcessor


def pretty(code):
    py_processor = LangProcessor.processors["python"](root_folder="./build")
    cpp_processor = LangProcessor.processors["cpp"](root_folder="./build")
    # java_processor = LangProcessor.processors["java"](root_folder="./build")

    #You most probably dot need the tokenizers
    # py_tokenizer = py_processor.tokenize_code
    # cpp_tokenizer = cpp_processor.tokenize_code
    # java_tokenizer = java_processor.tokenize_code

    #Use the detokenizers on the outputs
    py_detokenizer = py_processor.detokenize_code
    cpp_detokenizer = cpp_processor.detokenize_code
    # java_detokenizer = java_processor.detokenize_code

    pretty_code = py_detokenizer(code)

    return pretty_code