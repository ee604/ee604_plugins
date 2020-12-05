from setuptools import setup

requirements = ['pytube']

setup(
    name="ee604_plugins",
    packages=['ee604_plugins'],
    install_requires=requirements,
    version="0.4.2",
    description='Plugins to download dataset and some supported functions',
    author = 'Shashi Kant Gupta',
    author_email = 'shashikg.iitk@gmail.com',
)
