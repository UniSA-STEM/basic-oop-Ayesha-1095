"""
File: Hacker.py
Description: Defines the Hacker class, representing a cyberpunk hacker who can acquire rigs, manage assets, launch attacks, encrypt/decrypt items, and track trace levels.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    """
    Represents a hacker in the digital underworld who begins with one CryptoToken, no rig,
    and a trace level of 0. Hackers can acquire rigs, launch data spikes, encrypt or decrypt
    assets, transfer items, and upgrade rigs. Performing risky actions increases the trace level,
    and exceeding a threshold may restrict certain abilities.

    Attributes:
        __name (str): The hacker's name.
        __inventory (list): A list of digital assets the hacker owns.
        __rig (Rig): The hacker's associated rig, which can be upgraded.
        __trace_level (int): The hacker's exposure level to being traced.
    """

    def __init__(self, name: str, rig=None) -> None:
        """
        Initializes a Hacker object with a name, one CryptoToken in inventory,
        no rig by default, and a trace level of 0.

        Args:
            name (str): The hacker's chosen name.
            rig (Rig): The hacker's rig, if they already have one. Default is None.
        """
        self.__name = name
        self.__inventory = [
            Asset('CryptoToken', 'Used to acquire or repair rigs.')
        ]  # Hacker starts with one CryptoToken in their inventory
        self.__rig = rig  # Initially, the hacker has no rig (None)
        self.__trace_level = 0  # Starts at 0

    # ===================================== Getter methods ================================================
    def get_name(self) -> str:
        return self.__name

    def get_inventory(self) -> list:
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self) -> int:
        return self.__trace_level

    # ==================================== Properties ======================================================
    name = property(get_name)
    inventory = property(get_inventory)
    rig = property(get_rig)
    trace_level = property(get_trace_level)

    # ==================================== Methods ==========================================================
    def acquire_a_rig(self, rig: Rig = None) -> None:
        """
        This method allows the hacker to get a rig, which costs one CryptoToken.
        If the acquisition is successful, it will display a message announcing the rig's activation.
        """
        # If hacker already has a rig, display a message
        if self.__rig:
            print('Already have a rig')
        else:
            # Check for CrytoToken in inventory
            crypto_token = None
            for asset in self.__inventory:
                if isinstance(asset, Asset) and asset.name == 'CryptoToken':
                    crypto_token = asset
            # Check if CryptoToken was found
            if crypto_token is None:
                print('No CryptoToken found in the inventory')
            else:
                # If found remove it from inventory
                self.__inventory.remove(crypto_token)
                # If no rig provided or wrong type, create default rig
                if not isinstance(rig, Rig):
                    rig = Rig(self.__name + '-Rig')  # Create default rig if none provided
                # Assign rig to hacker
                self.__rig = rig
                print('Rig activated: ' + rig.get_name())
