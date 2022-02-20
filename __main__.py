from utils.read_input import ReadInput
from utils.emoji_count import EmojiCount
from utils.message_utils import GetMessageStatistics, GetMessagesByTime, GetMessagesByDay
from utils.wordcloud_utils import PrepareDataForWordcloud, AddCustomStopwords, DrawWordCloud


if __name__ == '__main__':
    # Read the input file
    filepath = "/Users/ambuj/Desktop/PycharmProject1/data/WhatsAppChat-Asha_part2.txt"
    stopwords_filepath = "/Users/ambuj/Desktop/GithubProjects/whatsapp_analyser/data/stopwords.txt"
    n = 5

    conversations = ReadInput(filepath)

    #statistics = GetMessageStatistics(conversations)
    #time_statistics = GetMessagesByDay(conversations)
    
    custom_stopwords = AddCustomStopwords(stopwords_filepath)
    data = PrepareDataForWordcloud(conversations, for_every_user=True)
    DrawWordCloud(data['asha nit'] + data['ambuj'], stopwords=custom_stopwords)
    
    """
    emoji_count = EmojiCount(conversations, n=5)
    for user, emojis in emoji_count.items():
        print('The {} most common emoji used by {} are: '.format(n, user))
        most_common_emojis = emojis.most_common(n)
        for emoji in most_common_emojis:
            print(emoji)
    """

    print("DONE")
