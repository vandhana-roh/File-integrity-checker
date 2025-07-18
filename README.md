# File-integrity-checker

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: BASAVAMGARI VANDHANA

*INTERN ID*: CT06DH153

*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING

*DURATION*: 6 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:

The File Integrity Checker is a Python-based tool designed to detect any unauthorized changes or tampering in files by using cryptographic hash functions such as SHA-256. It works by generating unique hash values for selected files and storing them in a JSON file (`file_hashes.json`) as a reference. Later, the tool can re-calculate the hash values of those files and compare them with the previously stored ones to check if any modifications have occurred. If the hash values match, the file is unchanged; otherwise, it indicates that the file has been altered. The script uses Python’s `hashlib` library for hashing and `argparse` for command-line interaction, allowing users to hash files (`--hash`) or verify their integrity (`--verify`). This tool is especially useful in cybersecurity, forensic investigations, backup verification, and ensuring the integrity of critical system or configuration files. It provides a lightweight and efficient way to monitor file authenticity without needing any external tools. By supporting multiple hashing algorithms, it also gives users flexibility based on their security needs. The tool is executed via the command line and provides clear, readable output for quick assessment

*OUTPUT*:

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/84bbdee8-f15a-4a41-a8e4-949435d9a60b" />
