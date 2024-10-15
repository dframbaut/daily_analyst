
### **README.md**

# File Analysis and Email Reporting Tool

This tool analyzes CSV files in a selected folder, checks for records, validates column structures, and generates an HTML report. The report can be viewed in the terminal, and optionally sent via email.

## Project Structure
```
daily_analyst/
│
├── config_loader.py
├── config.json
├── data_contract.py
├── file_reader.py
├── html_report_generator.py
├── main.py
├── README.md
├── requirements.txt
└── run.sh
```

## Table of Contents
1. [Setup - only first time](#setup---only-first-time)
2. [How to Run the Main Script](#how-to-run-the-main-script)
3. [Configuration](#configuration)
4. [Setting Up Gmail App Password](#setting-up-gmail-app-password)

---

## Setup - only first time

Before running the script, it’s recommended to create a virtual environment to isolate the dependencies for this project. Follow these steps to set up the environment and install the necessary libraries:

### Step 1: Clone the repository and navigate to the Project Folder

1. **Clone the repository**:
   - Open the terminal and clone the repository:
     ```bash
     git clone https://github.com/your-repo/daily_analyst.git
     ```

2. **Navigate to the Project Folder**:
   - Use the `cd` command to navigate to the `daily_analyst` project folder:
     ```bash
     cd daily_analyst
     ```

### Step 2: Run the Setup Script

Once you're in the project folder, you can use the `run.sh` script to handle the setup process automatically. The script will check if Python is installed, create a virtual environment, install the required dependencies, and set up an alias for easy access.

Run the following command:
```bash
./run.sh
```

This script will:
- Create a virtual environment named `env_daily_analyst`.
- Install the necessary dependencies from the `requirements.txt`.
- Set up an alias `daily_analyst` for easy script execution.

### Step 3: Reload your terminal (only required for first-time setup)

After running the setup script, you need to reload your terminal to apply the alias. You can do this by running:
```bash
source ~/.zshrc
```

Once the alias is loaded, you can now run the script with a simple command.

---

### Step 4: Run the Main Script

You can now run the script using the `daily_analyst` alias:
```bash
daily_analyst
```

Follow the instructions in the terminal to select the folder to analyze and generate the report.

---

## Configuration

The tool requires a configuration file named `config.json` that contains the necessary paths, prefixes, email settings, and expected files.

### `config.json` structure:
```json
{
    "data_contract_path": "/path/to/data_contract.json",
    "uploads_folder_path": "/path/to/uploads/folder",
    "prefixes": ["prefix1-", "prefix2-"],
    "suffix_order": ["-table1-", "-table2-"],
    "expected_files": [
        "prefix1-table1-", "prefix1-table2-", "prefix2-table1-", "prefix2-table2-"],
    "sender_email": "your_email@gmail.com",
    "receiver_emails": ["recipient1@example.com", "recipient2@example.com"],
    "smtp_user": "your_email@gmail.com",
    "smtp_password": "your_generated_app_password"
}
```

### Explanation of the Fields:
- **data_contract_path**: The path to the JSON file that contains the data contract.
- **uploads_folder_path**: The path to the folder containing CSV files to be analyzed.
- **prefixes**: A list of file prefixes used to filter and analyze files.
- **suffix_order**: The expected suffixes of the files, ensuring correct processing order.
- **expected_files**: A list of files that are expected to be present in the folder, defined by their prefix and suffix.
- **sender_email**: The email address from which the report will be sent.
- **receiver_emails**: A list of email addresses that will receive the report.
- **smtp_user**: The Gmail address used to send the email (same as `sender_email`).
- **smtp_password**: The app-specific password generated for your Gmail account.

---

## How to Run the Main Script

1. **Start the Program**:
   - Run the script `main.py` from your terminal:
     ```bash
     daily_analyst
     ```

2. **Select a Folder to Analyze**:
   - The program will display a list of folders containing CSV files.
   - Input the number or name of the folder you want to analyze and press **Enter**.

3. **View the Report**:
   - The script will analyze the files in the selected folder and display the following information in the terminal:
     - **Records Data**: Number of records for each file, or "empty file" if the file is empty.
     - **Mismatch Files**: Files where expected columns do not match the found columns.
     - **Valid Files**: Files that have valid records, along with a preview of their data.
     - **Missing Files**: A list of expected files that were not found in the folder.

4. **Choose to Send the Report by Email**:
   - After viewing the report in the terminal, the script will ask if you want to send the report by email.
   - Type `yes` to send the report or `no` to skip email sending.

5. **Email Confirmation**:
   - If you choose to send the report, it will be sent to the specified email addresses using the configuration in `config.json`.

---

## Setting Up Gmail App Password

To securely send the report via Gmail, you need to generate an **App Password**. Here are the steps:

### Steps to Generate a Gmail App Password:

1. Go to your Gmail security settings, look for **App passwords**.
2. **Generate an App Password**:
   - In the **App Passwords** section, you may be prompted to log in again.
   - Type the **App name** and press create.
   - The password will be generated.
3. **Copy the App Password**:
   - You will see a 16-character password. Copy this password.
   - Use this password in your `config.json` file as the value for `"smtp_password"`.
4. **Test Sending Email**:
   - Run your script and ensure that the email is sent successfully using your new App Password.
