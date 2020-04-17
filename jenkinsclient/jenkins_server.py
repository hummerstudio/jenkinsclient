"""
Copyright (c) 2020 Tang Ming
jenkinsclient is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import jenkins
from jenkinsapi.jenkins import Jenkins
import yaml
from jenkinsclient import config
from os.path import exists, isfile


def get_jenkins_server(type='python-jenkins'):

    config_json = get_config_json()

    try:
        jenkins_servers = config_json['jenkins_servers']
        use = config_json['use']
    except KeyError as e:
        print('配置文件格式不正确，缺少%s字段' % str(e))
        exit()

    for server in jenkins_servers:
        if server['name'] == use:
            url = server['url']
            username = server['username']
            token = server['token']
    if type == 'python-jenkins':
        server = jenkins.Jenkins(url, username=username, password=token, timeout=30)
    else:
        server = Jenkins(url, username=username, password=token, timeout=30)
    return server


def get_config_json():
    if exists(config.CONFIG_FILE_PATH) and isfile(config.CONFIG_FILE_PATH):
        stream = open(config.CONFIG_FILE_PATH, 'r')
    else:
        print('配置文件%s不存在，请先使用config generate命令生成' % config.CONFIG_FILE_PATH)
        exit()
    config_json = yaml.load(stream, Loader=yaml.FullLoader)
    return config_json


def get_url():
    config_json = get_config_json()

    try:
        jenkins_servers = config_json['jenkins_servers']
        use = config_json['use']
    except KeyError as e:
        print('配置文件格式不正确，缺少%s字段' % str(e))
        exit()

    for server in jenkins_servers:
        if server['name'] == use:
            url = server['url']
    return url


def get_blue_url():
    return get_url() + '/blue/organizations/jenkins'
