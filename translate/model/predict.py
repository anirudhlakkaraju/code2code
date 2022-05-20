import os
import torch
from .inference_utils import *
from django.core.cache import cache

# Initializes model globally as None
model = None

# Setup device and model paths
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_type = 'plbart'
model_path = "translate/model/plbart/"

# Download model config and tokenizers on runserver. Executes ONLY ONCE when server is started.
model_name_or_path = "uclanlp/plbart-python-en_XX" #"uclanlp/plbart-base" #uclanlp/plbart-python-en_XX
config_class, model_class, tokenizer_class = MODEL_CLASSES[model_type]
config = config_class.from_pretrained(model_name_or_path)
tokenizer = tokenizer_class.from_pretrained("uclanlp/plbart-base")

# Key to retrieve model from cache
model_cache_key = 'model_cache' 
model = cache.get(model_cache_key)

# Load model if not present in cache
if model is None:
    model = model_class.from_pretrained(model_name_or_path) # load model
    cache.set(model_cache_key, model, None) # save in the cache
    # in above line, None is the timeout parameter. It means cache forever

print('PLBART Model initialized! \n')


def get_model(lang1, lang2):

    # Path to pretrained checkpoints
    load_model_path_prefix = model_path + lang1 + "-" + lang2 + "/"
    load_model_path = load_model_path_prefix + "checkpoint-best-bleu/pytorch_model.bin"
    
    # Loads state dict from pretrained checkpoints
    model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu'))) 

    print("\nget_model OK")
    model.eval()
    return model

    
# Method to format Python outputs. (UNUSED)
def process_python_output(prediction):
    lines = prediction.split("NEW_LINE")
    curr_indent = 0
    new_lines = []
    for line in lines:
        indent_count = line.count('INDENT')
        dedent_count = line.count('DEDENT')
        curr_indent += indent_count - dedent_count
        new_lines.append('\t'*curr_indent + line.replace('INDENT', '').replace('DEDENT', ''))
    return "\n".join(new_lines)


def predict(source_language, target_language, source_code):

    # Obtains model with loaded state dict
    model = get_model(source_language, target_language)
    model.to(device)

    eval_batch_size = 1
    max_source_length, max_target_length = 400, 400
    
    # Obtains source and mask ids
    all_source_ids, all_source_mask = get_eval_tensors(source_code, max_source_length, max_target_length, tokenizer)
    print("eval_tensors OK")

    # Generates prediction 
    pred = sample_generation_single(all_source_ids, all_source_mask, model, model_type, tokenizer, 
                                max_target_length, device)
    print("generation OK\n")

    # Returns prediction with special tokens
    return pred[0]



# x = """int fib(int n)
# {
#     if (n <= 1)
#         return n;
#     return fib(n-1) + fib(n-2);
# }
 
# int main ()
# {
#     int n = 9;
#     cout << fib(n);
#     getchar();
#     return 0;
# }
# """


# include <bits/stdc++.h>
# using namespace std ;
# string process_output ( string prediction ) {
#   string line = "" ;
#   for ( int i = 0 ;
#   i < line . size ( ) - 1 ;
#   i ++ ) {
#     line += "" ;
#   }
#   return line ;
# }
# string _output ( string prediction ) {
#   string new_lines = "" ;
#   for ( int i = 0 ;
#   i < line . size ( ) - 1 ;
#   i ++ ) {
#     new_lines += line . split ( "
#     " ) curr_indent = 0 new_lines . append ( new_lines . pop_first ( ) ) indent_count = line . count ( ' ' dedent_count = line . count ( ' ' curr_indent += indent_count - dedent_count new_lines . append ( '	' * curr_indent + line . replace ( ' ',' ') . replace ( ' ',' ' ) return new_lines ;
