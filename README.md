# 🛡️ Secure Automated Data Shield

An automated Python-based backup and protection system that continuously monitors a source directory, detects new or modified files, creates incremental backups, and generates compressed ZIP archives for secure storage.

## 🚀 Features

- 📂 Automated folder backup
- 🔄 Detects new and modified files
- 📦 Creates ZIP archives automatically
- ⏰ Scheduled execution using configurable time intervals
- 🔒 File integrity verification using MD5 hashing
- 📁 Preserves original folder structure
- ⚡ Lightweight and easy to configure
- 🖥️ Command-line based automation

---

## 🛠️ Technologies Used

- Python 3.x
- os
- shutil
- hashlib
- zipfile
- schedule

---

## 📂 Project Structure

```text
Secure-Automated-Data-Shield
│
├── data_shield.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── execution.png
│   └── backup_created.png
│
└── sample_backup/
    └── example.zip
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Secure-Automated-Data-Shield.git
cd Secure-Automated-Data-Shield
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Help Menu

```bash
python data_shield.py --h
```

### Usage Information

```bash
python data_shield.py --u
```

### Start Automated Backup

```bash
python data_shield.py 5 Data
```

Where:

- `5` = Backup interval in minutes
- `Data` = Source folder name

Example:

```bash
python data_shield.py 10 Documents
```

This creates backups every 10 minutes.

---

## 🔐 How It Works

1. Scans the source directory.
2. Compares files using MD5 hashing.
3. Copies only new or modified files.
4. Creates a backup directory.
5. Generates a ZIP archive of the backup.
6. Repeats automatically at the specified interval.

---

## 📸 Screenshots

### Application Execution

_Add screenshot here_

### Generated Backup Archive

_Add screenshot here_

---

## 📈 Future Enhancements

- Email notification after backup
- Backup encryption using AES
- Cloud storage integration
- Backup history tracking
- GUI Dashboard
- Backup restoration module

---

## 👨‍💻 Author

**Atharv Bhosale**


GitHub: https://github.com/atharv-bhosale11

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
