"""
File: Asset.py
Description: This module defines the Asset class, which represents digital assets such as
CryptoToken, Data Spike, and Security Chip that can be used, stored, or transferred
between hackers and rigs.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    """
    Represent a digital asset, such as CryptoToken, Data Spike, or Security Chip.
    Attributes:
        __name (str): The name of the asset.
        __description (str): A short explanation of what the asset does.
        __encrypted (bool): True if the asset is encrypted, False otherwise.
    """

    def __init__(self, name, description, encrypted=False):
        """
        Initialize an Asset object with its name and description, and encryption status.
        """
        self.__name = name
        self.__description = description
        self.__encrypted = encrypted  # False by default (not encrypted)

    # ============================= Getter methods ===========================================
    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    # ============================= Properties ==============================================
    name = property(get_name)
    description = property(get_description)
    encrypted = property(get_encrypted)
