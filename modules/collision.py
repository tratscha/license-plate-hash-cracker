import hashlib

def run():
    print("[+] Checking for collisions...")

    seen = {}

    samples = ["AA-000", "AB-111", "AC-222"]

    for plate in samples:
        h = hashlib.sha256(plate.encode()).hexdigest()

        if h in seen:
            print(f"[!] Collision found: {plate} and {seen[h]}")
        else:
            seen[h] = plate

    print("[+] No collisions detected")