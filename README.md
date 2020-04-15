[![Build Status](https://img.shields.io/travis/com/hummerstudio/jenkinsclient/master?logo=travis)](https://travis-ci.com/hummerstudio/jenkinsclient)

# JenkinsClient

A powerful cross-platform Jenkins command-line client which supports multiple instances of Jennkins.

# Features

- Global info
    - get Jenkins server version
    - get whoami info
    - get plugins info
    - get node info
    - get jobs info
    - get queues info
- Object operations
    - Plugin
        - list, search, install, uninstall plugin, and many more operations
    - Job 
        - list, build, copy, create, delete, disable, enable, rename job, and many more operations
    - Queue
        - list and cancel queue
    - Build
        - get env_vars, information, log and test report of build
- ...
    

# Install

You can use pip to install jenkinsclient on PyPI, just execute following command:

`pip3 install jenkinsclient`

or manually download the source code and use setuptools:

`python setup.py install`

# Usage

After install jenkinsclient, you can use command `jenkins` to perform many operations on Jenkins server.

## QUICK START

1. Use `jenkins config generate` to config jenkins servers.

This command will generate a config file, you can modify it by yourself.

1. Do what you want.

try `jenkins jobs` to see all jobs on your jenkins server.

try `jenkins plugins` to see all plugins on your jenkins server.

## Help infomation

Type `jenkins` to show help infomation like this:

```
NAME
    jenkins - Jenkins命令行客户端

SYNOPSIS
    jenkins GROUP | COMMAND

DESCRIPTION
    Jenkins命令行客户端

GROUPS
    GROUP is one of the following:

     config
       配置信息

     job
       Jenkins任务相关操作

     plugin
       Jenkins插件相关操作

COMMANDS
    COMMAND is one of the following:

     jobs
       显示任务列表

     plugins
       显示插件列表

     whoami
       显示当前用户
```

## Command infomation

You can type `jenkins COMMAND` to view command infomation, such as `jenkins confg`, `jenkins job`.
