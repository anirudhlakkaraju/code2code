import os
import torch
from inference_utils import *
device = torch.device("cuda")

# data_path = "./small_test_data/"
# lang1 = "C++"
# lang2 = "Python"

model_type = "plbart"
model, tokenizer = get_model(model_type, lang1, lang2)
model.to(device)
print()

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



eval_batch_size = 1
max_source_length, max_target_length = 400, 400


x = """int fib(int n)
{
    if (n <= 1)
        return n;
    return fib(n-1) + fib(n-2);
}
 
int main ()
{
    int n = 9;
    cout << fib(n);
    getchar();
    return 0;
}
"""

eval_examples, eval_dataloader = get_eval_dataloader(x, eval_batch_size, 
                                                     max_source_length, max_target_length, tokenizer)

pred = sample_generation_single(eval_examples, eval_dataloader, model, model_type, tokenizer, 
                         max_target_length, device)



print(process_python_output(pred[0]))