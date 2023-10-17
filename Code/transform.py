import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from datetime import datetime



def sentiment_score(review):

    model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    rating = int(torch.argmax(result.logits))+1
    if rating <= 2:
        return -1
    elif rating == 3:
        return 0
    else:
        return 1

def split_date(date_str):
    if pd.isna(date_str):
        return None, None, None
    else:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        day = date_obj.day
        month = date_obj.month
        year = date_obj.year
        return day, month, year

def transform(**kwargs):
    
    print("-------------------------transform-------------------------")
    extracted_data = kwargs['ti'].xcom_pull(task_ids='extract_task')
    df = pd.DataFrame(extracted_data)
    df = df.dropna(subset=['text'])

    df['latitude'] = df['location'].apply(lambda loc: loc['lat'])
    df['longitude'] = df['location'].apply(lambda loc: loc['lng'])

    columns_to_keep = ['latitude', 'longitude', 'city', 'state', 'countryCode', 'text', 'publishedAtDate']
    df = df[columns_to_keep]

    df[['day', 'month', 'year']] = df['publishedAtDate'].apply(lambda x: pd.Series(split_date(x)))
    df = df.drop('publishedAtDate', axis=1)
    df['day'] = df['day'].astype(int)
    df['month'] = df['month'].astype(int)
    df['year'] = df['year'].astype(int)


    df['score'] = df['text'].apply(lambda x: sentiment_score(x[:512]) if isinstance(x, str) else np.nan)
    df.dropna()
    df = df.drop('text', axis=1)


    #return df.values.tolist()
    return df


