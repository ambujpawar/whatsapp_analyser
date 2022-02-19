from datetime import datetime
from typing import List


def ReadInput(filepath: str) -> List[tuple]:
    """
    Reads input file provided a filepath and converts it into a list of tuples of datetime, person's name and the message
    """
    input_file = open(filepath, encoding='UTF-8')
    input_strings = input_file.readlines()
    conversations = []
    users = []

    for message in input_strings:
        try:
            datetime_as_str, person_and_text =  message.split("-")
            timestamp = datetime.strptime(datetime_as_str.strip(), '%m/%d/%y, %H:%M')

            person, text = person_and_text.strip().lower().split(':')

            if person not in users:
                users.append(person)
            
            # Usual case
            conversations.append((timestamp, person, text.strip()))
            
        except ValueError:
            # Go here if there is no user specificied. It means a multiline msg. Previous sender is the user
            conversations.append((timestamp, person, message.strip().lower()))

    input_file.close()
    return conversations


def FindUsers(conversations: List[tuple]) -> List[str]:
    """
    Conversations are a list of tuples with the format (Datetime, sender, message).
    Returns the list of users
    """
    users = []
    for conv in conversations:
        if conv[1] not in users:
            users.append(conv[1])
    return users