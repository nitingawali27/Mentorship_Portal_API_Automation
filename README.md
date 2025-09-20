# Mentorship_Portal_API_Automation

## Overview
This repository contains automated API test cases for the **Mentorship Program Portal**.  
It uses **Python**, **Playwright**, and **pytest** to validate various API endpoints, including employee search, welcome messages, and employee details.

---

## Features
- API client setup for reusable requests  
- Test scripts for GET endpoints:
  - Welcome message
  - Employee search
  - Employee details
- Verification utilities for:
  - HTTP status codes
  - JSON key existence
  - Response content
- Logging and reporting for test execution  
- Variables and configuration files for easy maintenance

---

## Project Structure

Mentorship_Portal_API_Automation/
│
├─ Tests/ # Test scripts
├─ Utilities/ # Helper modules (API client, logger, verifications, variables)
├─ Reports/ # Test execution reports
├─ Logs/ # Log files
├─ venv/ # Python virtual environment (ignored in git)
├─ requirements.txt # Project dependencies
├─ README.md # Project documentation
└─ .gitignore # Git ignore file

--

## Setup

1. Clone the repository:
git clone https://github.com/nitingawali27/Mentorship_Portal_API_Automation.git
Navigate to project folder:


cd Mentorship_Portal_API_Automation
Create and activate virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
Install dependencies:

pip install -r requirements.txt
Running Tests
Run all tests:


pytest
Run a specific test file:


pytest Tests/test_mentorship.py
Test reports will be generated in the Reports/ folder.

Notes
Make sure to keep the venv/ folder ignored in Git.
Logs are stored in the Logs/ folder for debugging.

Variables like firstname, lastname, and employeeCode are maintained in Utilities/variables.py for easy updates.

Author
Nitin Gawali