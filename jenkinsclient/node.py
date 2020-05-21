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


class Node(object):
    """Manage Jenkins nodes"""
    def info(self, node_name):
        """Display node information"""
        server = jenkins_server.get_jenkins_server()
        if node_name == 'master':
            node_name = '(master)'
        info = server.get_node_info(node_name)
        return info

    def ls(self):
        """List nodes"""
        server = jenkins_server.get_jenkins_server()
        nodes = server.get_nodes()
        print('%s%s%s%s%s%s' % ('节点名称'.ljust(27), '架构'.ljust(18), '可用交换空间'.ljust(16), '可用内存空间'.ljust(15),
                                           '可用临时空间'.ljust(15), '可用磁盘空间'.ljust(20)))
        print('%s%s%s%s%s%s' % ('--------'.ljust(30), '--------'.ljust(20), '--------'.ljust(20), '--------'.ljust(20),
                                '--------'.ljust(20), '--------'.ljust(20)))
        for node in nodes:
            if node['name'] == 'master':
                node['name'] = '(master)'
            # TODO: 修复jenkinsapi的bug后，可直接调用接口
            node_info = server.get_node_info(node['name'])

            architecture = node_info['monitorData']['hudson.node_monitors.ArchitectureMonitor']

            swap_space_monitor = node_info['monitorData']['hudson.node_monitors.SwapSpaceMonitor']
            available_swap_space = swap_space_monitor['availableSwapSpace']
            total_swap_space = swap_space_monitor['totalSwapSpace']
            available_physical_memory = swap_space_monitor['availablePhysicalMemory']
            total_physical_memory = swap_space_monitor['totalPhysicalMemory']

            temporary_space = node_info['monitorData']['hudson.node_monitors.TemporarySpaceMonitor']['size']

            disk_space = node_info['monitorData']['hudson.node_monitors.DiskSpaceMonitor']['size']

            clock_diff = node_info['monitorData']['hudson.node_monitors.ClockMonitor']['diff']

            swap_space = str(round(available_swap_space/1024/1024, 2)) + '/' + str(round(total_swap_space/1024/1024, 2)) + ' MB'
            physical_memory = str(round(available_physical_memory/1024/1024, 2))\
                              + '/' + str(round(total_physical_memory/1024/1024, 2)) + ' MB'

            temporary = str(round(temporary_space/1024/1024)) + ' MB'
            disk = str(round(disk_space/1024/1024)) + ' MB'

            print('%s%s%s%s%s%s' % (node['name'].ljust(30),
                                    architecture.ljust(20),
                                    swap_space.ljust(20),
                                    physical_memory.ljust(20),
                                    temporary.ljust(20),
                                    disk.ljust(20)))


if locale.getlocale()[0] == 'zh_CN':
    Node.__doc__ = '管理Jenkins节点'
    Node.info.__doc__ = '查看节点信息'
    Node.ls.__doc__ = '查看节点列表'
