[![Build Status](https://img.shields.io/travis/com/hummerstudio/jenkinsclient/master?logo=travis)](https://travis-ci.com/hummerstudio/jenkinsclient)

# JenkinsClient

A powerful cross-platform Jenkins command line client which supports multiple instances of Jenkins.

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
        - list and cancel queue item
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
    jenkins - A powerful cross-platform Jenkins command line client

SYNOPSIS
    jenkins GROUP | COMMAND

DESCRIPTION
    A powerful cross-platform Jenkins command line client

GROUPS
    GROUP is one of the following:

     build
       Manage builds

     config
       Configure Jenkins server information

     cred
       Manage Jenkins credentials

     executor
       Manage Jenkins executors

     job
       Manage Jenkins jobs

     node
       Manage Jenkins nodes

     plugin
       Manage Jenkins plugins

     queue
       Manage Jenkins queue

COMMANDS
    COMMAND is one of the following:

     app
       app mode, operating jenkins in a window

     creds
       List Credentials

     jobs
       List jobs

     nodes
       List nodes

     plugins
       List plugins

     queues
       List queues

     version
       Display Jenkins server version

     whoami
       Display who am i
```
