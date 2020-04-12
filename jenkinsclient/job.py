from jenkins import JenkinsException
from jenkinsclient import jenkins_server

class Job(object):
    """
    Jenkins任务相关操作
    """

    def build(self, job_name, parameters=None):
        """
        构建任务
        """
        server = jenkins_server.get_jenkins_server()
        build_number = server.build_job(job_name, parameters=parameters)
        return '任务%s已触发，构建号：%d' % (job_name, build_number)

    def copy(self, from_name, to_name):
        """
        复制任务
        """
        server = jenkins_server.get_jenkins_server()
        try:
            server.copy_job(from_name, to_name)
        except Exception as e:
            return '复制任务%s到%s失败' % (from_name, to_name)
        return '复制任务%s到%s成功' % (from_name, to_name)

    def delete(self, job_name):
        """
        删除任务
        """
        server = jenkins_server.get_jenkins_server()
        try:
            server.delete_job(job_name)
        except JenkinsException as e:
            return '删除任务' + job_name + '失败'
        return '删除任务%s成功' % job_name

    def disable(self, job_name):
        """
        禁用任务
        """
        server = jenkins_server.get_jenkins_server()
        server.disable_job(job_name)
        return '禁用任务%s成功' % job_name

    def enable(self, job_name):
        """
        启用任务
        """
        server = jenkins_server.get_jenkins_server()
        server.enable_job(job_name)
        return '启用任务%s成功' % job_name

    def exists(self, job_name):
        """
        判断任务是否存在
        """
        server = jenkins_server.get_jenkins_server()
        exists = server.job_exists(job_name)
        if exists:
            return '任务%s存在' % job_name
        else:
            return '任务%s不存在' % job_name

    def info(self, job_name):
        """
        显示任务信息
        """
        server = jenkins_server.get_jenkins_server()
        job_info = server.get_job_info(job_name)
        return job_info

    def ls(self):
        """
        显示任务列表
        """
        server = jenkins_server.get_jenkins_server()
        job_list_content = '任务名称'.ljust(26) + '类型'.ljust(28) + '链接\n'
        job_list_content += '--------'.ljust(30) + '--------'.ljust(30) + '--------\n'
        all_jobs = server.get_all_jobs()
        for job in all_jobs:
            job_list_content += job['fullname'].ljust(30) + job['_class'].split('.')[-1].ljust(30) + job['url'] + '\n'
        return job_list_content

    def rename(self, from_name, to_name):
        """
        重命名任务
        """
        server = jenkins_server.get_jenkins_server()
        try:
            server.rename_job(from_name, to_name)
        except JenkinsException as e:
            return '重命名%s为%s失败，错误信息：%s' % (from_name, to_name, str(e))
        return '重命名%s为%s成功' % (from_name, to_name)
