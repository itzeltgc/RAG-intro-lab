import pandas as pd

def prepare_data(file_path):
    print('phase 1: initiating data ingest...')

    # load df
    df = pd.read_csv(file_path, names = ['sentiment','headline'], header = None, encoding= 'latin-1')

    # clean null values
    df_clean = df.dropna(subset=['sentiment','headline'])

    # additional cleaning: erase additional blank spaces
    df_clean.loc[:, 'headline'] = df_clean['headline'].str.strip()
    df_clean.loc[:, 'sentiment'] = df_clean['sentiment'].str.strip().str.lower()

    new_records = df_clean.to_dict('records')

    return new_records