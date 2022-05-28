from transformers import BartTokenizer, BartForConditionalGeneration

INPUT_MAX_LEN = 512
OUTPUT_MAX_LEN = 64
BEAMS = 4

class TextSummarizer():

    def __init__(self):
        self.model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-xsum-12-6')
        self.tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-xsum-12-6')

    def __call__(self, text):

        inputs = self.tokenizer.encode_plus(
            text,
            max_length=INPUT_MAX_LEN,
            truncation=True,
            return_tensors='pt'
        )

        summary_ids = self.model.generate(
            inputs['input_ids'],
            num_beams=BEAMS,
            max_length=OUTPUT_MAX_LEN,
            early_stopping=True)

        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return summary
