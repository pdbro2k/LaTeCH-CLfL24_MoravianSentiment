import pandas as pd

def get_sentiws_df(sentiws_base_path):
    def join_columns(columns, separator):
        return separator.join([column for column in columns if column != ""])

    # read and concat files
    sentiws_df = pd.concat([
        pd.read_csv(f"{sentiws_base_path}_{label}.txt", sep="\t", names=["lemma", "polarity", "forms"]) for label in ["Positive", "Negative"]
    ])
    
    # split concatenated lemma into lemma/pos
    sentiws_df[["lemma", "pos"]] = sentiws_df["lemma"].str.split('|', expand=True)

    # split forms into multiple columns
    sentiws_df["forms"].fillna('', inplace=True)
    sentiws_df['forms'] = sentiws_df.apply(lambda x: join_columns([x['lemma'], x['forms']], ","), axis=1)
    sentiws_df["forms"] = sentiws_df["forms"].str.split(",")
    sentiws_df = sentiws_df.explode("forms")

    # rename and rearrange header
    sentiws_df.rename(columns = {"forms": "word"}, inplace = True)
    sentiws_df = sentiws_df[["word", "lemma", "pos", "polarity"]]
    
    return sentiws_df
    
def get_sentiws_score(sentiws_df, instance):
    words = instance.split()
    score = 0
    for word in words:
        value_list = list(sentiws_df.loc[sentiws_df["word"] == word]["polarity"])
        if len(value_list) == 1: # get only the first match
            score += value_list[0]
    return score / len(words)

def get_label(polarity, threshold=.05):
    if polarity >= threshold:
        return "positive"
    if polarity <= threshold * -1:
        return "negative"
    return "neutral"

def get_polarity(label):
    if label == "positive":
        return 1
    if label == "negative":
        return -1
    return 0