from bertviz import head_view, model_view
from transformers import BertTokenizer, BertModel


def berthead(sentence_a, sentence_b):
    model_version = 'bert-base-uncased'
    model = BertModel.from_pretrained(model_version, output_attentions=True)
    tokenizer = BertTokenizer.from_pretrained(model_version)
    inputs = tokenizer.encode_plus(sentence_a, sentence_b, return_tensors='pt')
    input_ids = inputs['input_ids']
    token_type_ids = inputs['token_type_ids']
    attention = model(input_ids, token_type_ids=token_type_ids)[-1]
    sentence_b_start = token_type_ids[0].tolist().index(1)
    input_id_list = input_ids[0].tolist() # Batch index 0
    tokens = tokenizer.convert_ids_to_tokens(input_id_list)
    head_view(attention, tokens, sentence_b_start)