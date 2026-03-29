import hashlib

def run(value):
    if not value:
        print("Provide input")
        return

    hash_value = hashlib.sha256(value.encode()).hexdigest()

    print(f"[+] Input: {value}")
    print(f"[+] SHA-256: {hash_value}")