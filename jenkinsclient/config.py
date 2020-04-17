"""
Copyright (c) 2020 Tang Ming
jenkinsclient is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
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
CONFIG_FILE_PATH = os.environ['HOME'] + os.sep + '.jenkinsclient.yaml'


class Config(object):
    """
    配置信息
    """
    def generate(self):
        """
        生成配置文件模版
        """
        if os.path.exists(CONFIG_FILE_PATH):
            choice = input('配置文件%s已存在，确认要重新生成吗？y/n：' % CONFIG_FILE_PATH).lower()
            yes = {'yes', 'y', 'ye', ''}
            no = {'no', 'n'}
            if choice in yes:
                with open(CONFIG_FILE_PATH, 'w') as config_file_object:
                    config_file_object.write(CONFIG_TEMPLATE)
            else:
                return
        else:
            with open(CONFIG_FILE_PATH, 'w') as config_file_object:
                config_file_object.write(CONFIG_TEMPLATE)
            system = platform.system()
            if system == 'Darwin':
                return_code = subprocess.call(['open', CONFIG_FILE_PATH])
                if return_code == 0:
                    return '生成配置文件%s成功，请在打开的编辑器中修改并保存。' % CONFIG_FILE_PATH
            elif system == 'Linux':
                return_code = subprocess.call(['vi', CONFIG_FILE_PATH])
                if return_code == 0:
                    return '配置文件%s保存成功' % CONFIG_FILE_PATH
            elif system == 'Windows':
                return_code = os.startfile(CONFIG_FILE_PATH)
                if return_code == 0:
                    return '生成配置文件%s成功，请在打开的编辑器中修改并保存。' % CONFIG_FILE_PATH

    def get(self, item):
        """
        获取配置项的值
        """
        if item=='url':
            return

    def edit(self):
        """
        修改配置文件
        :return:
        """
        if os.path.exists(CONFIG_FILE_PATH):
            system = platform.system()
            if system == 'Darwin':
                return_code = subprocess.call(['open', CONFIG_FILE_PATH])
                if return_code == 0:
                    return '配置文件%s已在编辑器中打开，请修改并保存。' % CONFIG_FILE_PATH
            elif system == 'Linux':
                return_code = subprocess.call(['vi', CONFIG_FILE_PATH])
                if return_code == 0:
                    return '配置文件%s保存成功' % CONFIG_FILE_PATH
            elif system == 'Windows':
                return_code = os.startfile(CONFIG_FILE_PATH)
                if return_code == 0:
                    return '配置文件%s已在编辑器中打开，请修改并保存。' % CONFIG_FILE_PATH
        else:
            return '配置文件%s不存在，可使用jenkins config generate命令生成配置文件模版' % CONFIG_FILE_PATH

    def ls(self):
        """
        显示配置信息
        """
        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH, 'r') as config_file_object:
                return config_file_object.read()
        else:
            return '配置文件%s不存在，可使用jenkins config generate命令生成配置文件模版' % CONFIG_FILE_PATH

