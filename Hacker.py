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
            return f'No {token_name} found in the inventory.\n'

        # If found remove it from inventory
        self.inventory.remove(crypto_token)

        # Create a default rig if none was provided
        if not isinstance(rig, Rig):
            rig = Rig(self.name + '-Rig')  # Create default rig if none provided

        # Assign rig to the hacker and confirm with message
        self.rig = rig
        return f'Rig activated: {self.rig.name}. \n{token_name} consumed from inventory.'

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
            return 'Trace level too high, cannot attack.'

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
            return f'!!!No {spike_name} in the rig storage!!!\n'

        # Consume the Data Spike and perform attack
        self.rig.storage.remove(data_spike)
        # Call take_hit() from Rig's class
        target_rig.take_hit()
        # Increase trace level and display it
        self.trace_level += 1

        # Combine into a short formatted message
        msg = [f"- Data Spike launched at {target_rig.name}",
               f"- Trace level: {self.trace_level}",
               f"- Target Rig: {target_rig.get_condition()}"]

        if target_rig.broken_state:
            msg.append("! Target rig broken — extraction possible with a Removable Drive")

        return "\n".join(msg)

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
                removable_drive = asset  # Store the actual Asset object.
                found = True  # Set flag to True to prevent checking further
        # ---------------------------------------------

        # If no removable drive in attacker rig, cannot extract
        if removable_drive is None:
            return f'!!!No {drive_name} available!!!'  # Return a message

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
            extracted_assets_names.append(asset.name)

        # Increase trace level by 1 and inform
        self.trace_level += 1
        return (f'Removable drive consumed for extraction.\n'
                f'Extracted assets: {extracted_assets_names}.\n'
                f'Trace level increased to {self.trace_level}.')

    def encrypt_asset(self, target_asset: Asset) -> str:
        """
        Encrypts a specified asset using a Security Chip from the rig's storage.

        The asset must be unencrypted and can be located in either the hacker's
        inventory or the rig's storage. A Security Chip is required from the rig's
        storage for the operation.

        Args:
            target_asset (Asset): The asset object in the hacker's inventory to encrypt.

        Returns:
            str: A message describing the outcome.
        """
        # Validate if the target asset is an Asset instance, if not show a message.
        if not isinstance(target_asset, Asset):
            return 'Error: Invalid asset type!'

        # Check if the target asset is encrypted, if yes show a message.
        if target_asset.encrypted is True:
            return f'{target_asset.name} is already encrypted!'

        # Check if no active rig is found, show a message.
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
                security_chip = asset  # Store the actual Asset object.
                found = True  # Set flag to True to prevent checking further
        # ---------------------------------------------

        #  If no Security Chip found, show an error message
        if security_chip is None:
            return f'Error: {chip_name} not found in rig storage.\n'
        # Consume the Security Chip
        self.rig.storage.remove(security_chip)

        # Change the asset's state to True
        target_asset.encrypted = True

        # Return Success output
        return f'{target_asset.name} is  successfully encrypted. {chip_name} is consumed.'

    def decrypt_asset(self, target_asset: Asset) -> str:
        """
        Decrypts a specified asset by consuming a Security Chip.

        The asset must be encrypted and can be located in either the hacker's
        inventory or the rig's storage. A Security Chip is required from the rig's
        storage for the operation.

        Args:
            target_asset (Asset): The asset object to decrypt.

        Returns:
            str: A message describing the outcome.
        """
        # Validate if the target asset is an Asset instance, if not show a message.
        if not isinstance(target_asset, Asset):
            return 'Error: Invalid asset type!'

        # Check if the target asset is encrypted, if not yes show a message.
        if target_asset.encrypted is False:
            return f'{target_asset.name} is already decrypted!'

        # Check if no active rig is found, show a message.
        if self.rig is None:
            return 'Error: Cannot decrypt without an active rig.'

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
                security_chip = asset  # Store the actual Asset object.
                found = True  # Set flag to True to prevent checking further
        # ---------------------------------------------

        #  If no Security Chip found, show an error message
        if security_chip is None:
            return f'Error: {chip_name} not found in rig storage.\n'
        # Consume the Security Chip
        self.rig.storage.remove(security_chip)

        # Change the asset's state to True
        target_asset.encrypted = False

        # Return success output
        return f'{target_asset.name} is successfully decrypted. {chip_name} consumed.'

    def upgrade_hacker_rig(self) -> str:
        """
        Upgrades the hacker's active rig by consuming a Hardware Patch from inventory.

        This increases the rig's upgrade level, improving storage size and defense.

        Returns:
            str: A message describing the outcome.
        """
        # Check if no active rig is found, show a message.
        if self.rig is None:
            return 'Error: Cannot upgrade without a rig!'

        # --- Flag based Search for Security Chip ---
        # Find a Hardware Patch in the hacker's rig storage
        patch_name = 'Hardware Patch'  # Use a separate string variable for the name
        hardware_patch = None  # This variable will store the Asset object
        found = False  # Flag to stop searching once a Hardware Patch is found

        for asset in self.inventory:
            # stop after first Hardware Patch found using flag
            if not found and isinstance(asset, Asset) and asset.name == patch_name:
                hardware_patch = asset  # Store the actual Asset object.
                found = True  # Set flag to True to prevent checking further
        # ---------------------------------------------
        # Check if the patch isn't in the hacker's inventory
        if hardware_patch is None:
            return f'Error: {patch_name} not found in inventory.\n'

        # Consume the Hardware Patch from the inventory
        self.inventory.remove(hardware_patch)

        # Increase the rig upgrade level by calling the method from rig's class
        self.rig.upgrade_rig()
        return f'{patch_name} consumed from inventory.\n'

    def store_asset(self, target_asset: Asset) -> str:
        """
        Transfers a specific asset from the hacker's inventory to the rig's storage.

        Encrypted assets cannot be transferred. Requires an active rig.

        Args:
            target_asset (Asset): The asset object to store.

        Returns:
            str: A message describing the outcome.
        """
        # Validate if target asset is an instance of Asset, if not return an error
        if not isinstance(target_asset, Asset):
            return 'Error: Invalid asset type!'

        # Check if no active rig is found, show a message.
        if self.rig is None:
            return 'Error: Cannot store without a rig!'

        # Check if assets are encrypted, if yes, it cannot be transferred
        if target_asset.encrypted is True:
            return f'{target_asset.name} is encrypted and cannot be transferred'

        # Check if asset is not in the inventory, and return a message
        if target_asset not in self.inventory:
            return f'{target_asset.name} is not found in inventory.'

        # Remove the asset from the inventory and store it in the storage
        self.inventory.remove(target_asset)
        self.rig.storage.append(target_asset)

        # Return success message
        return f'{target_asset.name} successfully moved to rig storage.'

    def retrieve_asset(self, target_asset: Asset) -> str:
        """
        Transfers a specific asset from the rig's storage to the hacker's inventory.

        Encrypted assets cannot be transferred. Requires an active rig.

        Args:
            target_asset (Asset): The asset object to retrieve.

        Returns:
            str: A message describing the outcome.
        """
        # Validate if target asset is an instance of Asset, if not return an error
        if not isinstance(target_asset, Asset):
            return 'Error: Invalid asset type!'

        # Check if no active rig is found, show a message.
        if self.rig is None:
            return 'Error: Cannot store without a rig!'

        # Check if assets are encrypted, if yes, it cannot be stored
        if target_asset.encrypted is True:
            return f'{target_asset.name} is encrypted and cannot be transferred.'

        # Check if asset is not in the storage, and return a message
        if target_asset not in self.rig.storage:
            return f'{target_asset.name} is not found in rig storage.'

        # Remove the asset from the rig storage and add it to the inventory
        self.rig.storage.remove(target_asset)
        self.inventory.append(target_asset)

        # Return success message
        return f'{target_asset.name} is successfully moved to inventory.'

    def scan_inventory(self, asset_name: str) -> Asset:
        """
        Scans the hacker's inventory for an asset by name.
        If found, the asset is removed from inventory and returned.

        Args:
            asset_name (str): The name of the asset to search for.

        Returns:
            Asset/None: The found Asset object, or None if not found.
        """
        # Validate if input is a non-empty string
        if not isinstance(asset_name, str) or not asset_name:
            print('Error: Invalid or empty asset name!')
            return None

        # Variable to hold the Asset object if found. Starts as None
        asset_to_remove = None
        # Flag to control the search loop.
        found = False

        # Look for the Asset by name in the inventory
        for asset in self.inventory:
            # Check if the asset is not found yet and the currect asset matched the name
            if not found and asset.name == asset_name:
                asset_to_remove = asset  # Store the actual Asset object
                found = True  # Set flag to True to prevent checking further
        # ---------------------------------------------

        # Check if an asset object was successfully stored.
        if asset_to_remove is not None:
            # Remove the found Asset object from the inventory.
            self.inventory.remove(asset_to_remove)
            # Return the Asset object itself.
            return asset_to_remove

        # If the asset was not found after the loop completes, return None.
        return None

    def __str__(self):
        """
        Returns a comprehensive string representation of the Hacker object.

        The output includes the hacker's name, current trace level, the status
        and contents of the active rig, and the items held in the inventory.

        Returns:
            str: A formatted string detailing the hacker's current state.
        """
        # --- Define Basic Hacker Info ---
        display_string = 'Hacker Name: ' + self.name + '\n'
        # Convert int to str for display!
        display_string += 'Trace Level: ' + str(self.trace_level) + '\n'

        # --- Define Rig Status ---
        display_string += '\n===== Rig Status =====\n'

        # Check if an active rig is present
        if self.rig is not None:
            display_string += 'Active Rig: ' + self.rig.name + '\n'
            # Display the rig's upgrade level, converting the integer to a string.
            display_string += 'Upgrade Level: ' + str(self.rig.upgrade_level) + '\n'
            display_string += '\n===== Rig Storage =====\n'

            # Check if the list is empty
            if not self.rig.storage:
                display_string += '(Storage is Empty)\n'
            else:
                # Loop over the storage list to list each asset
                for asset in self.rig.storage:
                    # Display the asset name and its encryption status (converting boolean to string)
                    display_string += '-' + asset.name + ' (Encrypted: ' + str(asset.encrypted) + ')\n'
        else:
            # Message if no rig is active
            display_string += ('Active Rig: None (Acquire one to gain storage)\n')

        # --- Define Inventory Contents ---
        display_string += '\n====== Inventory =====\n'

        # Check if the list is empty
        if not self.inventory:
            display_string += '(Inventory is Empty)\n'
        else:
            # Loop over the inventory list to list assets
            for asset in self.inventory:
                # Display the asset name and its encryption status.
                display_string += '-' + asset.name + ' (Encrypted: ' + str(asset.encrypted) + ')\n'

        # --- Return the Final String ---
        return display_string
