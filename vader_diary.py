import os
from collections import Counter
from nltk.sentiment import vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_emoji(score):
    """
    returns an emoji based on the intensity score
    """
    if score > 0.05:
        return ':)'
    elif score < -0.05:
        return ':('
    else:
        return ':|'

def get_sentiment(path, model):
    """
    opens the entry at the given path and gets its score
    """
    with open(path, 'r') as f:
        a = f.read()
        score = model.polarity_scores(a)['compound']
        return get_emoji(score), score

def main():
    diary_path = input('Please input the path to the root folder of your diary. ')
    
    entries = []
    emoji_list = []
    vader = SentimentIntensityAnalyzer()

    # get a list of all diary entries
    for root, dirs, files in os.walk(diary_path):
        for name in files:
            if name.endswith('.md'):
                entries.append(os.path.join(root, name))

    print(f'{len(entries)} entries found!')

    # now get the sentiment for each entry
    for entry in entries:
        print(f'reading {entry}...')

        emoji, score = get_sentiment(entry, vader)
        print(f'\trated: {emoji} ({score})')

        emoji_list.append(emoji)

    # convert the Counter object to a dict
    emoji_count = dict(Counter(emoji_list))

    # now output the totals
    for sentiment in emoji_count:
        print(f'{emoji_count[sentiment]} entries rated {sentiment}')

if __name__ == '__main__':
    main()