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

    # ===================================== Initialization ============================================================
    def __init__(self, name: str, damage_counter: int = 0, broken_state: bool = False, upgrade_level: int = 0) -> None:
        """
        Initializes a Rig object.

        Initializes the rig with its name, starting assets in storage, damage,
        broken state, and upgrade level. All attributes are set via their properties.

        Args:
            name (str): The name of the rig.
            damage_counter (int): The initial damage taken by the rig. Default is 0.
            broken_state (bool): The initial broken status of the rig. Default is False.
            upgrade_level (int): The initial upgrade level of the rig. Default is 0.
        """
        # Assign attributes using property setters
        self.name = name
        # Initialize storage with starting assets
        self.__storage = [
            Asset('Data Spike', 'Used in battles'),
            Asset('Data Spike', 'Used in battles'),
            Asset('Removable Drive', 'Used for extraction of assets')
        ]  # Starting assets
        self.damage_counter = damage_counter  # Tracks rig damage
        self.broken_state = broken_state  # True if broken
        self.upgrade_level = upgrade_level  # Upgrade level of rig

    # ======================= Private Getter methods ===============================================
    # These methods are private and accessed only via the public properties.
    def __get_name(self) -> str:
        """Returns the name of the rig."""
        return self.__name

    def __get_storage(self) -> list:
        """Returns the list of assets stored in this rig."""
        return self.__storage

    def __get_damage_counter(self) -> int:
        """Returns the number of hits the rig has taken."""
        return self.__damage_counter

    def __get_broken_state(self) -> bool:
        """Returns the broken status of the rig (True if broken)."""
        return self.__broken_state

    def __get_upgrade_level(self) -> int:
        """Returns the upgrade level applied to the rig."""
        return self.__upgrade_level

    # =========================== Private Setter Methods ===========================================
    # These methods are private and accessed only via the public properties.
    def __set_name(self, name: str) -> None:
        """
        Sets the name of the rig.

        Args:
            name (str): The new name for the rig.

        Returns:
            None: Prints an error if not valid.
        """
        # Validate if the input is a string
        if isinstance(name, str) and name:
            self.__name = name
        else:
            print('Error: The name must be a non empty string!')

    def __set_damage_counter(self, damage_counter: int) -> None:
        """
        Sets the damage counter of the rig.

        Args:
            damage_counter (int): The new damage value (must be non-negative).

        Returns:
            None: Prints an error if not valid.
        """
        # Validate if the input is an integer and greater than 0
        if isinstance(damage_counter, int) and damage_counter >= 0:
            self.__damage_counter = damage_counter
        else:
            print('Error: The damage counter must be a non negative integer!')

    def __set_broken_state(self, state: bool) -> None:
        """
        Sets the broken state of the rig.

        Args:
            state (bool): The new broken state (True or False).

        Returns:
            None: Prints an error if not valid.
        """
        # Validate if the input is a boolean
        if isinstance(state, bool):
            self.__broken_state = state
        else:
            print('Error: The broken state must be a boolean (True/False).')

    def __set_upgrade_level(self, level: int) -> None:
        """
        Sets the upgrade level of the rig.

        Args:
            level (int): The new upgrade level (must be positive integer).

        Returns:
            None: Prints an error if not valid.
        """
        # Validate if the input is positive integer.
        if isinstance(level, int) and level >= 0:
            self.__upgrade_level = level
        else:
            print('Error: The upgrade level must be a non negative integer!')

    # ============================ Properties ===============================================
    # Properties provide the public interface to the private attributes
    name = property(__get_name, __set_name)
    storage = property(__get_storage, )  # Setter included for initial/full replacement use
    damage_counter = property(__get_damage_counter, __set_damage_counter)
    broken_state = property(__get_broken_state, __set_broken_state)
    upgrade_level = property(__get_upgrade_level, __set_upgrade_level)

    # ============================= Methods ==================================================
    def repair_damage(self) -> None:
        """
        Repairs the rig if it has any damage.

        Resets damage_counter to 0 and broken_state to False.
        If the rig is not damaged, it displays a message.

        Returns:
            None
        """
        #  Check damage OR broken state to ensure a full repair
        if self.damage_counter > 0 or self.broken_state:
            self.damage_counter = 0  # Reset damage_counter to 0
            self.broken_state = False  # Set broken_state to False
            print(f'{self.name} repaired successfully.')
        else:
            print('No repair needed')  # Display a message if not damaged

    def upgrade_rig(self) -> None:
        """
        Increases the rig's upgrade level.

        The upgrade level is increased by 1. This affects
        the maximum hits the rig can take before breaking (take_hit).

        Returns:
            None
        """
        self.upgrade_level += 1  # Increase the upgrade level by 1
        print(f'{self.name} upgraded to level {self.upgrade_level}')  # Show the new level

    def take_hit(self) -> None:
        """
        Increases the damage counter by 1 and checks if the rig is broken.

        The maximum hits is calculated as (2 + upgrade_level). If damage reaches or
        exceeds this limit, the broken_state is set to True.

        Returns:
            None
        """
        self.damage_counter += 1  # Increase damage counter by 1
        max_hits = 2 + self.upgrade_level  # Calculate limit based on level

        # Check if rig has taken enough damage to be broken
        if self.damage_counter >= max_hits:
            self.broken_state = True  # Set the rig as broken
            print(f'{self.name} has been broken!')
        else:
            print(f'{self.name} took a hit {self.damage_counter}/{max_hits}')

    def generate_asset(self) -> None:
        """
        Generates a new asset randomly and adds it to the rig's storage.

        A random Asset object is selected from a predefined list and appended to
        the rig's storage list.

        Returns:
            None
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
        self.storage.append(asset)

        # Print a message to confirm
        print(f'Rig generated asset: {asset.name}')

    def store_asset(self, hacker, asset: Asset) -> None:
        """
        Store an asset from the hacker's inventory into the rig.

        Validates the asset object, ensures it is in the hacker's inventory, and confirms
        it is not encrypted before transferring it to the rig's storage. Requires a Hacker
        object for access to inventory.

        Args:
            hacker: The hacker object who owns the asset.
            asset (Asset): The asset object to be transferred.
        Returns:
            None: Prints a message describing the outcome.
        """
        # Validate if asset is an instance of Asset
        if not isinstance(asset, Asset):
            print(f'Invalid asset object!')
        # Check if the hacker actually has this asset in their inventory
        elif asset in hacker.inventory:
            # Only allow storing if the asset is not encrypted
            if not asset.encrypted:
                hacker.inventory.remove(asset)  # Remove asset from hacker inventory
                self.storage.append(asset)  # Add asset to rig storage
                print(f'{asset.name} stored in rig!')
            else:
                # Display a message if asset is encrypted that it cannot be transferred
                print('Cannot store encrypted asset!')
        else:
            # Display a message if Hacker doesn't have this asset
            print(f'Hacker does not have {asset.name} asset!')

    def release_asset(self, hacker, asset: Asset) -> None:
        """
        Release an unencrypted asset from the rig's storage to the hacker's inventory.

        Validates the asset object, ensures it is in the rig's storage, and confirms
        it is not encrypted before transferring it to the hacker's inventory.
        It also prevents adding duplicates to the hacker's inventory list.

        Args:
            hacker: The hacker object who will receive the asset.
            asset (Asset): The asset object to be transferred.

        Returns:
            None: Prints a message describing the outcome.
        """
        # Validate if asset is an instance of Asset
        if not isinstance(asset, Asset):
            print('Invalid asset object!')
        # Check if the asset exists in the rig's storage
        elif asset in self.storage:
            # Only allow releasing if the asset is not encrypted
            if not asset.encrypted:
                # Ensure the hacker does not already have this asset (avoid duplicates)
                if asset not in hacker.inventory:
                    self.storage.remove(asset)  # Remove asset from rig storage
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

    def get_condition(self) -> str:
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
        max_hits = 2 + self.upgrade_level
        # Check if rig is broken or has reached/exceeded max hits
        if self.broken_state or self.damage_counter >= max_hits:
            return f'Broken (Level {self.upgrade_level})'
        # Check if rig has no damage
        elif self.damage_counter == 0:
            return f'Pristine (Level {self.upgrade_level})'
        # Otherwise, rig has some damage but is still operational
        else:
            return f'Damaged (Level {self.upgrade_level})'

    def __str__(self) -> str:
        """
        Provides a string representation of the rig for display.

        Returns:
            str: A string describing the rig's status, condition,
                 upgrade level, and stored assets.
        """
        # Create a list to store asset names
        asset_names = []

        # Loop through each asset in storage and get its name
        for asset in self.storage:
            asset_names.append(asset.name)

        # Check for asset names, if the list is empty display a message
        if asset_names:
            # Join the names with commas for display
            asset_str = ', '.join(asset_names)
        else:
            asset_str = 'No assets available'

        # Return the formatting string
        return (
            f'Rig Name: {self.name}\n'
            f'Condition: {self.get_condition()}\n'
            f'Upgrade Level: {self.upgrade_level}\n'
            f'Stored Assets: {asset_str}\n'
        )
