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


@dataclass
class Post:
    """
    Post
    """

    content_warning: str = ""  # CW
    main_text: str = ""        # Main text
    attachments_list: List = []     # Attachments (paths)
