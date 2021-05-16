"""
Copyright (c) 2021 Tang Ming
jenkinsclient is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import locale
import os
import platform

import requests
from requests.exceptions import ConnectionError


class Core(object):
    """Manage Jenkins War Packages"""
    def download(self, version='latest'):
        """Download Jenkins war package"""
        JENKINS_WAR_PACKAGE_URL= 'https://get.jenkins.io/war-stable/'
        url = JENKINS_WAR_PACKAGE_URL + version + '/jenkins.war'
        try:
            print('正在从%s下载...' % url)
            war_file = requests.get(url, allow_redirects=True)
            if platform.system() == 'Windows':
                HOME_PATH = os.environ['HOMEPATH']
            else:
                HOME_PATH = os.environ['HOME']
            open(HOME_PATH + os.sep + '/jenkins.war', 'wb').write(war_file.content)
        except ConnectionError as e:
            return 'Error: %s' % str(e)
        return 'jenkins.war已下载到目录%s，你可以使用"jenkins core start"命令启动' % HOME_PATH

    def start(self):
        """start jenkins"""
        os.system("java -jar ~/jenkins.war")


if locale.getdefaultlocale()[0] == 'zh_CN':
    Core.__doc__ = '管理Jenkins war包'
    Core.download.__doc__ = '下载Jenkins war包'
    Core.start.__doc__ = '启动Jenkins'
