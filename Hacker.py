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
        Acquire a rig by taking one CryptoToken from the hacker's inventory.

        If a rig object is passed in it will be used, otherwise a default Rig is created
        with the hacker's name. If the hacker already has a rig, the method prints a
        message and does nothing. On successful acquisition the method removes one
        CryptoToken from inventory, assigns the rig to the hacker, and prints a
        confirmation message.

        Args:
            rig (Rig): The hacker's rig, if they already have one. Default is None.
        """
        # If hacker already has a rig, display a message
        if self.__rig:
            print('Already have a rig')
        else:
            # Check for CryptoToken in inventory
            crypto_token = None
            found = False  # Flag to stop searching once a CryptoToken is found
            for asset in self.__inventory:
                # Only check until we find the first CryptoToken
                if not found and isinstance(asset, Asset) and asset.name == 'CryptoToken':
                    crypto_token = asset  # Store the found CryptoToken
                    found = True  # Set flag to True to prevent checking further assets
            # Check if CryptoToken is found, print a message
            if crypto_token is None:
                print('No CryptoToken found in the inventory')
            else:
                # If found remove it from inventory
                self.__inventory.remove(crypto_token)
                # If no rig provided or wrong type, create default rig
                if not isinstance(rig, Rig):
                    rig = Rig(self.__name + '-Rig')  # Create default rig if none provided
                # Assign rig to hacker to the hacker and confirm with message
                self.__rig = rig
                print('Rig activated: ' + rig.name)

    def launch_data_spike(self, target_rig):
        """
        Launch a data spike at a target rig.

        Consume one Data Spike from the hacker's rig storage and apply a hit to the
        target rig (calls target_rig.take_hit()). Each hit increases the target's
        damage. If the target becomes broken, print a message telling the hacker they
        can extract unsecured assets (extraction is a separate method).

        Args:
            target_rig (Rig): The hacker's rig, if they already have one.
        """
        # Check if the hacker has a rig. If not, return a message
        if not self.__rig:
            return 'No rig to launch attack!'

        # Check if the target is a rig. If not, return a message
        if not isinstance(target_rig, Rig):
            return 'Invalid target rig!'

        # Check the trace level. If it higher than the threshold, return a message
        if self.__trace_level > 5:
            return 'Trace level too high, cannot launch attack until reduce.'

        # Find a Data Spike in attacker's rig storage
        data_spike = None
        found = False  # Flag to stop searching once a CryptoToken is found
        for asset in self.__rig.storage:
            if not found and isinstance(asset, Asset) and asset.name == 'Data Spike':
                data_spike = asset  # Store the found Data Spike
                found = True  # Set flag to True to prevent checking further assets

        # If there is no Data Spike, return a message
        if data_spike is None:
            return 'No Data Spike in the rig\'s storage!'

        # Consume the Data Spike and perform attack
        self.__rig.storage.remove(data_spike)
        print('Data Spike launched at', target_rig.name)
        # Call take_hit() from Rig's class
        target_rig.take_hit()
        # Increase trace level and display it
        self.__trace_level += 1
        print('Trace level increased to', self.__trace_level)
        # If taget broken, display a message to inform hacker
        if target_rig.broken_state:
            print(f'Target rig {target_rig.name} is broken - you can extract unsecured assets using a Removable Drive.')

    def extract_unsecured_assets(self, target_rig):
        pass

    def encrypt_asset(self):
        pass

    def decrypt_asset(self):
        pass

    def store_asset(self):
        pass

    def retrieve_asset(self):
        pass

    def scan_inventory(self):
        pass

    def __str__(self):
        pass
