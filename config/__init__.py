import json

import os
import sys
import random
from utils.readYaml import read_yaml_data

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 获取配置文件路径
API_CONFIG = os.path.join(BASE_DIR, 'config/apiConfig.yaml')
RUN_CONFIG = os.path.join(BASE_DIR, 'config/runConfig.yaml')
DB_CONFIG = os.path.join(BASE_DIR, 'config/dbConfig.yaml')

# 获取运行配置信息
RC = {'interval': 1, "project_name": 1}
INTERVAL = RC['interval']
PROJECT_NAME = RC['project_name']

# 虚假请求头
FAKE_HEADERS = random.choice(json.loads(open(os.path.join(BASE_DIR, 'config/fakeHeaders.json'), 'r').read())['Headers'])

if __name__ == '__main__':
    print(FAKE_HEADERS)
