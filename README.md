# ADVANCED-ENCRYPTION-TOOL

COMPANY NAME : CODTECH IT SOLUTIONS

NAME : SANIYA

INTERN ID : CTIS5454

DOMAIN NAME : CYBER SECURITY AND ETHICAL HACKING

DURATION : 4 WEEKS

MENTOR NAME : NEELA SANTOSH

TASK 2 : PENETRATION TESTING TOOLKIT

# DESCRIPTION :  Project OverviewThis project was developed as a core task during my Software Development Internship. The objective was to build a robust, production-grade application capable of securing local files using advanced cryptographic standards.The application provides a seamless bridge between complex mathematical security and a modern, user-friendly interface. It ensures that sensitive data remains confidential and, more importantly, tamper-proof.

# 🛠️ Technical Specifications
The tool is built on three pillars of modern cryptography
   1. Advanced Encryption Standard (AES-256-GCM)I implemented AES-256 in Galois/Counter Mode (GCM). Unlike standard block cipher modes (like CBC), GCM is an "Authenticated Encryption" mode.Confidentiality: 256-bit keys make the data unreadable to unauthorized parties.Integrity: It generates an Authentication Tag. If a single bit of the encrypted file is altered (bit-flipping attack), the decryption process will automatically fail and alert the user.
   2. High-Entropy Key Derivation (Scrypt)To prevent "Brute-Force" and "Dictionary Attacks," the application does not use the user's password directly as a key. Instead, it utilizes the Scrypt Key Derivation Function:Salting: A unique 16-byte random salt is generated for every file, preventing "Rainbow Table" attacks.Memory-Hardness: Scrypt is configured to be computationally expensive ($2^{14}$ iterations), significantly slowing down hackers using GPUs or specialized hardware.
   3.  Modern User InterfaceBuilt with CustomTkinter, the UI follows modern design principles:Dark Mode Optimization: Reduces eye strain and provides a professional aesthetic.Event-Driven Architecture: Ensures the UI remains responsive while the "Crypto Engine" processes files in the background.
# 🚀 Deployment & Execution
# Prerequisites
Python 3.8+
Cryptography Library: pip install cryptography
CustomTkinter: pip install customtkinter

# Usage Instructions
Clone: git clone https://github.com/[Your-Username]/AES-Encryption-Tool.git
Launch: Execute python main.py within the VS Code terminal.
Secure: Select your target file, input a master password, and hit Encrypt.
Restore: Select the .enc file and provide the original password to recover your data.

# 📊 Deliverables Met
[x] Robustness: Handles file I/O errors and incorrect password attempts gracefully.
[x] Advanced Algorithms: Implementation of NIST-approved AES-256-GCM.
[x] User-Friendly: Fully functional GUI with clear feedback messages.
