from bertviz.transformers_neuron_view import BertModel, BertTokenizer
from bertviz.neuron_view import show
 
def bertKVQ(sentence_a, sentence_b):  
    model_type = 'bert'
    model_version = 'bert-base-uncased'
    model = BertModel.from_pretrained(model_version, output_attentions=True)
    tokenizer = BertTokenizer.from_pretrained(model_version, do_lower_case=True)
    show(model, model_type, tokenizer, sentence_a, sentence_b, layer=4, head=3)