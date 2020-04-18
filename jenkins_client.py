"""
Copyright (c) 2020 Tang Ming
jenkinsclient is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import os

import fire
from jenkinsclient.executor import Executor
from jenkinsclient.build import Build
from jenkinsclient.config import Config
from jenkinsclient.job import Job
from jenkinsclient.node import Node
from jenkinsclient.plugin import Plugin
from jenkinsclient import jenkins_server
from jenkinsclient.queue import Queue


class JenkinsClient(object):
    """
    Jenkins命令行客户端
    """
    def __init__(self):
        self.build = Build()
        self.config = Config()
        self.executor = Executor()
        self.job = Job()
        self.node = Node()
        self.plugin = Plugin()
        self.queue = Queue()

    def app(self):
        """
        APP模式——在独立窗口中打开Jenkins
        """
        try:
            __import__('webview')
        except ModuleNotFoundError:
            print('APP模式为实验性功能，需要使用pywebview模块，将自动为你安装')
            return_code = os.system('pip3 install --quiet pywebview')
            if return_code != 0:
                print('自动安装pywebview失败！')
                exit(1)
            else:
                print('自动安装pywebview成功')

        import webview
        url = jenkins_server.get_blue_url()
        webview.create_window('Jenkins', url=url, width=1024, height=768, confirm_close=True, text_select=True)
        webview.start()

    def jobs(self):
        """
        显示任务列表
        """
        return Job().ls()

    def nodes(self):
        """
        显示节点列表
        """
        return Node().ls()

    def plugins(self):
        """
        显示插件列表
        """
        return Plugin().ls()

    def queues(self):
        """
        查看队列
        :return:
        """
        return Queue().ls()

    def version(self):
        """
        显示Jenkins服务器版本号
        """
        server = jenkins_server.get_jenkins_server(type='jenkinsapi')
        version = server.version
        return 'Jenkins server version: %s' % version

    def whoami(self):
        """
        显示当前用户
        """
        server = jenkins_server.get_jenkins_server()
        try:
            i = server.get_whoami()
        except Exception as e:
            return '操作失败：连接服务器失败'
        return i['fullName']


def main():
    fire.Fire(JenkinsClient)


if __name__ == '__main__':
    main()
