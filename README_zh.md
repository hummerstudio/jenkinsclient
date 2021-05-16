[![Build Status](https://img.shields.io/travis/com/hummerstudio/jenkinsclient/master?logo=travis)](https://travis-ci.com/hummerstudio/jenkinsclient)

# JenkinsClient

Jenkinsclient是一个功能强大的、开源的、跨平台的、支持多实例的`Jenkins`命令行客户端。

# 功能

- 获取全局信息
    - 获取Jenkins服务器信息
    - 获取当前用户信息（`whoami`）
    - 获取插件（`plugins`）信息
    - 获取节点（`nodes`）信息
    - 获取任务（`jobs`）信息
    - 获取队列（`queues`）信息
- 操作Jenkins对象
    - 插件
        - 列出、搜索、安装、卸载插件，以及更多其他操作
    - 节点
        - 列出、获取节点信息以及更多其他操作
    - 执行器（`Executor`）
        - 获取节点执行器的数量以及更多其他操作
    - 任务 
        - 列出、构建、复制、创建、删除、禁用、启用、重命名任务以及更多其他操作
    - 队列
        - 列出并取消队列项目
    - 构建
        - 获取构建的环境变量、信息、日志和测试报告等
    

# 安装

您可以使用`pip`在`PyPI`上安装`jenkinsclient`，只需执行以下命令：

`pip3 install jenkinsclient`

或手动下载源代码并使用`setuptools`工具安装，在源码根目录执行以下命令：

`python setup.py install`

# 升级

`pip3 install -U jenkinsclient`

# 发布

[https://pypi.org/project/jenkinsclient/](https://pypi.org/project/jenkinsclient/)

# 使用

安装`jenkinsclient`后, 你可以使用命令`jenkins` 或`jks` 来对Jenkins服务器执行很多操作。

## 快速开始

1. 使用 `jenkins config generate` 来配置Jenkins服务器.

    该命令将生成一个配置文件，您可以自己修改它。

1. 做你想做的操作.

尝试 `jenkins jobs` 以查看jenkins服务器上的所有任务。

尝试 `jenkins plugins` 以查看jenkins服务器上的所有插件.

小技巧：所有的命令中，都可以将`jenkins`替换为`jks`，以简化输入。

## 帮助信息

输入 `jenkins` 以显示 `jenkinsclient` 的帮助信息, 或者输入 `jenkins <GROUP>` 以查看组命令的帮助信息, 例如 `jenkins config`, `jenkins job`。输出类似这样：

```
NAME
    jks - 功能强大的跨平台Jenkins命令行客户端

SYNOPSIS
    jks GROUP | COMMAND

DESCRIPTION
    功能强大的跨平台Jenkins命令行客户端

GROUPS
    GROUP is one of the following:

     build
       Jenkins构建相关操作

     config
       配置Jenkins服务器信息

     cred
       管理Jenkins凭据

     executor
       管理Jenkins执行器

     job
       管理Jenkins任务

     node
       管理Jenkins节点

     plugin
       管理Jenkins插件

     queue
       管理Jenkins队列
COMMANDS
    COMMAND is one of the following:

     app
       APP模式——在独立窗口中操作Jenkins

     creds
       显示凭据列表

     jobs
       显示任务列表

     nodes
       显示节点列表

     plugins
       显示插件列表

     queues
       显示队列

     version
       显示Jenkins服务器版本号

     whoami
       显示当前用户
```
