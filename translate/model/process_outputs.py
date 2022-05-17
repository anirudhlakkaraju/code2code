from .output_processing.codegen_sources.preprocessing.lang_processors.cpp_processor import CppProcessor
from .output_processing.codegen_sources.preprocessing.lang_processors.python_processor import PythonProcessor
from .output_processing.codegen_sources.preprocessing.lang_processors.java_processor import JavaProcessor
from .output_processing.codegen_sources.preprocessing.lang_processors.lang_processor import LangProcessor


def pretty(code, lang):

    lang_selection = {
        "Python" : "python",
        "C++" : "cpp",
    }

    # Initializes object to process given code 
    processor = LangProcessor.processors[lang](root_folder="translate/model/output_processing/build")

    # Use the detokenizers on the outputs
    detokenizer = processor.detokenize_code

    # Generate and return pretty (formatted) code
    pretty_code = detokenizer(code)

    return pretty_code