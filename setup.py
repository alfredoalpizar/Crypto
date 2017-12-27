from setuptools import setup

setup(
    name="crypto",
    version='0.2',
    py_modules=['crypto'],
    install_requires=[
        'click', 'requests', 'terminaltables',
    ],
    entry_points='''
        [console_scripts]
        crypto=crypto:cli
    ''',
)
