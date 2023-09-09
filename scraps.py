number_of_sentences = len(sentences)
number_of_characters = sum([len(s) for s in paper_text])

{
    "count_sentences": number_of_sentences,
    "count_characters": number_of_characters,
}

length_word = sum(
    len(element.text.split(" ")) for element in sentences if element.text is not None
)
if number_of_sentences is not None and number_of_sentences != 0:
    avg_sentence_length_char = length_char / number_of_sentences
    avg_sentence_length_word = length_word / number_of_sentences

test = {
    "length_word": length_word,
    "avg_sentence_length_char": avg_sentence_length_char,
    "avg_sentence_length_word": avg_sentence_length_word,
}

# TODO Check what the longest sentence is
def preprocess(data):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
    example = data["raw_summary"][0]
    encoded_source = tokenizer(example)

    with tokenizer.as_target_tokenizer():
        labels = tokenizer(data["raw_paper"], max_length=512, truncation=True)
    
    model_inputs["labels"] = labels["input_ids"]

    return example, encoded_source
