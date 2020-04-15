import fire

from jenkinsclient.executor import Executor
from jenkinsclient.build import Build
from jenkinsclient.config import Config
from jenkinsclient.job import Job
from jenkinsclient.node import Node
from jenkinsclient.plugin import Plugin
from jenkinsclient import jenkins_server
from jenkinsclient.queue import Queue


class JenkinsClient(object):
    """
    Jenkins命令行客户端
    """
    def __init__(self):
        self.build = Build()
        self.config = Config()
        self.executor = Executor()
        self.job = Job()
        self.node = Node()
        self.plugin = Plugin()
        self.queue = Queue()

    def jobs(self):
        """
        显示任务列表
        """
        return Job().ls()

    def nodes(self):
        """
        显示节点列表
        """
        return Node().ls()

    def plugins(self):
        """
        显示插件列表
        """
        return Plugin().ls()

    def queues(self):
        """
        查看队列
        :return:
        """
        return Queue().ls()

    def version(self):
        """
        显示Jenkins服务器版本号
        """
        server = jenkins_server.get_jenkins_server(type='jenkinsapi')
        version = server.version
        return 'Jenkins server version: %s' % version

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
