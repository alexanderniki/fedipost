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

    # FILES

    def listdir(self, directory_path: str) -> List[str]:
        """
        Get a list of files in the directory

        Args:
            directory_path (str): Path to directory

        Returns:
            List[str]: A list of files in given directory
        """
        ...

    def create_file(self, filename_path: str) -> None:
        ...

    def rename_file(self, filename_path: str, filename_path_new: str) -> str:
        ...

    # DIRECTORIES

    def create_directory(self, directory_path: str) -> None:
        ...

    def rename_directory(self, directory_path: str, directory_path_new: str) -> str:
        ...

    def get_home_directory(self) -> str:
        ...

    def get_current_directory(self) -> str:
        ...
