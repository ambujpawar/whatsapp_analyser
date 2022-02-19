from collections import Counter
from typing import List, Tuple

from utils.read_input import FindUsers


def MessagesCounterByDate(conversations: List[tuple]) -> Counter:
    """
    Conversations are a list of tuples with the format (Datetime, sender, message)
    """
    return Counter(conv[0].date() for conv in conversations)


def MessageCounterByDateAndSender(conversations: List[tuple]) -> List[Counter]:
    """
    Conversations are a list of tuples with the format (Datetime, sender, message)
    """
    users = FindUsers(conversations)
    conversations_by_user = []
    for user in users:
        conv_counter = Counter(conv[0].date() for conv in conversations if conv[1] == user)
        conversations_by_user.append(conv_counter)
    return conversations_by_user
