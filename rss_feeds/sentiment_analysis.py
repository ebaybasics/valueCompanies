# Import modules
import matplotlib.pyplot as plt
import pandas as pd
import squarify
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')



# Define text and omit_words arguments
# text = "This is a sample text with some repeated words like text and words and some unique words like sample and unique"
# omit_words = ["a", "is", "with", "and", "some"]


def generate_treemap(text, omit_words=None, top_n=15):
    """
    Generate a treemap plot of word frequencies in the given text, excluding specified words.

    :param text: Input text for generating the treemap plot.
    :param omit_words: List of words to exclude from the plot, default is None.
    :param top_n: Number of top words to display in the treemap plot, default is 15.
    """
    # Create stopwords list
    stopwords_list = set(stopwords.words('english'))
    print(stopwords_list)
    # Add custom omit words to the stopwords list
    if omit_words:
        stopwords_list.update(omit_words)

    # Split the text into words and filter out stopwords
    words = [word for word in text.split() if word not in stopwords_list]

    # Create a pandas DataFrame with words and their frequencies
    df = pd.DataFrame(words, columns=["word"])
    df = df.value_counts().reset_index(name="freq")

    df_copy = df
    pd.set_option('display.max_rows', None)
    print(df_copy.head(200))

    # Keep only the top_n rows
    df = df.head(top_n)

    # Generate a treemap
    squarify.plot(sizes=df["freq"], label=df["word"], alpha=0.8)

    # Remove axes
    plt.axis("off")

    # Show plot
    plt.show()


def run_sentiment(rss_data='rss_results.txt'):
    omit = ['How', 'New', 'first', 'A', 'In', 'US', 'Fox', 'The', '&', 'News', 'quarter', 'Why', 'Can', 'says', 'May', 'U.S.', 'Is', 'For', 'After', "To", "Will", "HN:", "And", "Are", "Who", "Of", "new", "More", "This", "best", "That", ":", "From", "Its", "Has", "–", "Up", "Be", "case", "3", "I", "On", "next", "trial", "since", "First", "Could", "Ahead", "His", "Due", "Do", "Not", "Just", "Get", "‘The", "It", "2020", "2022", "Keep", "using", "4", "—", "With", "2", "Go", "About", "may", "Here's", "What", "You", "At", "500", "Among", "2023", "He", "Today", "keep",]

    with open(rss_data, encoding='utf-8') as f:
        text = f.read()
        generate_treemap(text, omit_words=omit, top_n=45)