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
        name (str): The name of the asset.
        description (str): A short explanation of what the asset does.
        encrypted (bool): True if the asset is encrypted, False otherwise.
    """

    def __init__(self, name, description, encrypted=False):
        """
        Initialize an Asset object with its name and description, and encryption status.
        """
        self.name = name
        self.description = description
        self.encrypted = encrypted  # False by default (not encrypted)
