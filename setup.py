from setuptools import setup, find_packages

setup(
    name='ck-selenium-python',
    version='0.1.0',
    description='Setting up python package for web testing',
    author='Vivek Biswas',
    author_email='vivek.biswas@cloudkaptan.com',
    url='https://github.com/vivek-ck/ck-selenium-python.git',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'seleniumbase',
    ],
    extras_require={},
    entry_points={
        'console_scripts': ['my-command=src.features:main']
    },
    package_data={'ck-selenium-python': ['data/schema.json']}
)