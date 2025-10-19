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
        encrypted (bool): True if the asset is encrypted, False otherwise.
    """

    def __init__(self, name: str, description: str, encrypted: bool = False) -> None:
        """
        Initialize an Asset object with its name and description, and encryption status.

        Args:
            name (str): The name of the asset.
            description (str): A short explanation of what the asset does.
            encrypted (bool): The initial encryption status. Default is False.
        """
        self.__name = name
        self.__description = description
        # Calls __set_encrypted
        self.encrypted = encrypted  # False by default (not encrypted)

    # ============================= Private Getter methods ===========================================
    def __get_name(self):
        """Returns the name of the asset."""
        return self.__name

    def __get_description(self):
        """Returns the description of the asset."""
        return self.__description

    def __get_encrypted(self):
        """Returns the encryption status of the asset."""
        return self.__encrypted

    # =========================== Private Setter Methods ==========================================
    def __set_encrypted(self, encrypt: bool) -> None:
        """
        Sets the encryption state of the asset.

        Args:
            encrypt (bool): The new encryption state (True for encrypted, False for decrypted).

        Returns:
            None: Prints an error if validation fails.
        """
        # Validate if the input is a boolean
        if isinstance(encrypt, bool):
            self.__encrypted = encrypt
        else:
            print('Error: The encryption must be a boolean (True/False).')

    # ============================= Properties ==============================================
    # Used properties to manage these attributes, keeping the data safe and controlled
    name = property(__get_name)
    description = property(__get_description)
    encrypted = property(__get_encrypted, __set_encrypted)

    def __str__(self):
        """
        Provide a formatted string of the asset.

        If the asset is encrypted, show [Encrypted] at the end of the string.

        Returns:
            str: The formatted string of the asset's name, description, and encryption status.
        """
        # Check if the asset is encrypted
        if self.encrypted:
            # Return name, description, and [Encrypted] label
            return f'{self.name}: {self.description} [Encrypted]'
        else:
            # Return just name and description, if not encrypted
            return f'{self.name}: {self.description}'

    def __eq__(self, other):
        """
        Compare this Asset with another object for equality.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if 'other' is an Asset with the same name and description, False otherwise.
        """
        # Compare if 'other' is also an Asset instance
        if isinstance(other, Asset):
            # Compare name and description
            return self.name == other.name and self.description == other.description
