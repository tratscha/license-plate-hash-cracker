import argparse
from modules import generator, hasher, bruteforce, collision

def main():
    parser = argparse.ArgumentParser(description="License Plate Hash Cracker")

    parser.add_argument("--mode", required=True,
                        choices=["generate", "hash", "bruteforce", "collision"],
                        help="Select mode")

    parser.add_argument("--input", help="Input value")

    args = parser.parse_args()

    if args.mode == "generate":
        generator.run()

    elif args.mode == "hash":
        hasher.run(args.input)

    elif args.mode == "bruteforce":
        bruteforce.run(args.input)

    elif args.mode == "collision":
        collision.run()

if __name__ == "__main__":
    main()