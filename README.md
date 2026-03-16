# Password Encryption Project

## About
This project securely encrypts and stores MySQL passwords using Python and Fernet symmetric encryption — so no plain text passwords are ever exposed in the code.

## Technologies Used
- Python 3
- MySQL Connector
- Cryptography (Fernet)

## Project Structure
| File | Description |
|------|-------------|
| `password_utils.py` | Encrypt & Decrypt password functions |
| `mysql_connect_safe.py` | MySQL connection using encrypted password |
| `encrypt_once.py` | One-time key & password encryption generator |
| `.gitignore` | Hides secret.key from GitHub |

## Security
- `secret.key` is never uploaded to GitHub
- Password is always masked when printed
- Fernet encryption ensures password safety

## How It Works
1. Run `encrypt_once.py` → generates `secret.key` + encrypted password
2. Paste encrypted password into `password_utils.py`
3. Run `mysql_connect_safe.py` → connects to MySQL securely
