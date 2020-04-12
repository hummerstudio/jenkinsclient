import platform
import os
import subprocess

CONFIG_TEMPLATE = """jenkins_servers:
- name: default
  url: http://localhost:8080/jenkins
  username: admin
  token: '1'
use: default
"""
CONFIG_FILE_PATH = os.environ['HOME'] + os.sep + '.jenkins_client.yaml'


class Config(object):
    """
    配置信息
    """
    def generate(self):
        """
        从模版生成配置文件
        :return:
        """
        with open(CONFIG_FILE_PATH, 'w') as config_file_object:
            config_file_object.write(CONFIG_TEMPLATE)

        system = platform.system()
        if system == 'Darwin':
            return_code = subprocess.call(['open', CONFIG_FILE_PATH])
            if return_code == 0:
                return '生成配置文件%s成功' % CONFIG_FILE_PATH
        elif system == 'Linux':
            return_code = subprocess.call(['vi', CONFIG_FILE_PATH])
            if return_code == 0:
                return '生成配置文件%s成功' % CONFIG_FILE_PATH
        elif system == 'Windows':
            return_code = os.startfile(CONFIG_FILE_PATH)
            if return_code == 0:
                return '生成配置文件%s成功' % CONFIG_FILE_PATH
