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


class Queue(object):
    """Manage Jenkins queue"""
    def cancle(self, queue_id):
        """Cancel a task in queue"""
        server = jenkins_server.get_jenkins_server()
        try:
            server.cancel_queue(queue_id)
        except Exception as e:
            return '取消队列中任务%d失败' % queue_id
        return '取消队列中任务%d成功' % queue_id

    def ls(self):
        """List tasks in queue"""
        server = jenkins_server.get_jenkins_server()
        queue = server.get_queue_info()
        print('任务ID\t%s\t原因' % '任务链接'.ljust(50))
        for q in queue:
            print('%d\t%s\t%s' % (q['id'], q['task']['url'].ljust(50), q['why']))


if locale.getlocale()[0] == 'zh_CN':
    Queue.__doc__ = '管理Jenkins队列'
    Queue.cancle.__doc__ = '取消队列中任务'
    Queue.ls.__doc__ = '显示队列'
