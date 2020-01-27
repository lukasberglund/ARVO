from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ARVO',
    version='0.0.1',
    description='An AI that plays ultimate Tic Tac Toe',
    long_description=readme,
    author='Lukas Berglund',
    author_email='lukastberglund@gmail.com',
    url='https://github.com/lukasberglund/ARVO',
    license=license,
    packages=find_packages()
)
