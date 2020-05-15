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


class Credentials(object):
    """
    Jenkins凭据相关操作
    """

    def ls(self):
        """
        查看凭据列表
        """
        server = jenkins_server.get_jenkins_server(type="jenkinsapi")
        credentials = server.get_credentials().credentials
        print('%s%s%s%s' % ('ID'.ljust(40), '名称'.ljust(30), '类型'.ljust(60), '描述'))
        for credential in credentials:
            print(credential.ljust(40), credentials[credential].displayname.ljust(30),
                  str(type(credentials[credential])).ljust(60),
                  credentials[credential].description)

