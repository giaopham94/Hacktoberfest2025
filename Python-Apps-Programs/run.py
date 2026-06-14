import os
import csv
from solders.keypair import Keypair
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def generate_seed_phrase():
    """Generate a BIP39 seed phrase."""
    mnemonic = Bip39MnemonicGenerator().FromWordsNumber(12)  # Generate a 12-word mnemonic
    return mnemonic

def account_from_seed(seed_phrase):
    """Generate a keypair from a seed phrase."""
    seed_bytes = Bip39SeedGenerator(seed_phrase).Generate()
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.SOLANA)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
    return bip44_acc.PublicKey().ToAddress(), bip44_acc.PrivateKey().Raw().ToHex()

if __name__ == '__main__':
    name_file = str(input("Name Output file (without csv): "))
    amount = int(input("How many accounts to create: "))
    i = 0

    directory = "Wallet"
    create_directory_if_not_exists(directory)

    with open(file=os.path.join(directory, f"{name_file}.csv"), mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "Seed Phrase"])  # Write header row
        while i != amount:
            seed_phrase = generate_seed_phrase()
            address, _ = account_from_seed(seed_phrase)
            print(f"Generated wallet {i+1}/{amount}: Address: {address}")
            writer.writerow([address, seed_phrase])
            i += 1
