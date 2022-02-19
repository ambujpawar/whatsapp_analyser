import argparse

from utils.read_input import ReadInput
from utils.emoji_count import EmojiCount
from utils.message_utils import GetMessageStatistics

def ParseArgs():
    """Parses the arguments"""
    parser = argparse.ArgumentParser("Whatsapp chat analyser based on the flags given")
    parser.add_argument('chat', type=str, help='Path to the whatsapp chat')
    parser.add_argument('-emoji_count', action='store_false', help="Flag to return the most common emojis used by the 2 persons")
    parser.add_argument('-word_count', action='store_false', help="Flag to return the most common words by the 2 persons")
    parser.add_argument('-n', type=int, default=5, help='the n most frequent words/emojis to be returned')
    parser.add_argument('-word_cloud', action='store_false', help='The wordcloud of the most frequent words to be returned to the user')
    parser.add_argument('-stopwords_filepath', type=str, help='Path to the file with the list of words not to be used in the wordcloud')
    parser.add_argument('-wordcloud_imagepath', type=str, help='Path to the image file to be used as base. Otherwise the default wordcloud will be used')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    # Read the input file
    filepath = "/Users/ambuj/Desktop/PycharmProject1/data/WhatsAppChat-Asha_part2.txt"
    n = 5

    conversations = ReadInput(filepath)
    statistics = GetMessageStatistics(conversations)
    
    """
    emoji_count = EmojiCount(conversations, n=5)
    for user, emojis in emoji_count.items():
        print('The {} most common emoji used by {} are: '.format(n, user))
        for emoji in emojis:
            print(emoji)
    """

    # args = ParseArgs()
    print("DONE")
