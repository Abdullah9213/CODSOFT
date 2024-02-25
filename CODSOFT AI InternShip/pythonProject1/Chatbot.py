import spacy
from spacy.tokens import Token
from Pattern import patterns
import random
from spacy.language import Language

# Load English language model with word vectors
nlp = spacy.load('en_core_web_md')


@Language.component("enhance_spacy_pipeline")
def enhance_spacy_pipeline(doc):
    # Your custom component logic goes here
    return doc


# Add your custom pipeline component to the SpaCy pipeline
nlp.add_pipe('enhance_spacy_pipeline', after='ner')

# Add synonym extension attribute to Token class
Token.set_extension('synonyms', default=[], force=True)


# Function to add synonyms to token
def add_synonyms_to_token(token):
    synonyms = set()
    for syn in token._.wordnet.synonyms():
        synonyms.add(syn.lemma())
    token._.set('synonyms', list(synonyms))


# Enhance spaCy pipeline to include synonym information
def enhance_spacy_pipeline(doc):
    for token in doc:
        add_synonyms_to_token(token)
    return doc


class chatbot:
    def __init__(self):
        self.nlp = nlp

    def get_response(self, user_input):
        # Tokenize the user input
        doc = self.nlp(user_input.lower())
        # Check for patterns in the tokenized input
        response, prob = self.match_patterns(doc)
        return response if response else "I'm sorry, I don't understand.", prob

    def match_patterns(self, doc):
        max_match = 0
        best_response = None
        for pattern, responses in patterns.items():
            pattern_tokens = self.nlp(pattern.lower())
            match_count = self.pattern_matches(pattern_tokens, doc)
            # Calculate probability based on match count
            prob = match_count / len(pattern_tokens)
            if match_count > max_match:
                max_match = match_count
                best_response = self.select_response(responses), prob
        return best_response

    def pattern_matches(self, pattern_tokens, doc):
        match_count = 0
        for token in pattern_tokens:
            if token.text in doc.text:
                match_count += 1
        return match_count

    def select_response(self, responses):
        # Randomly select a response from the list of possible responses
        return random.choice(responses)


my_chatbot = chatbot()
