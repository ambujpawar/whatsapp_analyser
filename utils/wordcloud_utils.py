"""
The utitlity functions regarding the creation of wordcloud will be stored here
"""
import numpy as np
from typing import Dict, List, Set, Tuple

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
from .message_utils import GetUsers, GetMessagesByUsers
from .read_input import ReadStopwordsTextFile


def AddCustomStopwords(filepath: str) -> Set:
    """
    Takes a txt file containing all the words that you want to eliminate from the wordcloud
    """
    stopwords = set(STOPWORDS)
    custom_stopwords = ReadStopwordsTextFile(filepath)

    for word in custom_stopwords:
        stopwords.add(word)
    return stopwords


def PrepareDataForWordcloud(conversations: List[Tuple], for_every_user: bool = False):
    """
    Prepare data for creating wordcloud
    @param for_every_user: Draw wordcloud for every user seperately
    """
    all_messages_by_user = GetMessagesByUsers(conversations)

    if for_every_user:
        all_words_by_user = {user: ' '.join(messages) for user, messages in all_messages_by_user.items()}
    else:
        # TODO: Fix this
        for user, messages in all_messages_by_user.items():
            all_words = " ".join(msg for msg in messages)    
    return all_words_by_user
    
def DrawWordCloud(data: Dict, base_image_path: str = None, stopwords: Set = None):
    """
    Draw wordcloud based on the conversations given
    @param base_image_path: Path to image to be used to draw a wordcloud
    @param stopwords: Path to text file containing all the stopwords
    """
    mask = np.array(Image.open(base_image_path))
    wordcloud = WordCloud(width=600, height=600, stopwords=stopwords, background_color='white', mask=mask, min_font_size=8, max_font_size=50, max_words=400).generate(data)
    image_colors = ImageColorGenerator(mask)

    plt.figure(figsize=[40,40])
    #plt.imshow(wordcloud, interpolation="bilinear")
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    # store to file
    plt.savefig("news2.png", format="png") 
    plt.show()