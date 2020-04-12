import jenkins
from jenkinsapi.jenkins import Jenkins
import yaml
from jenkinsclient import config
from os.path import exists, isfile


def get_jenkins_server(type='python-jenkins'):
    if exists(config.CONFIG_FILE_PATH) and isfile(config.CONFIG_FILE_PATH):
        stream = open(config.CONFIG_FILE_PATH, 'r')
    else:
        print('配置文件%s不存在，请先使用config generate命令生成' % config.CONFIG_FILE_PATH)
        exit()

    config_json = yaml.load(stream, Loader=yaml.FullLoader)

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
