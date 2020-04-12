from jenkinsclient import jenkins_server
from jenkinsapi.plugins import Plugins

class Plugin(object):
    """
    Jenkins插件相关操作
    """
    def install(self, plugin_name):
        """
        安装插件
        :return:
        """
        server = jenkins_server.get_jenkins_server()
        restart_required = server.install_plugin(plugin_name)
        if restart_required:
            return '插件%s安装成功，重启后生效' % plugin_name
        else:
            return '插件%s安装成功并生效' % plugin_name

    def ls(self):
        """
        显示插件列表
        """
        server = jenkins_server.get_jenkins_server()
        plugins = server.get_plugins()
        plugins_list_content = '插件名称'.ljust(32) + '类型'.ljust(68) + '版本\n'
        plugins_list_content += '--------'.ljust(36) + '--------'.ljust(70) + '--------\n'
        for key in plugins.keys():
            plugins_list_content += key[0].ljust(36) + key[1].ljust(70) + plugins[key[0]]['version'] + '\n'
        return plugins_list_content

    # TODO: 解析update-center.json内容并搜索
    def search(self, plugin_name):
        """
        搜索插件
        """
        return '插件搜索功能尚未实现！'
