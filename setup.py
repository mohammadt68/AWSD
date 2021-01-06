from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='weightedspatiotemporaldistillation',
    version='0.1',
    install_requires=requirements,
    packages=['weightedspatiotemporaldistillation'],
    url='',
    license='MIT',
    author='',
    author_email='',
    description=''
)
