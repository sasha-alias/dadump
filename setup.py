from distutils.core import setup

setup(name='dadump',
      version='0.1',
      description='Daily dumps management for Postgresql',
      author='Sasha Aliashkevich',
      scripts=['dadump'],
      data_files=[('/etc/dadump', ['dadump.conf'])]
      )
