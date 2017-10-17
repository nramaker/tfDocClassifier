import pandas as pd 
import random

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

def generate_random(original, deviation, i):
    new_df = create_feature_df()
    index = len(new_df)


    new_df = new_df.set_value(index,'label', original.get_value(i,'label'))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'product_ids',original.get_value(i,'product_ids')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'numbers', original.get_value(i,'numbers')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'invoice_ids',original.get_value(i,'invoice_ids')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'nouns',original.get_value(i,'nouns')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'verbs',original.get_value(i,'verbs')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'adjectives',original.get_value(i,'adjectives')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'conjunctions',original.get_value(i,'conjunctions')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'small_blocks',original.get_value(i,'small_blocks')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'med_blocks', original.get_value(i,'med_blocks')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'large_blocks', original.get_value(i,'large_blocks')*(1+r))
    r=random.uniform(-deviation,deviation)
    new_df.set_value(index,'total_words',original.get_value(i,'total_words')*(1+r))

    return new_df

def fill_random(dataframe, size, deviation=0.3):
    original_size = len(dataframe)
    if original_size==0:
        print("Don't call fill_random with an empty dataframe!")
        return dataframe
    while len(dataframe) < size:
        random_index = random.randint(1, original_size)
        #print("selecting row", random_index)
        df_sample = dataframe.iloc[random_index-1:random_index]
        #print(df_sample)
        df_new = generate_random(df_sample, deviation, random_index-1)
        print(df_new)
        dataframe = dataframe.append(df_new, ignore_index=True)
    return dataframe
