from builtins import all
from collections import Counter
from typing import List, Tuple


def GetUsers(conversations: List[tuple]) -> List[str]:
    """
    Conversations are a list of tuples with the format (Datetime, sender, message).
    Returns the list of users
    """
    users = []
    for conv in conversations:
        if conv[1] not in users:
            users.append(conv[1])
    return users


def MessagesCounterByDate(conversations: List[tuple]) -> Counter:
    """
    Conversations are a list of tuples with the format (Datetime, sender, message)
    """
    return Counter(conv[0].date() for conv in conversations)


def MessageCounterByDateAndSender(conversations: List[tuple]) -> List[Counter]:
    """
    Conversations are a list of tuples with the format (Datetime, sender, message)
    """
    users = GetUsers(conversations)
    conversations_by_user = []
    for user in users:
        conv_counter = Counter(conv[0].date() for conv in conversations if conv[1] == user)
        conversations_by_user.append(conv_counter)
    return conversations_by_user


def GetMessagesByUsers(conversations: List[Tuple]):
    """
    Group all the message sent by a user
    """
    all_messages_by_user = dict()
    for conv in conversations:
        user = conv[1]
        if user not in all_messages_by_user.keys():
            all_messages_by_user[user] = []
        else:
            all_messages_by_user[user].append(conv[2])
    return all_messages_by_user


def GetMessageStatistics(conversations: List[Tuple]):
    """
    Generate a list of statistics based on the conversation.
    For now it only includes, total messages sent, total messages sent by user, pictures sent
    """
    users = GetUsers(conversations)
    all_message_by_user = GetMessagesByUsers(conversations)

    message_sent_by_user = {}

    message_sent_by_user = {user:len(all_message_by_user[user]) for user in users}

    pictures_sent_by_user = {user: 0 for user in users}
    words_sent_by_user = {user: 0 for user in users}

    for user in users:
        for msg in all_message_by_user[user]:

            words_sent_by_user[user] += len(msg)
            if 'media omitted' in msg:
                pictures_sent_by_user[user] += 1

    return message_sent_by_user, words_sent_by_user, pictures_sent_by_user