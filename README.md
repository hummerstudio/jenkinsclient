[![Build Status](https://img.shields.io/travis/com/hummerstudio/jenkinsclient/master?logo=travis)](https://travis-ci.com/hummerstudio/jenkinsclient)

# JenkinsClient

A powerful cross-platform Jenkins command-line client which supports multiple instances of Jenkins.

# Features

- Get global info
    - get Jenkins server info
    - get whoami info
    - get plugins info
    - get nodes info
    - get jobs info
    - get queues info
- Operating Jenkins objects
    - Plugin
        - list, search, install, uninstall plugin, and many more operations
    - Node
        - list, get node info and many more operations
    - Executor
        - get the number of node's executors, and many more operations
    - Job 
        - list, build, copy, create, delete, disable, enable, rename job, and many more operations
    - Queue
        - list and cancel queue
    - Build
        - get env_vars, information, log and test report of build
    

# Install

You can use pip to install jenkinsclient on PyPI, just execute following command:

`pip3 install jenkinsclient`

or manually download the source code and use setuptools:

`python setup.py install`

# Upgrade

`pip3 install -U jenkinsclient`

# Releases

[https://pypi.org/project/jenkinsclient/](https://pypi.org/project/jenkinsclient/)

# Usage

After install jenkinsclient, you can use command `jenkins` to perform many operations on Jenkins server.

## QUICK START

1. Use `jenkins config generate` to config jenkins servers.

This command will generate a config file, you can modify it by yourself.

1. Do what you want.

try `jenkins jobs` to see all jobs on your jenkins server.

try `jenkins plugins` to see all plugins on your jenkins server.

## Help information

Type `jenkins` to show jenkinsclient help information, or `jenkins GROUP` to view group command help information, such as `jenkins config`, `jenkins job`.like this:

```
NAME
    jenkins - Jenkins命令行客户端

SYNOPSIS
    jenkins GROUP | COMMAND

DESCRIPTION
    Jenkins命令行客户端

GROUPS
    GROUP is one of the following:

     build
       Jenkins构建相关操作

     config
       配置信息

     executor
       Jenkins执行器相关操作

     job
       Jenkins任务相关操作

     node
       Jenkins节点相关操作

     plugin
       Jenkins插件相关操作

     queue
       Jenkins队列相关操作

COMMANDS
    COMMAND is one of the following:

     jobs
       显示任务列表

     nodes
       显示节点列表

     plugins
       显示插件列表

     queues
       查看队列

     version
       显示Jenkins服务器版本号

     whoami
       显示当前用户
```
