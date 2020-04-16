import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name='jenkinsclient',
    version='1.0.0',
    author="TangMing",
    author_email="hummerstudio@163.com",
    description="A powerful cross-platform Jenkins command-line client which supports multiple instances of Jennkins.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/hummerstudio/jenkinsclient',
    packages=setuptools.find_packages(),
    py_modules=['jenkins_client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mulan Permissive Software License，Version 2",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'fire', 'jenkinsapi', 'python-jenkins', 'PyYAML'
    ],
    entry_points='''
        [console_scripts]
        jenkins=jenkins_client:main
    '''
)