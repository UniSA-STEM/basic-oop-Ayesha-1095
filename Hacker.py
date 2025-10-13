"""
File: Hacker.py
Description: Defines the Hacker class, representing a cyberpunk hacker who can acquire rigs, manage assets, launch attacks, encrypt/decrypt items, and track trace levels.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Misconduct Policy.
"""


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

    def __init__(self, name, rig=None):
        """
        Initializes a Hacker object with a name, one CryptoToken in inventory,
        no rig by default, and a trace level of 0.

        Args:
            name (str): The hacker's chosen name.
            rig (Rig): The hacker's rig, if they already have one. Default is None.
        """
        self.__name = name
        self.__inventory = ['CryptoToken']  # Hacker starts with one CryptoToken in their inventory
        self.__rig = rig  # Initially, the hacker has no rig (None)
        self.__trace_level = 0  # Starts at 0

    # ===================================== Getter methods ================================================
    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_trace_level(self):
        return self.__trace_level

    # ==================================== Properties ======================================================
    name = property(get_name)
    inventory = property(get_inventory)
    rig = property(get_rig)
    trace_level = property(get_trace_level)

    # ==================================== Methods ==========================================================
    def acquire_a_rig(self, rig=None):
        """
        This method allows the hacker to get a rig, which costs one CryptoToken.
        If the acquisition is successful, it will display a message announcing the rig's activation.
        """
        # If hacker already has a rig, display a message
        if self.__rig:
            print('Already have a rig')

        # If a CryptoToken exists in inventory, use it to acquire the rig
        elif 'CryptoToken' in self.__inventory:
            self.__inventory.remove('CryptoToken')  # Remove one CryptoToken
            self.__rig = rig  # Assign the passed in rig (or None if not provided)
            print('Rig activated')

        # If no CryptoToken is found, display a message
        else:
            print('No CryptoToken in the inventory')
