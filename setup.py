from setuptools import setup, find_packages

setup(name='risk',
      version='0.1',
      license='GNU GPLv3 or posterior',
      description='',
      url='https://github.com/BielStela/Risketos',
      author='Biel Stela Ballester, Guillem Duràn Ballester',
      author_email='biel.stela@gmail.com',
      packages=find_packages(),
      package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.yaml', '*.yml', '*.csv'],
        },
)