🚀 Day 1: Shell Scripting vs. Python for DevOpsThis document demonstrates the functional differences between Shell Scripting (Bash) and Python. In DevOps, we use Shell for "near-the-metal" system tasks and Python for "high-level" logic and API interactions.📂 Scenario 1: System-Level Automation (The Shell Territory)Task: Create a directory, generate a dummy log file, and check the system's disk usage.Shell Script (system_check.sh)Shell is native to the Linux kernel. It is concise and fast for executing standard system commands.Bash#!/bin/bash

# Define variables
DIR_NAME="devops_logs"
FILE_NAME="daily_report.log"

# Create a directory if it doesn't exist
mkdir -p $DIR_NAME

# Generate a log entry
echo "Log Entry: $(date) - System is healthy" > $DIR_NAME/$FILE_NAME

# Check disk space (human-readable)
echo "--- Current Disk Usage ---"
df -h | grep '^/dev/'
🐍 Scenario 2: Data Manipulation & Logic (The Python Territory)Task: Process a list of server configurations (JSON-style) and identify which ones require a security update.Python Script (security_filter.py)Python excels at handling data structures (Lists and Dictionaries) and performing complex conditional logic.Pythonimport json

# Simulated data from a Cloud API or Config File
servers_json = '''
[
    {"id": "web-01", "os": "Ubuntu", "version": "20.04", "patch_required": true},
    {"id": "db-01", "os": "RedHat", "version": "8.4", "patch_required": false},
    {"id": "app-01", "os": "Ubuntu", "version": "22.04", "patch_required": true}
]
'''

# Parse the JSON string into a Python List
servers = json.loads(servers_json)

print("--- Servers Requiring Critical Updates ---")

# Logic: Filter and print only servers needing patches
for server in servers:
    if server["patch_required"] == True:
        print(f"⚠️ ACTION REQUIRED: Update {server['id']} (Running {server['os']})")

📊 Key Differences at a Glance
FeatureShell ScriptingPython ScriptingPrimary UseSystem admin, file manipulation.APIs, Cloud SDKs, complex logic.SyntaxMinimalist, command-based.Readable, structured, object-oriented.Data HandlingMostly Strings (text).Rich types (Lists, Dicts, JSON).PortabilityHard to run on Windows (needs GitBash/WSL).Cross-platform (Windows, Linux, Mac).Error HandlingBasic (Exit codes).Robust (try/except blocks).


🛠️ How to Run These in VS Code
For Shell:

Open the VS Code Terminal.

Type bash system_check.sh.

For Python:

Ensure your Python extension is active.

Click the Play button in the top right or type python security_filter.py in the terminal.