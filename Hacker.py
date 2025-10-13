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
        name (str): The hacker's name.
        inventory (list): A list of digital assets the hacker owns.
        rig (Rig): The hacker's associated rig, which can be upgraded.
        trace_level (int): The hacker's exposure level to being traced.
    """

    def __init__(self, name, rig=None):
        """
        Initializes a Hacker object with a name, one CryptoToken in inventory,
        no rig by default, and a trace level of 0.

        Args:
            name (str): The hacker's chosen name.
            rig (Rig): The hacker's rig, if they already have one. Default is None.
        """
        self.name = name
        self.inventory = ['CryptoToken']  # Hacker starts with one CryptoToken in their inventory
        self.rig = rig  # Initially, the hacker has no rig (None)
        self.trace_level = 0  # Starts at 0
