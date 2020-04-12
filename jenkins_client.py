import fire
from jenkinsclient.config import Config
from jenkinsclient.job import Job
from jenkinsclient.plugin import Plugin
from jenkinsclient import jenkins_server


class JenkinsClient(object):
    """
    Jenkins命令行客户端
    """
    def __init__(self):
        self.config = Config()
        self.job = Job()
        self.plugin = Plugin()

    def jobs(self):
        """
        显示任务列表
        """
        return Job().ls()

    def plugins(self):
        """
        显示插件列表
        """
        return Plugin().ls()

    def whoami(self):
        """
        显示当前用户
        """
        server = jenkins_server.get_jenkins_server()
        try:
            i = server.get_whoami()
        except Exception as e:
            return '操作失败：连接服务器失败'
        return i['fullName']


def main():
    fire.Fire(JenkinsClient)


if __name__ == '__main__':
    main()
