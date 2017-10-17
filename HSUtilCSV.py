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

def generate_random(original, deviation):
    new_df = create_feature_df()
    index = len(new_df)

    new_df = new_df.set_value(index,'label', original['label'])
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'product_ids',original['product_ids']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'numbers', original['numbers']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'invoice_ids',original['invoice_ids']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'nouns',original['nouns']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'verbs',original['verbs']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'adjectives',original['adjectives']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'conjunctions',original['conjunctions']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'small_blocks',original['small_blocks']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'med_blocks', original['med_blocks']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'large_blocks', original['large_blocks']*(1+random))
    random=random.randrange(-deviation,deviation)
    new_df.set_value(index,'total_words',original['total_words']*(1+random))

    return new_df

def fill_random(dataframe, size, deviation=0.1):
    original_size = len(dataframe)
    if original_size==0:
        print("Don't call fill_random with an empty dataframe!")
        return dataframe
    while len(dataframe < size):
        random_index = random.randint(0, original_size)
        print("selecting row", random_index)
        df_sample = dataframe[random_index]
        print(df_sample)
        df_new = generate_random(df_sample, deviation)
        dataframe = dataframe.append(new_df, ignore_index=True)
    return dataframe
