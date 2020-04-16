"""
Copyright (c) 2020 Tang Ming
jenkinsclient is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
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