import hashlib
import string
import itertools

def run(target_hash):
    if not target_hash:
        print("Provide hash")
        return

    print("[+] Starting brute-force...")

    letters = string.ascii_uppercase[:3]
    numbers = "012"

    for l1, l2, n in itertools.product(letters, letters, numbers):
        plate = f"{l1}{l2}-{n}{n}{n}"
        hashed = hashlib.sha256(plate.encode()).hexdigest()

        if hashed == target_hash:
            print(f"[+] Match found: {plate}")
            return

    print("[-] No match found")