"""
File: Rig.py
Description: This module defines the Rig class representing a computer rig that can store assets, take damage, be repaired, and upgraded.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

from Asset import Asset
from Hacker import Hacker


class Rig:
    """
    Represents a computer rig in the digital underworld.

    A rig has a name, storage for assets, a damage counter, a broken state,
    and an upgrade level. Rigs can be repaired, upgraded, take hits in battles,
    and store or release assets.

    Attributes:
        __name (str): The name of the rig.
        __storage (list): The assets stored in this rig.
        __damage_counter (int): The number of hits the rig has taken.
        __broken_state (bool): True if the rig is broken, False otherwise.
        __upgrade_level (int): The upgrade level applied to the rig.
    """

    def __init__(self, name, damage_counter=0, broken_state=False, upgrade_level=0):
        """
        Initialize a Rig object with its name, storage, damage counter,
        broken state, and upgrade level.
        """
        self.__name = name
        self.__storage = [
            Asset('Data Spike', 'Used in battles'),
            Asset('Data Spike', 'Used in battles'),
            Asset('Removable Drive', 'Used for extraction of assets')
        ]  # Starting assets
        self.__damage_counter = damage_counter  # Tracks rig damage
        self.__broken_state = broken_state  # True if broken
        self.__upgrade_level = upgrade_level  # Upgrade level of rig

    # ======================= Getter methods ===============================================
    def get_name(self):
        return self.__name

    def get_storage(self):
        return self.__storage

    def get_damage_counter(self):
        return self.__damage_counter

    def get_broken_state(self):
        return self.__broken_state

    def get_upgrade_level(self):
        return self.__upgrade_level

    # ============================ Properties ===============================================
    name = property(get_name)
    storage = property(get_storage)
    damage_counter = property(get_damage_counter)
    broken_state = property(get_broken_state)
    upgrade_level = property(get_upgrade_level)

    # ============================= Methods ==================================================
    def repair_damage(self):
        """
        Repairs the rig if it has any damage.
        Reset damage_counter to 0 and broken_state to False.
        If rig is not damaged, display a message.
        """
        # Check if damage is greater than 0
        if self.__damage_counter > 0:
            self.__damage_counter = 0  # Reset damage_counter to 0
            self.__broken_state = False  # Set broken_state to False
            print(f'{self.__name} repaired successfully.')
        else:
            print('No repair needed')  # Display a message if not damaged

    def upgrade_rig(self):
        """
        Increases the rig's upgrade level when a Hardware Patch is used.
        Upgrading affects how much damage the rig can take in battles
        and the amount of assets it can store.
        """
        self.__upgrade_level += 1  # Increase the upgrade level by 1
        print(f'{self.__name} upgraded to level {self.__upgrade_level}')  # Show the new level

    def take_hit(self):
        """
        Each hit increases damage by 1.
        The number of hits a rig can take before breaking depends on its upgrade level.
         For example:
            Level 0 = breaks after 2 hits
            Level 1 = breaks after 3 hits
            Level 2 = breaks after 4 hits, etc.
        """
        self.__damage_counter += 1  # Increase damage counter by 1
        max_hits = 2 + self.__upgrade_level  # Calculate limit based on level

        # Check if rig has taken enough damage to be broken
        if self.__damage_counter >= max_hits:
            self.__broken_state = True  # Set the rig as broken
            print(f'{self.__name} has been broken!')
        else:
            print(f'{self.__name} took a hit {self.__damage_counter}/{max_hits}')

    def generate_asset(self):
        """
        Generates a new asset randomly and adds it to the rig's storage.

        The rig does not control the type of asset generated.
        Every time this method is called, it will pick one asset randomly
        from the possible assets list and store it in the rig's storage.
        """
        # The list of possible Asset object the rig can generate
        possible_assets = [
            Asset('Data Spike', 'Used in battles'),
            Asset('Removable Drive', 'Used for extraction of assets'),
            Asset('Security Chip', 'Used to encrypt or decrypt assets')
        ]

        # Select randomly one asset from the possible assets list
        asset = random.choice(possible_assets)

        # Add the new asset to the rig's storage
        self.__storage.append(asset)

        # Print a message to confirm
        print(f'Rig generated asset: {asset.name}')

    def store_asset(self, hacker, asset):
        """
        Store an asset from the hacker's inventory into the rig.

        This method transfers a specified asset from a hacker's inventory to the rig's storage,
        but only if the asset is not encrypted. Encrypted assets cannot be stored until decrypted.

        Args:
            hacker (Hacker): The hacker who owns the asset.
            asset (Asset): The asset object to be transferred.
        """
        # Check if the hacker actually has this asset in their inventory
        if asset in hacker.inventory:
            # Only allow storing if the asset is not encrypted
            if not asset.encrypted:
                hacker.inventory.remove(asset)  # Remove asset from hacker inventory
                self.__storage.append(asset)  # Add asset to rig storage
                print(f'{asset.name} stored in rig!')
            else:
                # Display a message if asset is encrypted that it cannot be transferred
                print('Cannot store encrypted asset!')
        else:
            # Display a message if Hacker doesn't have this asset
            print(f'Hacker does not have {asset.name} asset!')

    def release_asset(self, hacker, asset):
        """
        Release an asset from the rig's storage to the hacker's inventory.

        This method transfers a specified asset from a rig's storage to a hacker's inventory
        but only if the asset is not encrypted. Encrypted assets cannot be released until decrypted.
        Args:
            hacker (Hacker): The hacker who will receive the asset.
            asset (Asset): The asset object to be transferred.
        """
        # Check if the asset exists in the rig's storage
        if asset in self.__storage:
            # Only allow releasing if the asset is not encrypted
            if not asset.encrypted:
                # Ensure the hacker does not already have this asset (avoid duplicates)
                if asset not in hacker.inventory:
                    self.__storage.remove(asset)  # Remove asset from rig storage
                    hacker.inventory.append(asset)  # Add asset to hacker inventory
                    print(f'{asset.name} released to hacker!')  # Confirm the transfer
                else:
                    # Display a message if hacker already has this asset
                    print(f'Hacker already has {asset.name} in inventory!')
            else:
                # Display message if asset is encrypted
                print('Cannot release encrypted asset!')
        else:
            # Display message if the rig does not have the asset
            print(f'Rig does not have {asset.name}!')

    def get_condition(self):
        """
        Returns the current condition of the rig as a descriptive string.

        The condition depends on the rig's damage counter and upgrade level:
        - Broken if the rig is flagged as broken or the damage counter exceeds its limit.
        - Pristine if the rig has no damage.
        - Damaged for any other case where some damage exists but the rig is still operational.

        Returns:
            str: A string representing the rig's condition with its upgrade level included.
        """
        # Maximum hits the rig can take before breaking, depends on upgrade level
        max_hits = 2 + self.__upgrade_level
        # Check if rig is broken or has reached/exceeded max hits
        if self.__broken_state or self.__damage_counter >= max_hits:
            return f'Broken (Level {self.__upgrade_level})'
        # Check if rig has no damage
        elif self.__damage_counter == 0:
            return f'Pristine (Level {self.__upgrade_level})'
        # Otherwise, rig has some damage but is still operational
        else:
            return f'Damaged (Level {self.__upgrade_level})'

    def __str__(self):
        """
        Returns a string representation of the rig, including its name,
        condition, upgrade level, and stored assets.
        Returns:
            str: A multi-line string describing the rig's status and contents.
        """
        # Create a list to store asset names
        asset_names = []

        # Loop through each asset in storage and get its name
        for asset in self.__storage:
            asset_names.append(asset.name)

        # Check if storage is empty
        if len(asset_names) == 0:
            asset_str = 'No assets available'
        else:
            # Join the names with commas for display
            asset_str = ', '.join(asset_names)

        # Return the formatting string
        return (
            f'Rig Name: {self.__name}\n'
            f'Condition: {self.get_condition()}\n'
            f'Upgrade Level: {self.__upgrade_level}\n'
            f'Stored Assets: {asset_str}\n'
        )
