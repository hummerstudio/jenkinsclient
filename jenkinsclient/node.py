from jenkinsclient import jenkins_server


class Node(object):
    """
    Jenkins节点相关操作
    """

    def ls(self):
        """
        查看节点列表
        :return:
        """
        server = jenkins_server.get_jenkins_server(type="jenkinsapi")
        nodes = server.nodes
        for key in nodes.keys():
            node = nodes[key]
            if node.name == 'master':
                print(node)
            else:
                print(node,
                      node.get_architecture(),
                      node.get_available_physical_memory(),
                      node.get_available_swap_space(),
                      node.get_labels())
