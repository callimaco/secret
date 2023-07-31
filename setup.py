from setuptools import setup

setup(
    name='secret',
    version='0.1.0',
    packages=['secret', 'secret.secret_man', 'secret.secret_man.low_db'],
    package_dir={'': 'src'}
)
