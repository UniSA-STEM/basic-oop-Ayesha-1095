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

    Class Attributes:
        TRACE_THRESHOLD (int): The maximum trace level before restrictions apply (5).

    Attributes:
        __name (str): The hacker's name.
        __inventory (list): A list of digital assets the hacker owns.
        __rig (Rig): The hacker's associated rig, which can be upgraded.
        __trace_level (int): The hacker's exposure level to being traced.
    """
    # ================================== Class Level Attributes ==========================================
    TRACE_THRESHOLD = 5

    # ===================================== Initialization ================================================
    def __init__(self, name: str, rig=None) -> None:
        """
        Initializes a Hacker object with a name, one CryptoToken in inventory,
        no rig by default, and a trace level of 0.

        Args:
            name (str): The hacker's chosen name.
            rig (Rig): The hacker's rig, if they already have one. Default is None.
        """
        # Assign attributes using public properties, which call the private setters
        self.name = name
        self.rig = rig

        # Initialize inventory with a starting asset
        self.__inventory = [
            Asset('CryptoToken', 'Used to acquire or repair rigs.')
        ]

        # Initialize trace level using the property setter
        self.trace_level = 0

    # ===================================== Private Getter methods ================================================
    # These methods are private and accessed only via the public properties.
    def __get_name(self) -> str:
        """Returns the hacker's chosen name."""
        return self.__name

    def __get_inventory(self) -> list:
        """Returns the hacker's inventory."""
        return self.__inventory

    def __get_rig(self):
        """Returns the hacker's associated rig."""
        return self.__rig

    def __get_trace_level(self) -> int:
        """Returns the hacker's exposure level to being traced."""
        return self.__trace_level

    # ===================================== Private Setter methods ================================================
    # These methods are private and accessed only via the public properties.
    def __set_name(self, name: str) -> None:
        """
        Sets the hacker's name.

        Args:
        name (str): The new name for the hacker.

        Returns:
            None: Prints an error message if not valid.
        """
        # Validate if the input is a string and non-empty
        if isinstance(name, str) and name:
            self.__name = name
        else:
            # Print error message
            print('Error: The name must be a non-empty string!')

    def __set_rig(self, rig: Rig) -> None:
        """
        Sets the hacker's rig.

        Args:
            rig (Rig / None): The new Rig object to associate with the hacker, or None.

        Returns:
            None: Prints an error message if not valid.
        """
        # Validates if the rig is  either None or an instance of the Rig class
        if rig is None or isinstance(rig, Rig):
            self.__rig = rig
        else:
            # Print error message as requested
            print('Error: Rig must be a Rig object or None.')

    def __set_trace_level(self, level: int) -> None:
        """
        Sets the hacker's trace level.

        Args:
        level (int): The new trace level (must be non-negative).

        Returns:
        None: Prints an error message if not valid.
        """
        # Validate the type and ensures the level is not negative
        if isinstance(level, int) and level >= 0:
            self.__trace_level = level
        else:
            # Print error message
            print('Error: Trace level must be a non-negative integer!')

    # ==================================== Properties ======================================================
    # Properties provide the public interface for attribute accessed
    name = property(__get_name, __set_name)
    inventory = property(__get_inventory)  # Read only, as list manipulation is done via list methods
    rig = property(__get_rig, __set_rig)
    trace_level = property(__get_trace_level, __set_trace_level)

    # ==================================== Methods ==========================================================
    def acquire_a_rig(self, rig: Rig = None) -> str:
        """
        Acquire a rig by taking one CryptoToken from the hacker's inventory.

        If a rig object is passed in it will be used, otherwise a default Rig is created
        with the hacker's name. If the hacker already has a rig, the method prints a
        message and does nothing. On successful acquisition the method removes one
        CryptoToken from inventory, assigns the rig to the hacker, and prints a
        confirmation message.

        Args:
            rig (Rig): The hacker's rig, if they already have one. Default is None.

         Returns:
            str: A message describing the outcome of the acquisition.
        """
        # If hacker already has a rig, display a message
        if self.rig:
            return 'Already have a rig.'

        # --- Flag based Search for CryptoToken ---
        # Search for CryptoToken in inventory
        token_name = 'CryptoToken'  # Use a local variable to name the asset being searched for
        crypto_token = None
        found = False  # Flag to stop searching once a CryptoToken is found
        for asset in self.inventory:
            # Only check until we find the first CryptoToken
            if not found and isinstance(asset, Asset) and asset.name == token_name:
                crypto_token = asset  # Store the found CryptoToken
                found = True  # Set flag to True to prevent checking further assets
        # -----------------------------------------

        # Check if CryptoToken is found, print a message
        if crypto_token is None:
            return f'No {token_name} found in the inventory.'

        # If found remove it from inventory
        self.inventory.remove(crypto_token)

        # Create a default rig if none was provided
        if not isinstance(rig, Rig):
            rig = Rig(self.name + '-Rig')  # Create default rig if none provided

        # Assign rig to the hacker and confirm with message
        self.rig = rig
        return f'Rig activated: {self.rig.name}. {token_name} consumed from inventory.'

    def launch_data_spike(self, target_rig: Rig) -> str:
        """
        Launch a data spike at a target rig.

        Consume one Data Spike from the hacker's rig storage and apply a hit to the
        target rig (calls target_rig.take_hit()). Each hit increases the target's
        damage. If the target becomes broken, print a message telling the hacker they
        can extract unsecured assets (extraction is a separate method).

        Args:
            target_rig (Rig): The hacker's rig, if they already have one.

        Returns:
            str: error message on failure, or a success message on success.
        """
        # Check if the hacker has a rig. If not, return a message
        if not self.rig:
            return 'No rig to launch attack!'

        # Check if the target is a rig. If not, return a message
        if not isinstance(target_rig, Rig):
            return 'Invalid target rig!'

        # Check the trace level. If it higher than the threshold, return a message
        if self.trace_level > Hacker.TRACE_THRESHOLD:
            return 'Trace level too high, cannot launch attack until reduce.'

        # --- Flag based Search for Data Spike ---
        # Find a Data Spike in attacker's rig storage
        spike_name = 'Data Spike'  # Use a local variable to name the asset being searched for
        data_spike = None
        found = False  # Flag to stop searching once a CryptoToken is found
        for asset in self.rig.storage:
            if not found and isinstance(asset, Asset) and asset.name == spike_name:
                data_spike = asset  # Store the found Data Spike
                found = True  # Set flag to True to prevent checking further assets
        # ----------------------------------------

        # If there is no Data Spike, return a message
        if data_spike is None:
            return f'No {spike_name} in the rig\'s storage!'

        # Consume the Data Spike and perform attack
        self.rig.storage.remove(data_spike)
        # Call take_hit() from Rig's class
        target_rig.take_hit()
        # Increase trace level and display it
        self.trace_level += 1

        # Return a clear message describing the result
        if target_rig.broken_state:
            return (f'Data Spike launched at {target_rig.name}.\n'
                    f'Trace level increased to {self.trace_level}.\n'
                    f'Target rig {target_rig.name} is broken — you can extract unsecured assets using a Removable Drive.\n')
        else:
            return f'Data Spike launched at {target_rig.name}. Trace level increased to {self.trace_level}.\n'

    def extract_unsecured_assets(self, target_rig: Rig) -> str:
        """
        Extract unencrypted assets from a broken target rig using a Removable Drive.

        The hacker must have a rig (to provide the Removable Drive). The target rig must be
        broken. A Removable Drive is consumed from the hacker's rig storage and then all
        unencrypted assets are moved from the target rig's storage to the hacker's inventory.
        Trace level is increased by 1 for the risky extraction.

        Args:
            target_rig (Rig): The rig to extract from.

        Returns:
            str: error message on failure, or a success message listing extracted assets.
        """
        # Check if the hacker does not have a rig
        if not self.rig:
            return 'No rig to extract unsecured assets!'  # Return a message

        # Check if target rig is a Rig instance
        if not isinstance(target_rig, Rig):
            return 'Invalid target rig!'  # Return a message

        # Target rig must be broken to allow extraction
        if not target_rig.broken_state:
            # Return a message
            return f'Target rig {target_rig.name} is not broken! - cannot extract.'

        # --- Flag-Based Search for Removable Drive ---
        # Find a Removable Drive in the hacker's rig storage
        drive_name = 'Removable Drive'  # Use a local variable to name the asset being searched for
        removable_drive = None
        # Flag to stop searching once a Removable Drive is found
        found = False
        for asset in self.__rig.storage:
            # stop after first removable drive found using flag
            if not found and isinstance(asset, Asset) and asset.name == drive_name:
                removable_drive = asset
                found = True
        # ---------------------------------------------

        # If no removable drive in attacker rig, cannot extract
        if removable_drive is None:
            return f'No {drive_name} available!'  # Return a message

        # Remove Removable Drive
        self.rig.storage.remove(removable_drive)

        # Collect unencrypted assets from the target rig
        transfer_assets = []
        for asset in target_rig.storage:
            if isinstance(asset, Asset) and not asset.encrypted:
                transfer_assets.append(asset)

        # If nothing to extract, increase trace and report that the drive was consumed
        if not transfer_assets:
            self.trace_level += 1
            return (f'Removable drive consumed for extraction.\n'
                    f'No unencrypted assets found for extraction from {target_rig.name}.\n'
                    f'Trace level increased to {self.trace_level}.')

        # Move all unencrypted assets to the hacker's inventory
        extracted_assets_names = []
        for asset in transfer_assets:
            # Move the asset by removing it from target storage and appending to hacker inventory
            target_rig.storage.remove(asset)
            self.inventory.append(asset)
            extracted_assets_names.append(asset)

        # Increase trace level by 1 and inform
        self.trace_level += 1
        return (f'Removable drive consumed for extraction.\n'
                f'Extracted assets: {extracted_assets_names}.\n'
                f'Trace level increased to {self.trace_level}.')

    def encrypt_asset(self, target_asset: Asset) -> str:
        """
        Encrypts a specified asset using a Security Chip from the rig's storage.

        Args:
            target_asset (Asset): The asset object in the hacker's inventory to encrypt.

        Returns:
            str: A message describing the outcome (success or failure).
        """
        # Validate if the target asset is an Asset instance, if not show a message.
        if not isinstance(target_asset, Asset):
            return 'Error: Invalid asset type!'

        # Check if the target asset is encrypted, if yes show a message.
        if target_asset.encrypted is True:
            return f'{target_asset.name} is already encrypted!'

        # if no active rig is found, show a message.
        if self.rig is None:
            return 'Error: Cannot encrypt without an active rig.'

        # Check if the target asset is in either location.
        # If it's in neither, show an error.
        if target_asset not in self.inventory and target_asset not in self.rig.storage:
            return 'Error: Asset not found in inventory or rig storage!'

        # --- Flag based Search for Security Chip ---
        # Find a Security Chip in the hacker's rig storage
        chip_name = 'Security Chip'
        security_chip = None  # Use a local variable to name the asset being searched for
        found = False  # Flag to stop searching once a Security Chip is found
        for asset in self.rig.storage:
            # stop after first Security Chip found using flag
            if not found and isinstance(asset, Asset) and asset.name == chip_name:
                security_chip = asset
                found = True
        # ---------------------------------------------

        #  If no Security Chip found, show an error message
        if security_chip is None:
            return f'Error: {chip_name} not found in rig storage.'
        # Consume the Security Chip
        self.rig.storage.remove(security_chip)

        # Change the asset's state to True
        target_asset.encrypted = True

        # Return Success output
        return f'{target_asset.name} is  successfully encrypted. Security Chip is consumed.'

    def decrypt_asset(self):
        pass

    def upgrade_hacker_rig(self):
        pass

    def store_asset(self):
        pass

    def retrieve_asset(self):
        pass

    def scan_inventory(self):
        pass

    def __str__(self):
        pass
