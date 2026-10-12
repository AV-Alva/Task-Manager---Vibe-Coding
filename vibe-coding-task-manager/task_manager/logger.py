import logging

import os
import logging

logger = logging.getLogger('task_manager')
logger.setLevel(logging.DEBUG)

# Create log folder if it doesn't exist
log_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'log')
os.makedirs(log_folder, exist_ok=True)

# Log file path
log_file_path = os.path.join(log_folder, 'task_manager.log')

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create file handler
fh = logging.FileHandler(log_file_path)
fh.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)