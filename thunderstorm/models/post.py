"""
File: post.py
Version: 0.1
Author: Aleksandr Nikiforov (Lonin)
Contact: https://alexanderniki.name
Date: Nov 23, 2024
Description: A fediverse post (toot)
"""


from dataclasses import dataclass
from typing import List
from typing_extensions import Tuple


@dataclass
class Post:
    """
    Post

    Attr:
        content_warning (str): CW
        main_text (str): Posts' text
        attachments_list (List): Attachments paths
        location (Tuple): Location

    TODO:
        - Find documentation about locations in Fediverse
    """

    content_warning: str = ""
    main_text: str = ""
    attachments_list: List = []
    location: Tuple = (0.0, 0.0)
