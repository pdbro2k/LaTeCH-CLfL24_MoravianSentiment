def calc_polarity(sentiment_dict, instance):
    words = instance.split()
    score = 0
    for word in words:
        if word in sentiment_dict:
            score += sentiment_dict[word]
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