import os
import sys
from utils.readYaml import read_yaml_data
# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 获取配置文件路径
API_CONFIG = os.path.join(BASE_DIR, 'config/apiConfig.yaml')
RUN_CONFIG = os.path.join(BASE_DIR, 'config/runConfig.yaml')
DB_CONFIG = os.path.join(BASE_DIR, 'config/dbConfig.yaml')

# 获取运行配置信息
RC = read_yaml_data(RUN_CONFIG)
INTERVAL = RC['interval']
PROJECT_NAME = RC['project_name']