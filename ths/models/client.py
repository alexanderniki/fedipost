"""
File: client.py
Version: 0.1
Author: Aleksandr Nikiforov (Lonin)
Contact: https://alexanderniki.name
Date: Nov 23, 2024
Description: A fediverse client app/script
"""


from dataclasses import dataclass


@dataclass
class Client:
    """
    Client

    Attr:
        api_token (str): Token
        username (str): Username
        login (str): Login
        password (str): Password
    """

    api_token: str = ""
    username: str = ""
    login : str = ""
    password = ""
