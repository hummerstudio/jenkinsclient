"""
Copyright (c) 2020 Tang Ming
jenkinsclient is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import locale

from jenkinsclient import jenkins_server


class Executor(object):
    """Manage Jenkins executors"""
    def num(self, node_name):
        """
        Display executor number of a node
        """
        server = jenkins_server.get_jenkins_server(type="jenkinsapi")
        if node_name == 'master':
            node_name = '(master)'
        executors = server.get_executors(node_name)
        print('执行器个数为: %d' % executors.count)


if locale.getlocale()[0] == 'zh_CN':
    Executor.__doc__ = '管理Jenkins执行器'
    Executor.num.__doc__ = '显示节点执行器个数'
