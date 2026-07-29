# 🛡️ Python IP Allow List Automation

> A Python-based security automation tool that updates an organization's IP allow list by removing unauthorized IP addresses while demonstrating secure file handling, access control, and automation best practices.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Domain](https://img.shields.io/badge/Domain-Cybersecurity-red)

---

## 📖 Overview

Managing access control lists manually can be repetitive and error-prone. In many organizations, security analysts are responsible for maintaining lists of authorized systems and users that are permitted to access protected resources.

This project automates that process by reading an existing IP allow list, comparing it against a list of IP addresses that should no longer have access, removing unauthorized entries, and generating an updated allow list.

Originally completed as part of the **Google Cybersecurity Professional Certificate**, this repository has been redesigned into a **Portfolio Edition** project with improved code quality, documentation, repository structure, and maintainability.

---

## 🎯 Project Objectives

- Automate IP allow list maintenance
- Reduce manual administrative work
- Demonstrate Python file handling
- Apply access control concepts
- Showcase security automation using Python
- Build a portfolio-ready cybersecurity project

---

## 🏢 Real-World Scenario

A security administrator maintains an allow list containing IP addresses that are authorized to access sensitive company resources.

When employees leave the organization or no longer require access, their IP addresses must be removed from the allow list.

Instead of manually editing the file every time changes occur, this project automates the entire process.

---

## ⚙️ Features

- Reads an existing allow list
- Reads a remove list
- Compares both datasets
- Removes unauthorized IP addresses
- Generates an updated allow list
- Preserves clean file formatting
- Modular and readable Python code
- Error handling
- Logging support
- Sample data included

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Automation |
| Git | Version Control |
| GitHub | Repository Hosting |
| Text Files | Data Storage |

---

## 📂 Repository Structure

```
python-ip-allowlist-automation/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── allow_list.txt
│   └── remove_list.txt
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── file_handler.py
│   ├── validator.py
│   ├── allowlist_manager.py
│   └── logger_config.py
│
└── tests/
    └── test_allowlist_manager.py
```

---

## 🔄 Workflow

```
             allow_list.txt
                    │
                    ▼
          Read File into Memory
                    │
                    ▼
          Read remove_list.txt
                    │
                    ▼
         Compare IP Addresses
                    │
                    ▼
      Remove Unauthorized Entries
                    │
                    ▼
      Generate Updated Allow List
                    │
                    ▼
      updated_allow_list.txt
```

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-ip-allowlist-automation.git
```

### Navigate into the project

```bash
cd python-ip-allowlist-automation
```

### Run the application

```bash
python src/update_allowlist.py
```

---

## 📋 Example

### Input

**allow_list.txt**

```
192.168.10.25
192.168.10.31
172.16.0.15
10.0.0.8
203.0.113.55
```

**remove_list.txt**

```
172.16.0.15
203.0.113.55
```

---

### Output

```
192.168.10.25
192.168.10.31
10.0.0.8
```

---

## 🔒 Cybersecurity Concepts Demonstrated

- Access Control
- Security Automation
- Least Privilege
- Administrative Scripting
- Configuration Management
- File Integrity
- Secure File Handling

---

## 💡 Why This Project Matters

Even simple automation scripts can save security teams significant time by eliminating repetitive administrative work.

Automating routine security tasks also reduces the likelihood of human error, helping organizations maintain accurate access control records while improving operational efficiency.

Although simplified for educational purposes, the same concepts demonstrated in this project are commonly used in enterprise cybersecurity environments.

---

## 📚 Skills Demonstrated

- Python Programming
- File Input / Output
- String Manipulation
- Lists
- Loops
- Conditional Logic
- Functions
- Security Automation
- Access Control

---

## 📈 Portfolio Enhancements

Compared to the original coursework, this Portfolio Edition includes:

- Professional repository organization
- Improved project documentation
- Modular Python implementation
- Better code readability
- Error handling
- Logging
- Workflow diagram
- Screenshots
- Sample data
- Future improvement roadmap

---

## 🔮 Future Improvements

- IPv6 support
- IP address validation
- Command-line interface
- Audit logging
- CSV import/export
- JSON reporting
- Unit tests
- Docker container
- GitHub Actions automation

---

## 📝 Professional Reflection

Maintaining accurate access control records is a fundamental responsibility in cybersecurity. This project demonstrates how Python can automate repetitive administrative tasks, reducing manual effort while improving consistency and accuracy.

Transforming the original coursework into a portfolio-ready project also provided an opportunity to apply software engineering best practices, including modular design, documentation, and maintainable code organization.

---

## 🙏 Acknowledgment

This project is based on an assignment from the **Google Cybersecurity Professional Certificate**.

The original assignment has been expanded into a portfolio-quality project for educational and professional showcase purposes.

---

## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.
