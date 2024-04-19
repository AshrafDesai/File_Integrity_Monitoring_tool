import time
from hash_calculator import calculate_md5
from yara_checker import check_file_with_yara
from logger import setup_logger, log_event
from config import read_config, update_config

def check_file_integrity(yara_rule_path, file_path, log_file):
    print(f"Checking file integrity for: {file_path}")  # Debug print
    current_hash = calculate_md5(file_path)
    expected_hash = config.get('FILE_HASH', '')
    
    print(f"Current Hash: {current_hash}")
    print(f"Expected Hash: {expected_hash}")
    
    if expected_hash:
        if current_hash == expected_hash:
            log_event(f"File integrity maintained: {file_path}")
        else:
            log_event(f"File integrity compromised: {file_path}")
    else:
        log_event(f"Initial hash recorded for {file_path}: {current_hash}")
        update_config('FILE_HASH', current_hash)

if __name__ == "__main__":
    config_file = "config.ini"
    config = read_config(config_file)
    
    yara_rule_path = config.get('YARA_RULE_PATH')
    file_path = config.get('FILE_PATH')
    
    if not yara_rule_path or not file_path:
        print("YARA_RULE_PATH or FILE_PATH is not defined in config.ini.")
        exit(1)
    
    # Remove extra quotes from file_path
    file_path = file_path.strip('"')
    
    log_file = "logs/integrity_logs.log"
    
    setup_logger(log_file)
    
    while True:
        check_file_integrity(yara_rule_path, file_path, log_file)
        time.sleep(10)
