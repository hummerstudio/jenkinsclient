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

from jenkins import JenkinsException
from jenkinsclient import jenkins_server


class Build(object):
    """Manage builds"""
    def env(self, job_name, build_number):
        """Display env vars of a build"""
        server = jenkins_server.get_jenkins_server()
        try:
            env = server.get_build_env_vars(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return env

    def log(self, job_name, build_number):
        """Display log of a build"""
        server = jenkins_server.get_jenkins_server()
        try:
            console_text = server.get_build_console_output(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return console_text

    def info(self, job_name, build_number):
        """Display info of a build"""
        server = jenkins_server.get_jenkins_server()
        try:
            build_info = server.get_build_info(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return build_info

    def report(self, job_name, build_number):
        """Display test report of a build"""
        server = jenkins_server.get_jenkins_server()
        try:
            report = server.get_build_test_report(job_name, build_number)
        except JenkinsException as e:
            return '%s#%d不存在' % (job_name, build_number)
        return report


if locale.getlocale()[0] == 'zh_CN':
    Build.__doc__ = 'Jenkins构建相关操作'
    Build.env.__doc__ = '显示构建环境变量'
    Build.log.__doc__ = '显示构建日志'
    Build.info.__doc__ = '显示构建信息'
    Build.report.__doc__ = '显示构建测试报告'
