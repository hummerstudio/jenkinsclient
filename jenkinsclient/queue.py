from jenkinsclient import jenkins_server


class Queue(object):
    """
    Jenkins队列相关操作
    """
    def cancle(self, queue_id):
        """
        取消队列中任务
        :return:
        """
        server = jenkins_server.get_jenkins_server()
        try:
            server.cancel_queue(queue_id)
        except Exception as e:
            return '取消队列中任务%d失败' % queue_id
        return '取消队列中任务%d成功' % queue_id

    def ls(self):
        """
        查看队列
        :return:
        """
        server = jenkins_server.get_jenkins_server()
        queue = server.get_queue_info()
        print('任务ID\t%s\t原因' % '任务链接'.ljust(50))
        for q in queue:
            print('%d\t%s\t%s' % (q['id'], q['task']['url'].ljust(50), q['why']))
