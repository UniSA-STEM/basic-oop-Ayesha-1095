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
        If damage reaches 2 (for a level 0 rig), the rig becomes broken.
        """
        self.__damage_counter += 1  # Increase damage counter by 1

        # Check if rig has taken enough damage to be broken
        if self.__damage_counter >= 2:
            self.__broken_state = True  # Set the rig as broken
            print(f'{self.__name} has been broken!')
        else:
            print(f'{self.__name} took a hit. Damage counter: {self.__damage_counter}')

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
