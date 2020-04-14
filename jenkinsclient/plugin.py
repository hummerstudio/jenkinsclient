import json
import requests
from jenkinsapi.utils.jsonp_to_json import jsonp_to_json
from jenkinsclient import jenkins_server


class Plugin(object):
    """
    Jenkins插件相关操作
    """
    def has(self, plugin_name):
        """
        查看插件是否已安装
        """
        server = jenkins_server.get_jenkins_server(type='jenkinsapi')
        has = server.has_plugin(plugin_name)
        if has:
            return '插件%s已安装' % plugin_name
        else:
            return '插件%s未安装' % plugin_name

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

    def search(self, key_word):
        """
        搜索插件
        """
        server = jenkins_server.get_jenkins_server(type='jenkinsapi')
        update_center = 'http://updates.jenkins-zh.cn/update-center.json'
        jsonp = requests.get(update_center).content.decode('utf-8')
        update_center_plugins_dict = json.loads(jsonp_to_json(jsonp))['plugins']
        plugin_names = update_center_plugins_dict.keys()
        for plugin_name in plugin_names:
            if key_word in plugin_name:
                print('%s%s- %s' % (plugin_name.ljust(50),
                                   update_center_plugins_dict[plugin_name]['version'].ljust(10),
                                   update_center_plugins_dict[plugin_name]['excerpt']))

    def uninstall(self, plugin_name):
        """
        卸载插件
        """
        server = jenkins_server.get_jenkins_server()
        server.delete_plugin(plugin_name)
        return '插件%s卸载成功' % plugin_name
