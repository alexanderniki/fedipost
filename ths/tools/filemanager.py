"""
File: filemanager.py
Version: 0.1
Author: Aleksandr Nikiforov (Lonin)
Contact: https://alexanderniki.name
Date: Nov 23, 2024
Description: A tool for working with files
"""


import os
import random
from typing import List


class FileManager():
    """
    File manager
    """

    def __init__(self) -> None:
        pass

    def listdir(self, directory_path: str) -> List:
        ...

    def create_file(self, filename_path: str) -> None:
        ...

    def rename_file(self, filename_path: str, filename_path_new: str) -> str:
        ...
