import setuptools

setuptools.setup(
    name='jenkinsclient',
    version='0.1',
    author="TangMing",
    author_email="hummerstudio@163.com",
    description="A powerful Jenkins command line client.",
    packages=setuptools.find_packages(),
    py_modules=['jenkins_client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'fire', 'requests', 'jenkins', 'PyYAML'
    ],
    entry_points='''
        [console_scripts]
        jenkins=jenkins_client:main
    '''
)