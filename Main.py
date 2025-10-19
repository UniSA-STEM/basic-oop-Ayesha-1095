"""
File: main.py
Description: Main test script for the "Into the Grid" assignment.
This script runs a set of small tests that show how the Asset, Rig, and
Hacker classes work together. Each test is grouped into a function so the
results are easy to read.
Author: Ayesha Siddiqa
ID: 110481368
Username: SIDAY032
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Hacker import Hacker
from Rig import Rig


def display_header(title: str):
    """
    Show a clear header for each test section.

    This prints a boxed title to separate test output blocks. Helps the
    reviewer see each section easily.
    """
    print('=' * 50)
    print(title.center(50))
    print('=' * 50)


# ============================================================
# 1. CLASS-LEVEL TESTS
# ============================================================
def test_asset_class():
    """
    Test creating assets, changing encryption, and equality.

    This function makes a few Asset objects and prints them. It also
    shows what happens when we set encryption correctly and incorrectly.
    """
    display_header('ASSET CLASS TESTS')

    # Create different assets and show them
    assets = [
        Asset('CryptoToken', 'Used to acquire or repair rigs.'),
        Asset('Data Spike', 'Used in battles.'),
        Asset('Removable Drive', 'Used for extraction.'),
        Asset('Security Chip', 'Used to encrypt or decrypt assets.'),
        Asset('Hardware Patch', 'Used to upgrade rigs.')
    ]

    # Print each asset (calls __str__)
    print('\n>> Created Assets <<')
    for asset in assets:
        print('-', asset)

    # Test encryption
    print('\n>> Encrypting Security Chip <<')
    chip = assets[3]
    chip.encrypted = True
    print('>> After encryption <<')
    print(chip)

    # Test invalid encryption
    print('\n>> Trying to set invalid encryption "Yes" (should print error) <<')
    chip.encrypted = "yes"

    # Check equality of two same assets
    print('\n>> Testing equality <<')
    spike1 = Asset('Data Spike', 'Used in battles.')
    spike2 = Asset('Data Spike', 'Used in battles.')
    print('Spike1 == Spike2:', spike1 == spike2, '\n')


def test_rig_class():
    """
    Test rig creation, hits, repair, upgrades and generation.


    This shows: initial rig state, taking hits, repairing, upgrading,
    generating new assets and the storage-full edge case.
    """

    display_header('RIG CLASS TESTS')

    # Create a rig
    rig = Rig('Rigzilla')

    # Show initial rig details (calls Rig.__str__)
    print('\n>> Initial Rig Details <<')
    print(rig)

    # Call take_hit() several times to show damage progression
    print('>> Testing take_hit() 1 <<')
    print(rig.take_hit())
    print()
    print('>> Testing take_hit() 2 <<')
    print(rig.take_hit())  # Should break after 3 hits
    print()
    print('>> Testing take_hit() 3 <<')
    print(rig.take_hit())

    # Print condition string
    print('\n>> Rig condition <<')
    print(rig.get_condition())

    # Test repair_damage and show result
    print('\n>> Testing repair_damage() <<')
    rig.repair_damage()
    print('\n>> Rig condition after repair <<')
    print(rig.get_condition())

    # Upgrade the rig (increases level and storage)
    print('\n>> Testing upgrade_rig() <<')
    rig.upgrade_rig()
    print('\n>> Rig condition after upgrade <<')
    print(rig.get_condition())

    # Generate new assets until storage is full to test the limit
    print('\n>> Testing generate_asset() with full storage edge case <<')
    # Fill the rig storage to max_storage
    while len(rig.storage) < rig.max_storage:
        rig.generate_asset()

    # Try one more generation - should be blocked by max_storage check
    print('\n>> Attempting to generate asset when storage is full <<')
    rig.generate_asset()

    # Show final rig storage
    print('\n>> Rig storage after generation attempts <<')
    for asset in rig.storage:
        print('-', asset.name)


# ============================================================
# 2. BASIC HACKER TESTS
# ============================================================
def test_hacker_basic():
    """
    Test hacker creation, scanning inventory, acquiring and upgrading rig.

    This test checks normal flows and a few edge cases such as
    trying to upgrade without the needed Hardware Patch.
    """
    display_header('HACKER CLASS - BASIC TESTS')

    # Create a hacker and show initial state (has one CryptoToken)
    h = Hacker('Veil@dy')
    print('\n>> Initial Hacker Details <<')
    print(h)

    # Scan inventory for CryptoToken (this should remove it from inventory)
    print('>> Scan inventory for CryptoToken (returns asset or None) <<')
    found = h.scan_inventory('CryptoToken')
    print(found)
    print('\n>> Hacker after scan (inventory changed) <<')
    print('>> Hacker details <<')
    print(h)

    # Put the CryptoToken back for next tests (restore state)
    print('>> Added CryptoToken asset again for further testing <<')
    h.inventory.append(Asset('CryptoToken', 'Used to acquire or repair rigs.'))

    # Acquire a rig normally
    print('>> Acquiring a rig <<')
    acquire_rig = h.acquire_a_rig()
    print(acquire_rig)
    print('\n>> Hacker after acquiring rig (calls __str__) <<')
    print('>> Hacker details <<')
    print(h)

    # Edge case: attempt to acquire a second rig
    print('>> Try to acquire a rig again (edge) <<')
    print(h.acquire_a_rig())

    # Edge case: try upgrade without Hardware Patch
    print('\n>> Try upgrade without Hardware Patch (edge) <<')
    print(h.upgrade_hacker_rig())

    # Normal upgrade: add patch and upgrade
    h.inventory.append(Asset('Hardware Patch', 'Used to upgrade rigs.'))
    print('>> After adding Hardware Patch and calling upgrade <<')
    print(h.upgrade_hacker_rig())
    print('>> Rig after upgrade <<')
    print(h.rig)


# ============================================================
# 3. STORAGE TESTS
# ============================================================
def test_store_and_retrieve():
    """
    Test moving assets between hacker and rig (store and retrieve).

    Shows storing a Security Chip, retrieving it back, and failing cases
    (encrypted asset and missing asset).
    """
    display_header('STORE & RETRIEVE ASSET TESTS')

    # Create hacker and acquire a rig first
    h = Hacker('Veil@dy')
    print('\n>> Hacker before acquiring rig <<')
    print(h)

    # Acquire a rig (required to store/retrieve)
    print('>> Acquiring a rig <<\n')
    print(h.acquire_a_rig())

    # Add Security Chip to inventory
    asset = Asset('Security Chip', 'Used to encrypt or decrypt assets')
    h.inventory.append(asset)

    print('\n>> Before store - hacker inventory <<')
    for a in h.inventory:
        print('-', a)

    # Store asset to rig
    print('\n>> Store Security Chip to rig <<')
    print(h.store_asset(asset))
    print('\n>> After store - hacker (print):')
    print(h)

    # Retrieve it back
    print('>> Retrieve the Security Chip from rig <<')
    print(h.retrieve_asset(asset))

    print('\n>> After retrieve - hacker (print) <<')
    print(h)

    # --- Edge case tests ---

    # Try to store an encrypted asset
    encrypted_asset = Asset('Data Spike', 'Used in battles')
    encrypted_asset.encrypted = True
    h.inventory.append(encrypted_asset)
    print('>> Attempt to store an encrypted asset <<')
    print(h.store_asset(encrypted_asset))

    # Try to retrieve a non-existent asset
    fake_asset = Asset('Removable Drive', 'Found in rigs and used for extraction')
    print('\n>> Attempt to retrieve asset not in rig <<')
    print(h.retrieve_asset(fake_asset))


# ============================================================
# 4. ENCRYPTION TESTS
# ============================================================
def test_encrypt_decrypt():
    """
    Test encrypting and decrypting assets using Security Chip.

    The Security Chip can be in either hacker inventory or rig storage.
    This test shows successful encrypt/decrypt and the blocked case.
    """

    display_header('ENCRYPT & DECRYPT TESTS')

    h = Hacker('CryptoAsh')
    print('>> Hacker before acquiring rig <<')
    print(h)

    # Acquire a rig
    print('>> Acquiring rig:')
    print(h.acquire_a_rig())

    # Put a Security Chip into rig storage for encryption
    chip = Asset('Security Chip', 'Used to encrypt or decrypt assets.')
    h.rig.storage.append(chip)

    # Add asset to inventory to encrypt
    ast = Asset('Hardware Patch', 'Used to upgrade rigs')
    h.inventory.append(ast)
    print('>> Before encryption - hacker state <<')
    print(h)

    # Encrypt the asset and show result
    print('>> Encrypt asset <<')
    print(h.encrypt_asset(ast))
    print('\n>> After encryption - hacker state:')
    print(h)

    # Try to encrypt an already encrypted asset
    chip2 = Asset('Security Chip', 'Used to encrypt or decrypt assets.')
    h.rig.storage.append(chip2)
    print('>> Attempt to encrypt already encrypted asset <<')
    print(h.encrypt_asset(ast))

    # Add a Security Chip to decrypt
    chip3 = Asset('Security Chip', 'Used to encrypt or decrypt assets.')
    h.rig.storage.append(chip3)
    print('\n>> Decrypt asset <<')
    print(h.decrypt_asset(ast))
    print('\n>> After decryption - hacker state <<')
    print(h)


# ============================================================
# 5. ATTACK & EXTRACTION TESTS
# ============================================================
def test_launch_attack_and_extract():
    """Test attacking another hacker and extracting assets"""

    display_header('ATTACK & EXTRACTION TESTS')

    # Create hackers and give them rigs
    attacker = Hacker('Veil@dy')
    defender = Hacker('CryptoAsh')
    print('>> Both hackers acquire rigs <<\n')
    print('** Attacker **')
    print(attacker.acquire_a_rig())
    print('\n** Defender **')
    print(defender.acquire_a_rig())

    # Defender storage: one unsecured token and one encrypted secret
    defender.rig.storage.append(Asset('CryptoToken', 'Used to acquire or repair rigs.'))
    secret = Asset('SecretFile', 'Top secret')
    secret.encrypted = True
    defender.rig.storage.append(secret)

    # Attacker Data Spikes, give exactly 3 so we can show 3 steps
    for _ in range(3):
        attacker.rig.storage.append(Asset('Data Spike', 'Used in battles'))

    # Function to show the visual rig's health bar
    def rig_health_bar(rig):
        """Return a small visual bar and hits text: [**-] (1/3)."""
        max_hits = 2 + rig.upgrade_level
        damage = rig.damage_counter
        bar = '*' * damage + '-' * (max_hits - damage)
        return f"[{bar}] ({damage}/{max_hits})"

    print("\n>> Attacker Launching Data Spikes <<")

    # Helper to show status after an attack (simple loop to count spikes)
    def after_status():
        spikes_left = 0
        for asset in attacker.rig.storage:
            if asset.name == 'Data Spike':
                spikes_left += 1

        print(f"Defender: {defender.rig.get_condition()} | Attacker Trace: {attacker.trace_level}")
        print(f"Data Spikes left (attacker rig): {spikes_left}")

    # --- ATTACK #1 ---
    print('\n' + '*' * 50)
    print('ATTACK #1: Damage')
    print(f"Defender: {defender.rig.name} {rig_health_bar(defender.rig)}")
    if not defender.rig.broken_state:
        print(attacker.launch_data_spike(defender.rig))
    else:
        print("Blocked: target rig already broken.")
    after_status()
    print('*' * 50)

    # --- ATTACK #2 ---
    print('\n' + '*' * 50)
    print('ATTACK #2: Break Rig')
    print(f"Defender Rig (before): {defender.rig.name} {rig_health_bar(defender.rig)}")
    if not defender.rig.broken_state:
        print(attacker.launch_data_spike(defender.rig))
    else:
        print("Blocked: target rig already broken.")
    after_status()
    print('*' * 50)

    # --- ATTACK #3 ---
    print('\n' + '*' * 50)
    print('ATTACK #3: Attempt after break (should be blocked)')
    print(f"Defender Rig (before): {defender.rig.name} {rig_health_bar(defender.rig)}")
    if defender.rig.broken_state:
        print(f"Blocked: {defender.rig.name} is already broken — no attack performed.")
    else:
        print(attacker.launch_data_spike(defender.rig))
    after_status()
    print('*' * 50)

    # --- EXTRACTION SUCCESS ---
    print('\n>> Extraction Success <<')
    attacker.rig.storage.append(Asset('Removable Drive', 'Used for extraction'))
    msg = attacker.extract_unsecured_assets(defender.rig)
    msg += f"\nDefender Broken: {defender.rig.broken_state} | Inventory Count: {len(attacker.inventory)}"
    print(msg)
    print('*' * 50)

    # --- EXTRACTION FAILURE: Rig Repaired ---
    print('\n>> Extraction Failure: Rig Repaired <<')
    defender.rig.repair_damage()
    print(attacker.extract_unsecured_assets(defender.rig))
    print('*' * 50)

    # --- EXTRACTION FAILURE: No Removable Drive ---
    print('\n>> Extraction Failure: No Removable Drive <<')

    # Remove any removable drive from attacker rig storage (safe loop)
    for asset in attacker.rig.storage[:]:
        if asset.name == 'Removable Drive':
            attacker.rig.storage.remove(asset)

    # Break defender rig again so extraction would be allowed if a drive existed
    # CALL take_hit()
    defender.rig.take_hit()
    defender.rig.take_hit()

    after_status()
    print(attacker.extract_unsecured_assets(defender.rig))
    print('*' * 50)


# ============================================================
# 6. TRACE LEVEL LIMIT TEST
# ============================================================

def test_trace_limit():
    """Test what happens when hacker trace level reaches maximum."""

    display_header('TRACE LEVEL LIMIT TEST')

    # Create a Hacker and give them a rig
    h = Hacker('TraceLord')
    h.acquire_a_rig()

    # Manually set the hacker's trace level to the maximum (10
    h.trace_level = 10

    # Try to perform actions when trace level is at its limit
    print('\n>> Trace level set to 10 (max). Attempt restricted actions:')

    # Try to launch a data spike (should be blocked or fail if the rule is implemented)
    print('\n>> Launch data spike <<')
    print('^' * 40)
    h.launch_data_spike(h.rig)  # try launching own rig (just to see reaction)
    print(h.launch_data_spike(Rig('DummyRig')))  # try launching at another rig

    # Add a Security Chip and a Removable Drive to the hacker's inventory
    chip = Asset('Security Chip', 'Used to encrypt or decrypt assets.')
    h.inventory.append(chip)
    asset = Asset('Removable Drive', 'Used for extraction.')
    h.inventory.append(asset)

    # Try to encrypt an asset when trace level is high (should fail if restrictions are active)
    print('\n>> Encrypt asset with high trace (should block if implemented):')
    print('^' * 40)
    print(h.encrypt_asset(asset))


# ============================================================
# 7. EDGE CASE TESTS
# ============================================================

def test_edge_cases():
    """Test edge cases like missing rig, no token, or encrypted storage."""

    display_header('EDGE CASE TESTS')

    h = Hacker('V0il3t')

    # Try acquiring a rig without having a CryptoToken
    print('\n>> Acquire rig without CryptoToken <<')
    h.inventory.clear()
    print(h.acquire_a_rig())

    # Try upgrading without a rig (should fail)
    print('>> Upgrade without rig <<')
    print(h.upgrade_hacker_rig())

    # Add a Hardware Patch to inventory and acquire a rig
    h.inventory.append(Asset('Hardware Patch', 'Used to upgrade rigs.'))
    h.acquire_a_rig()

    # Try to store an encrypted asset
    print('\n>> Store encrypted asset <<')
    enc = Asset('Security Chip', 'Used to encrypt or decrypt assets.')
    enc.encrypted = True
    print(h.store_asset(enc))

    # Try to retrieve an asset not in rig storage
    print('\n>> Retrieve asset not in rig <<')
    print(h.retrieve_asset(Asset('Security Chip', 'Used to encrypt or decrypt assets.')))


def main():
    print("\n=== RUNNING HACKER SIMULATION TESTS ===")
    # Class-level tests
    test_asset_class()
    test_rig_class()
    test_hacker_basic()
    # Interaction tests
    test_store_and_retrieve()
    test_encrypt_decrypt()
    test_launch_attack_and_extract()
    test_trace_limit()
    test_edge_cases()


if __name__ == "__main__":
    main()
