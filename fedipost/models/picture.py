"""
File: picture.py
Version: 0.1
Author: Aleksandr Nikiforov (Lonin)
Contact: https://alexanderniki.name
Date: Nov 23, 2024
Description: A fediverse picture
"""


from dataclasses import dataclass


@dataclass
class Picture:
    """
    Picture
    """

    pic_path: str = ""  # Path to the picture
    alt_text: str = ""  # Alt text for the picture
