from setuptools import setup

setup(
    name="crypto",
    version='0.1',
    py_modules=['Crypto'],
    install_requires=[
        'click', 'requests',
    ],
    entry_points='''
        [console_scripts]
        crypto=Crypto:cli
    ''',
)

