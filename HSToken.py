import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
import unicodedata 
import HSGoogleHelper as googleAPI

#Methods related to Tokenization
def tokenize_alpha_num(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens                            
                                
#remove stopwords
def remove_stop_words(tokens):
    filteredTokens=[]
    swords = set(stopwords.words('english'))
    for t in tokens:
        if t not in swords:
            filteredTokens.append(t)
    return filteredTokens

#remove tokens below n characters
def remove_short_words(tokens, min):
    filteredTokens = []
    for t in tokens:
        if len(t) >= min:
            filteredTokens.append(t)
    return filteredTokens

def remove_digits(tokens):
    filteredTokens = []
    for t in tokens:
        if not t.isdigit():
            filteredTokens.append(t)
    return filteredTokens

def count_digits(tokens):
    count=0
    for t in tokens:
        if not t.isdigit():
            count+=1
    return count

def is_product_id(token):
    if len(token)==5 and token[:1]=='P' and token[1:].isdigit():
        return True
    return False

def is_invoice_id(token):
    if len(token)==7 and token[:3]=='INV' and token[3:].isdigit():
        print("INVOICE!",token)
        return True
    return False

def recognize_my_items(tokens):
    print("### recognize_my_items")
    recognized_tokens=[]
    count_prod=0
    count_invoice=0
    for t in tokens:
        if is_product_id(t):
            recognized_tokens.append("PRODUCTID")
            count_prod+=1
        elif is_invoice_id(t):
            print("RECOGNIZED INVOICE!")
            recognized_tokens.append("INVOICEID")
            count_invoice+=1
        else:
            recognized_tokens.append(t)
    return recognized_tokens, count_prod, count_invoice

def tokenize(text):
    tokens = tokenize_alpha_num(text)
    tokens = remove_stop_words(tokens)
    #tokens = remove_short_words(tokens, 3)
    return tokens
    
def remove_digits(tokens):
    filteredTokens = []
    for t in tokens:
        if not t.isdigit():
            filteredTokens.append(t)
    return filteredTokens

def count_digits(tokens):
    count=0
    for t in tokens:
        if not t.isdigit():
            count+=1
    return count

def is_product_id(token):
    if len(token)==5 and token[:1]=='P' and token[1:].isdigit():
        return True
    return False

def is_invoice_id(token):
    if len(token)==7 and token[:3]=='INV' and token[3:].isdigit():
        return True
    return False

def recognize_my_items(tokens):
    recognized_tokens=[]
    count_prod=0
    count_invoice=0
    for t in tokens:
        if is_product_id(t):
            recognized_tokens.append("PRODUCTID")
            count_prod+=1
        elif is_invoice_id(t):

            recognized_tokens.append("INVOICEID")
            count_invoice+=1
        else:
            recognized_tokens.append(t)
    return recognized_tokens, count_prod, count_invoice

def tokenize(text):
    tokens = tokenize_alpha_num(text)
    tokens = remove_stop_words(tokens)
    numbers = count_digits(tokens)
    tokens = remove_short_words(tokens, 3)
    return tokens, numbers


def stem_and_tag(tokens):
    stemmer = SnowballStemmer("english")
    stemmed_tokens = []
    for t in tokens:
        stemmed_tokens.append(stemmer.stem(t))
    
    tagged = nltk.pos_tag(stemmed_tokens)
    tagged_dict = combine_tokens(tagged)
    return stemmed_tokens, tagged_dict

def combine_tokens(tokens):
    dict = {}
    for t in tokens:
        count = 1
        if t in dict.keys():
            count = dict[t] + 1
        dict[t] = count
    return dict

def count_types(token_counts):
    nouns = 0
    verbs = 0
    adjectives = 0
    conjunctions = 0
    numerical = 0
    for key, value in token_counts.iteritems():
        type = key[1]
        if len(type)>=2 and type[:2]=="NN":
            nouns+=value
        elif len(type)>=2 and type[:2]=="JJ":
            adjectives+=value
        elif len(type)>=1 and type[:1]=="V":
            verbs+=value
        elif len(type)>=2 and type[:2]=="CC":
            conjunctions+=value
        elif len(type)>=2 and type[:2]=="CD":
            numerical+=value
        #else:
        #    print("unknown type", type)
    return nouns, verbs, adjectives, conjunctions, numerical

def extract_features(image):
    
    #Call Google API
    google_detection= googleAPI.get_text_from_google(image)
    text_areas = googleAPI.collect_text_areas(google_detection)
    count_low, count_med, count_high = googleAPI.count_text_areas_by_size(text_areas)
    
    #Tokenize and turn into Features
    text = google_detection.text
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')
    
    tokens, numbers = tokenize(text)
    total_len = len(tokens)
    tokens, count_prod, count_invoice = recognize_my_items(tokens)
    stemmed_tokens, tagged_tokens = stem_and_tag(tokens)

    nouns, verbs, adjectives, conjunctions, numbers = count_types(tagged_tokens)
    
    features = {}
    features["product_ids"]=count_prod
    features['numbers'] = numbers
    features['invoice_ids']=count_invoice
    features['nouns']=nouns
    features['verbs']=verbs
    features['adjectives']= adjectives
    features['conjunctions']= conjunctions
    features['small_blocks']=count_low
    features['med_blocks']=count_med
    features['large_blocks']=count_high
    features['total_words']=total_len
    return features, text