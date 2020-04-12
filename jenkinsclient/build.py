from jenkins import JenkinsException
from jenkinsclient import jenkins_server


class Build(object):
    """
    Jenkins构建相关操作
    """
    def env(self, job_name, build_number):
        """
        显示构建环境变量
        """
        server = jenkins_server.get_jenkins_server()
        try:
            env = server.get_build_env_vars(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return env

    def log(self, job_name, build_number):
        """
        显示构建日志
        """
        server = jenkins_server.get_jenkins_server()
        try:
            console_text = server.get_build_console_output(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return console_text

    def info(self, job_name, build_number):
        """
        显示构建信息
        """
        server = jenkins_server.get_jenkins_server()
        try:
            build_info = server.get_build_info(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return build_info

    def report(self, job_name, build_number):
        """
        显示构建测试报告
        """
        server = jenkins_server.get_jenkins_server()
        try:
            report = server.get_build_test_report(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return report
