import hashlib
import os
import json
import argparse

HASH_STORE = "file_hashes.json"

def calculate_hash(file_path, algorithm='sha256'):
    """Calculate the hash of a file."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def hash_files(file_list, algorithm='sha256'):
    """Hash multiple files and store their hashes."""
    hashes = {}
    for file_path in file_list:
        file_hash = calculate_hash(file_path, algorithm)
        if file_hash:
            hashes[file_path] = file_hash
    with open(HASH_STORE, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(f"Hashes stored in {HASH_STORE}")

def verify_files(algorithm='sha256'):
    """Verify file hashes against the stored hash file."""
    if not os.path.exists(HASH_STORE):
        print("No stored hash file found.")
        return
    with open(HASH_STORE, 'r') as f:
        old_hashes = json.load(f)

    for file_path, old_hash in old_hashes.items():
        current_hash = calculate_hash(file_path, algorithm)
        if current_hash is None:
            continue
        if current_hash == old_hash:
            print(f"[OK] {file_path}")
        else:
            print(f"[MODIFIED] {file_path}")

def main():
    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument('--hash', nargs='+', help="Hash and store hashes of files")
    parser.add_argument('--verify', action='store_true', help="Verify files using stored hashes")
    parser.add_argument('--algo', default='sha256', help="Hash algorithm (default: sha256)")
    args = parser.parse_args()

    if args.hash:
        hash_files(args.hash, args.algo)
    elif args.verify:
        verify_files(args.algo)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
 