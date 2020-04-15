from jenkinsclient import jenkins_server


class Executor(object):
    """
    Jenkins执行器相关操作
    """

    def num(self, node_name):
        """
        查看节点执行器个数
        """
        server = jenkins_server.get_jenkins_server(type="jenkinsapi")
        if node_name == 'master':
            node_name = '(master)'
        executors = server.get_executors(node_name)
        print('执行器个数为: %d' % executors.count)