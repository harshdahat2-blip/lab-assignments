"""
File Encryption/Decryption Tool
================================
Encrypts and decrypts text files using multiple algorithms:
  1. Caesar Cipher  – shifts each letter by a numeric key
  2. Vigener Cipher – uses a keyword for poly-alphabetic shifting
  3. XOR Cipher     – XORs every character with a numeric key

Usage (command line):
    python file_encryptor.py

Or import as a module:
    from file_encryptor import encrypt_file, decrypt_file
"""

import os
import sys


# ──────────────────────────────────────────────
#  Caesar Cipher
# ──────────────────────────────────────────────

def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt text using the Caesar Cipher."""
    result = []
    shift = shift % 26  # normalise shift to 0-25
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)   # preserve spaces, punctuation, digits
    return ''.join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt text that was encrypted with the Caesar Cipher."""
    return caesar_encrypt(text, -shift)


# ──────────────────────────────────────────────
#  Vigenère Cipher
# ──────────────────────────────────────────────

def vigenere_encrypt(text: str, keyword: str) -> str:
    """Encrypt text using the Vigenère Cipher."""
    if not keyword.isalpha():
        raise ValueError("Vigenère keyword must contain only letters (a-z / A-Z).")
    keyword = keyword.upper()
    result = []
    key_index = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)


def vigenere_decrypt(text: str, keyword: str) -> str:
    """Decrypt text that was encrypted with the Vigenère Cipher."""
    if not keyword.isalpha():
        raise ValueError("Vigenère keyword must contain only letters (a-z / A-Z).")
    keyword = keyword.upper()
    result = []
    key_index = 0
    for ch in text:
        if ch.isalpha():
            shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(ch)
    return ''.join(result)


# ──────────────────────────────────────────────
#  XOR Cipher
# ──────────────────────────────────────────────

def xor_cipher(text: str, key: int) -> str:
    """Encrypt OR decrypt text using XOR (same operation both ways)."""
    if not (0 <= key <= 255):
        raise ValueError("XOR key must be an integer between 0 and 255.")
    return ''.join(chr(ord(ch) ^ key) for ch in text)


# ──────────────────────────────────────────────
#  File helpers
# ──────────────────────────────────────────────

def read_file(filepath: str) -> str:
    """Read and return the contents of a text file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: '{filepath}'")
    if not os.path.isfile(filepath):
        raise IsADirectoryError(f"Path is a directory, not a file: '{filepath}'")
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath: str, content: str) -> None:
    """Write content to a text file, creating directories if needed."""
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


# ──────────────────────────────────────────────
#  Public API – encrypt / decrypt files
# ──────────────────────────────────────────────

ALGORITHMS = ('caesar', 'vigenere', 'xor')


def encrypt_file(input_path: str, output_path: str,
                 algorithm: str, key) -> None:
    """
    Read a text file, encrypt its contents, and write to output_path.

    Parameters
    ----------
    input_path  : path to the plaintext file
    output_path : path where the encrypted file will be saved
    algorithm   : 'caesar', 'vigenere', or 'xor'
    key         : int (shift) for caesar/xor, str (keyword) for vigenere
    """
    algorithm = algorithm.lower()
    if algorithm not in ALGORITHMS:
        raise ValueError(f"Unknown algorithm '{algorithm}'. "
                         f"Choose from: {', '.join(ALGORITHMS)}")

    plaintext = read_file(input_path)

    if algorithm == 'caesar':
        if not isinstance(key, int):
            raise TypeError("Caesar Cipher requires an integer key (shift value).")
        ciphertext = caesar_encrypt(plaintext, key)

    elif algorithm == 'vigenere':
        if not isinstance(key, str):
            raise TypeError("Vigenère Cipher requires a string keyword.")
        ciphertext = vigenere_encrypt(plaintext, key)

    else:  # xor
        if not isinstance(key, int):
            raise TypeError("XOR Cipher requires an integer key (0-255).")
        ciphertext = xor_cipher(plaintext, key)

    write_file(output_path, ciphertext)
    print(f"[✓] Encrypted  '{input_path}'  →  '{output_path}'  (algorithm: {algorithm})")


def decrypt_file(input_path: str, output_path: str,
                 algorithm: str, key) -> None:
    """
    Read an encrypted file, decrypt its contents, and write to output_path.

    Parameters
    ----------
    Same as encrypt_file – key must match what was used during encryption.
    """
    algorithm = algorithm.lower()
    if algorithm not in ALGORITHMS:
        raise ValueError(f"Unknown algorithm '{algorithm}'. "
                         f"Choose from: {', '.join(ALGORITHMS)}")

    ciphertext = read_file(input_path)

    if algorithm == 'caesar':
        if not isinstance(key, int):
            raise TypeError("Caesar Cipher requires an integer key (shift value).")
        plaintext = caesar_decrypt(ciphertext, key)

    elif algorithm == 'vigenere':
        if not isinstance(key, str):
            raise TypeError("Vigenère Cipher requires a string keyword.")
        plaintext = vigenere_decrypt(ciphertext, key)

    else:  # xor
        if not isinstance(key, int):
            raise TypeError("XOR Cipher requires an integer key (0-255).")
        plaintext = xor_cipher(ciphertext, key)   # XOR is its own inverse

    write_file(output_path, plaintext)
    print(f"[✓] Decrypted  '{input_path}'  →  '{output_path}'  (algorithm: {algorithm})")


# ──────────────────────────────────────────────
#  Interactive CLI
# ──────────────────────────────────────────────

def _get_key(algorithm: str):
    """Prompt the user for the appropriate key type."""
    if algorithm == 'caesar':
        while True:
            try:
                return int(input("  Enter shift value (integer, e.g. 3): ").strip())
            except ValueError:
                print("  [!] Please enter a valid integer.")

    elif algorithm == 'vigenere':
        while True:
            kw = input("  Enter keyword (letters only, e.g. SECRET): ").strip()
            if kw.isalpha():
                return kw
            print("  [!] Keyword must contain only letters.")

    else:  # xor
        while True:
            try:
                val = int(input("  Enter XOR key (integer 0-255): ").strip())
                if 0 <= val <= 255:
                    return val
                print("  [!] Value must be between 0 and 255.")
            except ValueError:
                print("  [!] Please enter a valid integer.")


def _get_algorithm() -> str:
    """Ask the user to choose an algorithm."""
    print("\n  Algorithms available:")
    print("    1. Caesar Cipher  (integer shift key)")
    print("    2. Vigenère Cipher (keyword)")
    print("    3. XOR Cipher     (integer key 0-255)")
    choices = {'1': 'caesar', '2': 'vigenere', '3': 'xor',
               'caesar': 'caesar', 'vigenere': 'vigenere', 'xor': 'xor'}
    while True:
        choice = input("  Choose algorithm [1/2/3 or name]: ").strip().lower()
        if choice in choices:
            return choices[choice]
        print("  [!] Invalid choice. Enter 1, 2, 3, 'caesar', 'vigenere', or 'xor'.")


def main():
    print("=" * 50)
    print("   File Encryption / Decryption Tool")
    print("=" * 50)

    # ── Action ──────────────────────────────────
    while True:
        action = input("\nAction — [E]ncrypt or [D]ecrypt? ").strip().upper()
        if action in ('E', 'ENCRYPT', 'D', 'DECRYPT'):
            encrypting = action.startswith('E')
            break
        print("[!] Please enter E or D.")

    # ── Algorithm ───────────────────────────────
    algorithm = _get_algorithm()

    # ── Key ─────────────────────────────────────
    key = _get_key(algorithm)

    # ── Input file ──────────────────────────────
    while True:
        input_path = input("\n  Input file path: ").strip()
        if input_path:
            break
        print("  [!] Path cannot be empty.")

    # ── Output file ─────────────────────────────
    suggestion = (
        input_path.replace('.txt', '_encrypted.txt')
        if encrypting else
        input_path.replace('_encrypted', '_decrypted')
    )
    output_path = input(f"  Output file path [{suggestion}]: ").strip()
    if not output_path:
        output_path = suggestion

    # ── Execute ─────────────────────────────────
    print()
    try:
        if encrypting:
            encrypt_file(input_path, output_path, algorithm, key)
        else:
            decrypt_file(input_path, output_path, algorithm, key)
    except FileNotFoundError as e:
        print(f"[✗] File error: {e}")
        sys.exit(1)
    except (ValueError, TypeError) as e:
        print(f"[✗] Key/algorithm error: {e}")
        sys.exit(1)
    except PermissionError as e:
        print(f"[✗] Permission denied: {e}")
        sys.exit(1)
    except UnicodeDecodeError:
        print("[✗] Could not read file as UTF-8 text. "
              "Make sure the file is a plain text file.")
        sys.exit(1)

    print("\nDone! ✓")


# ──────────────────────────────────────────────
#  Quick self-test (run with: python file_encryptor.py --test)
# ──────────────────────────────────────────────

def _run_tests():
    sample = "Hello, World! The Quick Brown Fox Jumps Over The Lazy Dog. 12345"
    print("Running self-tests …\n")

    # Caesar
    enc = caesar_encrypt(sample, 13)
    dec = caesar_decrypt(enc, 13)
    assert dec == sample, "Caesar test failed"
    print(f"  Caesar (shift=13)\n    Plain : {sample}\n    Cipher: {enc}\n    Back  : {dec}\n")

    # Vigenere
    enc = vigenere_encrypt(sample, "KEY")
    dec = vigenere_decrypt(enc, "KEY")
    assert dec == sample, "Vigenère test failed"
    print(f"  Vigenère (keyword='KEY')\n    Plain : {sample}\n    Cipher: {enc}\n    Back  : {dec}\n")

    # XOR
    enc = xor_cipher(sample, 42)
    dec = xor_cipher(enc, 42)
    assert dec == sample, "XOR test failed"
    print(f"  XOR (key=42)\n    Plain : {sample}\n    Cipher: {repr(enc)}\n    Back  : {dec}\n")

    print("All tests passed ✓")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        _run_tests()
    else:
        main()
