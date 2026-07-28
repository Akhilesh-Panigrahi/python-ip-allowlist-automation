# 🛡️ Python IP Allow List Automation

> Automating secure IP allow list management using Python to maintain access control and reduce manual administrative effort.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-green)
![Automation](https://img.shields.io/badge/Focus-Security%20Automation-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Project Overview

Managing IP allow lists manually can become time-consuming and error-prone, especially as organizations grow and access requirements change. This project demonstrates how Python can automate the process of maintaining an IP allow list by removing unauthorized IP addresses from an existing allow list.

Originally completed as part of the **Google Cybersecurity Professional Certificate**, this repository expands upon the coursework by organizing the project into a professional GitHub repository with improved documentation, project structure, and maintainable source code.

---

# Scenario

An organization maintains a list of authorized IP addresses that are allowed to access restricted resources.

Over time, some users no longer require access. Instead of manually editing the allow list, a security analyst uses a Python script to:

* Read the existing allow list
* Compare it against a list of IP addresses that should be removed
* Remove unauthorized entries
* Generate an updated allow list

Automating this process helps reduce administrative effort while minimizing the risk of human error.

---

# Objectives

* Automate allow list maintenance
* Demonstrate Python file handling
* Apply basic security automation concepts
* Improve accuracy by reducing manual edits
* Reinforce access control best practices

---

# Skills Demonstrated

* Python Programming
* Security Automation
* File Input/Output (I/O)
* String Manipulation
* List Operations
* Access Control
* Secure Administration
* Basic Scripting

---

# Technologies Used

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python 3   | Automation scripting              |
| Text Files | Store allow list data             |
| Git        | Version control                   |
| GitHub     | Project hosting and documentation |

---

# Project Structure

```text
python-ip-allowlist-automation/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   └── Original_Google_Project.pdf
│
├── src/
│   ├── update_allowlist.py
│   ├── allow_list.txt
│   ├── remove_list.txt
│   └── updated_allow_list.txt
│
├── diagrams/
│   └── workflow.png
│
├── screenshots/
│   ├── before.png
│   ├── terminal-output.png
│   └── after.png
│
└── assets/
    └── banner.png
```

---

# Workflow

```text
Read allow_list.txt
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
Write Updated Allow List
          │
          ▼
Process Complete
```

---

# Example Input

### allow_list.txt

```text
192.168.1.10
192.168.1.11
192.168.1.12
192.168.1.13
```

### remove_list.txt

```text
192.168.1.11
192.168.1.13
```

---

# Example Output

```text
192.168.1.10
192.168.1.12
```

---

# How It Works

1. Read the current allow list.
2. Load the list of IP addresses to remove.
3. Compare both datasets.
4. Remove matching IP addresses.
5. Save the updated allow list.
6. Confirm successful execution.

---

# Security Concepts

This project demonstrates several foundational cybersecurity concepts:

* Principle of Least Privilege
* Access Control Management
* Administrative Automation
* Data Integrity
* Secure Configuration Management
* Operational Efficiency

Although the project uses a simplified example, these same concepts are commonly applied in enterprise environments to automate administrative security tasks.

---

# Repository Contents

| Folder      | Description                         |
| ----------- | ----------------------------------- |
| docs        | Original coursework PDF             |
| src         | Python source code and sample files |
| diagrams    | Workflow diagrams                   |
| screenshots | Demonstration images                |
| assets      | Repository graphics                 |

---

# Lessons Learned

During this project I gained practical experience with:

* Reading and writing files using Python
* Automating repetitive security tasks
* Working with lists and string manipulation
* Organizing scripts for maintainability
* Applying automation to access control processes

---

# Future Improvements

Potential enhancements include:

* Support for IPv6 addresses
* IP address validation using Python's `ipaddress` module
* Command-line arguments with `argparse`
* Timestamped audit logging
* Export change reports to JSON or CSV
* Automated unit testing
* Interactive command-line interface
* Improved error handling and logging

---

# Acknowledgment

The original project scenario was completed as part of the **Google Cybersecurity Professional Certificate**. This repository reorganizes and expands the original coursework into a portfolio-ready project with enhanced documentation and presentation while preserving the underlying learning objectives.

---

# License

This project is licensed under the MIT License. See the `LICENSE` file for more information.