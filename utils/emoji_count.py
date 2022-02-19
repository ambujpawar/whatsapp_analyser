from collections import Counter
import re
from typing import Tuple

from .message_utils import GetMessagesByUsers


def EmojiCount(conversations: Tuple, n: int) -> Tuple:
    """
    Returns the top n emojis used by the user
    NOTE: Conversations are in the form of (time, user, text)
    """
    all_message_by_user = GetMessagesByUsers(conversations)
    print('DONE')
    pass
