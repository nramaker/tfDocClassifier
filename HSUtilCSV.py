import pandas as pd 

def load_file(csv):
    dataframe = pd.read_csv(csv)
    return dataframe

def save_to_file(dataframe, file):
    dataframe.to_csv(file, sep=',', encoding='utf-8')

def create_feature_df():
    new_df = pd.DataFrame(columns=('label', 'product_ids', 'numbers','invoice_ids','nouns','verbs','adjectives','conjunctions','small_blocks', 'med_blocks', 'large_blocks', 'total_words'))
    return new_df
def append_to_dataframe(dataframe, features, label):
    new_df = create_feature_df()
    index = len(new_df)
    new_df = new_df.set_value(index,'label', label)
    new_df.set_value(index,'product_ids',features['product_ids'])
    new_df.set_value(index,'numbers', features['numbers'])
    new_df.set_value(index,'invoice_ids',features['invoice_ids'])
    new_df.set_value(index,'nouns',features['nouns'])
    new_df.set_value(index,'verbs',features['verbs'])
    new_df.set_value(index,'adjectives',features['adjectives'])
    new_df.set_value(index,'conjunctions',features['conjunctions'])
    new_df.set_value(index,'small_blocks',features['small_blocks'])
    new_df.set_value(index,'med_blocks', features['med_blocks'])
    new_df.set_value(index,'large_blocks', features['large_blocks'])
    new_df.set_value(index,'total_words',features['total_words'])

    dataframe = dataframe.append(new_df, ignore_index=True)
    return dataframe