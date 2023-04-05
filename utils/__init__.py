import sys
import os
from utils import new_log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

log = new_log.log
logger = new_log.logger
