from jenkinsclient import jenkins_server


class Node(object):
    """
    Jenkins节点相关操作
    """

    def ls(self):
        """
        查看节点列表
        """
        server = jenkins_server.get_jenkins_server(type="jenkinsapi")
        nodes = server.nodes
        for key in nodes.keys():
            node = nodes[key]
            if node.name == 'master':
                node.name = '(master)'
            # TODO: 后面三个数据的获取需要先修复jenkinsapi的bug
            print(node,
                  node.get_architecture(),
                  node.get_available_swap_space(),
                  node.get_temp_size(),
                  node.get_labels())

    def info(self, node_name):
        """
        查看节点信息
        """
        server = jenkins_server.get_jenkins_server()
        if node_name == 'master':
            node_name = '(master)'
        info = server.get_node_info(node_name)
        return info
