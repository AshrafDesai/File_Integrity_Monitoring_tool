# File Integrity Monitoring Using YARA Rules
![image](https://github.com/AshrafDesai/File_Integrity_Monitoring_tool/assets/132386307/ef78987d-9208-41f5-b0ea-1150dc336cca)


Overview:

This is a simple File Integrity Monitoring (FIM) system that uses YARA rules to monitor file changes. It checks for modifications in files and alerts the user if any unexpected changes are detected.

# Features:

Monitoring file integrity using YARA rules.
Detecting unauthorized file changes.
Alerting users about file integrity status.

# Prerequisites:

Python 3.x installed
YARA tool installed
YARA rule file (*.yar)
Configuration file (config.ini)
Target file to monitor

# Setup:

# 1.Install Dependencies:
Make sure you have Python 3.x installed.
Install YARA tool on your system.

# 2.Create Configuration File:
Create a config.ini file with the following content:
[DEFAULT]
YARA_RULE_PATH = "path/to/your/yara/rule.yar"
FILE_PATH = "path/to/target/file"

# 3 Run the Monitoring System:
Open a terminal or command prompt.
Navigate to the directory containing the monitoring system files.

Run the command
# python main.py

Note: Make sure to update the paths in the config.ini file according to your file locations.

Feel free to modify and expand this readme.txt file based on your specific requirements and use case!
