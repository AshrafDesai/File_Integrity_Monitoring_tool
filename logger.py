import logging
import os

def setup_logger(log_file):
    log_dir = os.path.dirname(log_file)
    
    # Create log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    logging.info(event)
