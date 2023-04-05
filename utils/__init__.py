import sys
import os
from utils import _log

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

log = _log.log
logger = _log.logger
