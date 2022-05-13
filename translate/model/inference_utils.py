from run import *
from bleu import _bleu

def convert_examples_to_features(examples, tokenizer, max_source_length, max_target_length, stage=None):
    features = []
    for example_index, example in enumerate(examples):
        #source
        source_tokens = tokenizer.tokenize(example.source)[:max_source_length-2]
        source_tokens =[tokenizer.cls_token]+source_tokens+[tokenizer.sep_token]
        source_ids =  tokenizer.convert_tokens_to_ids(source_tokens) 
        source_mask = [1] * (len(source_tokens))
        padding_length = max_source_length - len(source_ids)
        source_ids+=[tokenizer.pad_token_id]*padding_length
        source_mask+=[0]*padding_length
 
        #target
        if stage=="test":
            target_tokens = tokenizer.tokenize("None")
        else:
            target_tokens = tokenizer.tokenize(example.target)[:max_target_length-2]
        target_tokens = [tokenizer.cls_token]+target_tokens+[tokenizer.sep_token]            
        target_ids = tokenizer.convert_tokens_to_ids(target_tokens)
        target_mask = [1] *len(target_ids)
        padding_length = max_target_length - len(target_ids)
        target_ids+=[tokenizer.pad_token_id]*padding_length
        target_mask+=[0]*padding_length   
   
        if example_index < 5:
            if stage=='train':
                logger.info("*** Example ***")
                logger.info("idx: {}".format(example.idx))

                logger.info("source_tokens: {}".format([x.replace('\u0120','_') for x in source_tokens]))
                logger.info("source_ids: {}".format(' '.join(map(str, source_ids))))
                logger.info("source_mask: {}".format(' '.join(map(str, source_mask))))
                
                logger.info("target_tokens: {}".format([x.replace('\u0120','_') for x in target_tokens]))
                logger.info("target_ids: {}".format(' '.join(map(str, target_ids))))
                logger.info("target_mask: {}".format(' '.join(map(str, target_mask))))
       
        features.append(
            InputFeatures(
                 example_index,
                 source_ids,
                 target_ids,
                 source_mask,
                 target_mask,
            )
        )
    return features

# def get_eval_dataloader(data_path, lang1, lang2, eval_batch_size, max_source_length, max_target_length, tokenizer):
#     lang_pair = lang1 + "-" + lang2
#     if not os.path.isdir(data_path + lang_pair):
#         lang_pair = lang2 + "-" + lang1
#     test_file_prefix = data_path + lang_pair + "/test-" + lang_pair + "-tok"
#     test_src_file = test_file_prefix + file_extensions[lang1]
#     test_tgt_file = test_file_prefix + file_extensions[lang2]
#     test_file = test_src_file + "," + test_tgt_file
    
#     eval_examples = read_examples(test_file)
#     eval_features = convert_examples_to_features(eval_examples, tokenizer, 
#                                                  max_source_length, max_target_length,stage='test')
#     all_source_ids = torch.tensor([f.source_ids for f in eval_features], dtype=torch.long)
#     all_source_mask = torch.tensor([f.source_mask for f in eval_features], dtype=torch.long)    
#     eval_data = TensorDataset(all_source_ids,all_source_mask)   

#     # Calculate bleu
#     eval_sampler = SequentialSampler(eval_data)
#     eval_dataloader = DataLoader(eval_data, sampler=eval_sampler, batch_size=eval_batch_size)
#     return test_file, eval_examples, eval_dataloader

# def get_eval_dataloader(data_path, lang1, lang2, eval_batch_size, max_source_length, max_target_length, tokenizer):
#     lang_pair = lang1 + "-" + lang2
#     if not os.path.isdir(data_path + lang_pair):
#         lang_pair = lang2 + "-" + lang1
#     test_file_prefix = data_path + lang_pair + "/test-" + lang_pair + "-tok"
#     test_src_file = test_file_prefix + file_extensions[lang1]
#     test_tgt_file = test_file_prefix + file_extensions[lang2]
#     test_file = test_src_file + "," + test_tgt_file
    
#     eval_examples = read_examples(test_file)
#     eval_features = convert_examples_to_features(eval_examples, tokenizer, 
#                                                  max_source_length, max_target_length,stage='test')
#     all_source_ids = torch.tensor([f.source_ids for f in eval_features], dtype=torch.long)
#     all_source_mask = torch.tensor([f.source_mask for f in eval_features], dtype=torch.long)    
#     eval_data = TensorDataset(all_source_ids,all_source_mask)   

#     # Calculate bleu
#     eval_sampler = SequentialSampler(eval_data)
#     eval_dataloader = DataLoader(eval_data, sampler=eval_sampler, batch_size=eval_batch_size)
#     return test_file, eval_examples, eval_dataloader

# def get_eval_dataloader(code_string, eval_batch_size, max_source_length, max_target_length, tokenizer):
    
    
#     eval_examples = read_example(code_string)
#     eval_features = convert_examples_to_features(eval_examples, tokenizer, 
#                                                  max_source_length, max_target_length,stage='test')
#     all_source_ids = torch.tensor([f.source_ids for f in eval_features], dtype=torch.long)
#     all_source_mask = torch.tensor([f.source_mask for f in eval_features], dtype=torch.long)    
#     eval_data = TensorDataset(all_source_ids,all_source_mask)   

#     # Calculate bleu
#     eval_sampler = SequentialSampler(eval_data)
#     eval_dataloader = DataLoader(eval_data, sampler=eval_sampler, batch_size=eval_batch_size)
#     return eval_examples, eval_dataloader, eval_data, all_source_ids, all_source_mask

def get_eval_tensors(code_string, max_source_length, max_target_length, tokenizer):

    eval_examples = read_example(code_string)
    eval_features = convert_examples_to_features(eval_examples, tokenizer, 
                                                 max_source_length, max_target_length,stage='test')
    all_source_ids = torch.tensor([f.source_ids for f in eval_features], dtype=torch.long)
    all_source_mask = torch.tensor([f.source_mask for f in eval_features], dtype=torch.long)    
   
    return all_source_ids, all_source_mask



def sample_generation_single(all_source_ids, all_source_mask, model, model_type, tokenizer, max_target_length, 
                             device, do_sample=False, beam_size=1, temperature=0.5):
    p=[]
    pred_ids = []

    source_ids,source_mask = all_source_ids.to(device), all_source_mask.to(device)                 
    
    with torch.no_grad():
        if model_type == 'roberta':
                preds = model(source_ids=source_ids, source_mask=source_mask)
        else:
            preds = model.generate(source_ids,
                                   attention_mask=source_mask,
                                   use_cache=True,
                                   num_beams=beam_size,
                                   do_sample=do_sample,
                                   temperature=temperature,
                                   early_stopping=False, # 如果是summarize就设为True
                                   max_length=max_target_length,
                                   decoder_start_token_id=tokenizer.sep_token_id)
            top_preds = list(preds.cpu().numpy())
            pred_ids.extend(top_preds)

    p = [tokenizer.decode(id, skip_special_tokens=True, 
                              clean_up_tokenization_spaces=False)
                              for id in pred_ids]
    return p



# def sample_generation_single(test_file, eval_examples, eval_dataloader, model, model_type, tokenizer, max_target_length,
#                         out_fn, device, output_dir='./', do_sample=False, beam_size=1, temperature=0.5):
#     p=[]
#     pred_ids = []
#     for batch in tqdm(eval_dataloader,total=len(eval_dataloader)):
#         batch = tuple(t.to(device) for t in batch)
#         source_ids,source_mask= batch                  
#         with torch.no_grad():
#             if model_type == 'roberta':
#                     preds = model(source_ids=source_ids, source_mask=source_mask)
#             else:
#                 preds = model.generate(source_ids,
#                                        attention_mask=source_mask,
#                                        use_cache=True,
#                                        num_beams=beam_size,
#                                        do_sample=do_sample,
#                                        temperature=temperature,
#                                        early_stopping=False, # 如果是summarize就设为True
#                                        max_length=max_target_length,
#                                        decoder_start_token_id=tokenizer.sep_token_id)
#                 top_preds = list(preds.cpu().numpy())
#                 pred_ids.extend(top_preds)

#         p = [tokenizer.decode(id, skip_special_tokens=True, 
#                                   clean_up_tokenization_spaces=False)
#                                   for id in pred_ids]
#         print(p)
#         break
#     predictions=[]
#     accs=[]
#     idx = 0
#     file = test_file
#     with open(os.path.join(output_dir, out_fn),'w'
#              ) as f, open(os.path.join(output_dir,"test_{}.gold".format(str(idx))),'w') as f1:
#         for ref,gold in zip(p, eval_examples):
#             predictions.append(str(gold.idx)+'\t'+ref)
#             f.write(ref+'\n')
#             f1.write(gold.target+'\n')    
#             accs.append(ref==gold.target)
#     dev_bleu=round(_bleu(os.path.join(output_dir, "test_{}.gold".format(str(idx))).format(file), 
#                          os.path.join(output_dir, out_fn).format(file)),2)
#     print("  %s = %s "%("bleu-4",str(dev_bleu)))
#     print("  %s = %s "%("xMatch",str(round(np.mean(accs)*100,4))))
#     print("  "+"*"*20)  
#     return

def get_model(model_type, lang1, lang2):
    model_name_or_path = "uclanlp/plbart-python-en_XX" #"uclanlp/plbart-base" #uclanlp/plbart-python-en_XX
    load_model_path_prefix = model_path + lang1 + "-" + lang2 + "/"
    load_model_path = load_model_path_prefix + "checkpoint-best-bleu/pytorch_model.bin"
    config_class, model_class, tokenizer_class = MODEL_CLASSES[model_type]
    config = config_class.from_pretrained(model_name_or_path)
    tokenizer = tokenizer_class.from_pretrained("uclanlp/plbart-base")
    model = model_class.from_pretrained(model_name_or_path) #model_name_or_path
    model.load_state_dict(torch.load(load_model_path))
    model.eval()
    return model, tokenizer

file_extensions = {"Java": ".java", "C++": ".cpp", "C": ".c", "Python": ".py","Javascript": ".js",
                   "PHP":".php", "C#":".cs"}

model_path = "./plbart_official/"