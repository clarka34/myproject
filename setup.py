import os
from distutils.core import setup

opts = dict(name='clarka34',
            description='my project for UWSEDS',
            packages=['myproject','myproject/tests']
            )

if __name__ == '__main__':
    setup(**opts)
