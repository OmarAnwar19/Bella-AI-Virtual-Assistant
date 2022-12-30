from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Chloe-AI Virtual Assistant',
    version='0.1.0',
    long_description=readme,
    author='Omar Anwar',
    url='https://github.com/OmarAnwar19',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
