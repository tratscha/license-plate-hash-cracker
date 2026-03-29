# license-plate-hash-cracker
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Security](https://img.shields.io/badge/Focus-Cryptography-red)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)

# License Plate Hash Cracker
### Brute Force • SHA-256 Hashing • Collision / Integrity Check

---

## Project Overview

This project demonstrates a small, controlled cryptographic workflow based on a university assignment.

The original task used Italian license plate patterns in the form `AA 000 AA`, with 22 valid letters because `I`, `O`, `Q`, and `U` were excluded. The task also involved generating plates, hashing them with SHA-256, and comparing hashes to identify matches.

This GitHub version keeps the same idea, but it is organized as a clean, reusable Python project.

---

## Why the plate is stored without spaces

The display format is `AA 000 AA`, but the canonical hash input is stored without spaces as `AA000AA`.

That makes the hash deterministic and avoids ambiguity.

Example:

- Display: `AB 123 CD`
- Canonical input: `AB123CD`

---
## Notes
- The search space is intentionally limited for demonstration
- Real brute-force attacks require much larger datasets and optimization
- No real-world sensitive data is used

## Features

- License plate generation
- SHA-256 hashing
- Brute-force hash matching
- Hash uniqueness / collision sanity check
- Demo workflow for quick testing

---

## Project Structure

```text
license-plate-hash-cracker/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── sample_target.json
├── modules/
│   ├── __init__.py
│   ├── config.py
│   ├── generator.py
│   ├── hasher.py
│   ├── bruteforce.py
│   ├── collision.py
│   └── io_utils.py
├── results/
└── screenshots/
