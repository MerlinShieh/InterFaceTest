import os
import sys
from units.readYaml import read_yaml_data
# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 获取配置文件路径
API_CONFIG = os.path.join(BASE_DIR, 'config/api_config.ini')
RUN_CONFIG = os.path.join(BASE_DIR, 'config/run_config.ini')
DB_CONFIG = os.path.join(BASE_DIR, 'config/db_config.ini')