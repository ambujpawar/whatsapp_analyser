from collections import Counter
import re
import string
from typing import Tuple

from .message_utils import GetMessagesByUsers, GetUsers


def EmojiCount(conversations: Tuple, n: int) -> Tuple:
    """
    Returns the top n emojis used by the user
    NOTE: Conversations are in the form of (time, user, text)
    """
    users = GetUsers(conversations)
    all_message_by_user = GetMessagesByUsers(conversations)
    most_frequent_by_user = {}
    
    for user in users:
        most_count = Counter()

        for msg in all_message_by_user[user]:
            # Removes all the alphabet characters. Need some postprocessing with punctuations
            most_count += Counter(re.findall(r'\W', msg.translate(str.maketrans('', '', string.punctuation))))
        
        # space still passes thorugh
        most_count.pop(' ')
        most_frequent_by_user[user] = most_count.most_common(n)
    
    return most_frequent_by_user
