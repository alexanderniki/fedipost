"""
File: instance.py
Version: 0.1
Author: Aleksandr Nikiforov (Lonin)
Contact: https://alexanderniki.name
Date: Nov 23, 2024
Description: A fediverse instance
"""


from dataclasses import dataclass


@dataclass
class Instance:
    """
    Instance

    Attr:
        instance_url (str): Instance URL
        instance_name (str): Instance name
    """

    instance_url: str = ""
    instance_name: str = ""
