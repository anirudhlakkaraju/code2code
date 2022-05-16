from .output_processing.codegen_sources.preprocessing.lang_processors.cpp_processor import CppProcessor
from .output_processing.codegen_sources.preprocessing.lang_processors.python_processor import PythonProcessor
from .output_processing.codegen_sources.preprocessing.lang_processors.java_processor import JavaProcessor
from .output_processing.codegen_sources.preprocessing.lang_processors.lang_processor import LangProcessor


def pretty(code, lang):

    processor = LangProcessor.processors[lang](root_folder="translate/model/output_processing/build")
    # cpp_processor = LangProcessor.processors["cpp"](root_folder="translate/model/output_processing/build")
    # java_processor = LangProcessor.processors["java"](root_folder="./build")

    #You most probably dot need the tokenizers
    # py_tokenizer = py_processor.tokenize_code
    # cpp_tokenizer = cpp_processor.tokenize_code
    # java_tokenizer = java_processor.tokenize_code

    #Use the detokenizers on the outputs
    detokenizer = processor.detokenize_code
    # cpp_detokenizer = cpp_processor.detokenize_code
    # java_detokenizer = java_processor.detokenize_code

    pretty_code = detokenizer(code)

    return pretty_code