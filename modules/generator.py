import string

def run():
    print("[+] Generating license plates...")

    letters = string.ascii_uppercase
    numbers = "0123456789"

    for l1 in letters[:3]:
        for l2 in letters[:3]:
            for n in numbers[:3]:
                plate = f"{l1}{l2}-{n}{n}{n}"
                print(plate)