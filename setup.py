from distutils.core import setup

REQUIRES = [
    'records',
    'allure-pytest',
    'structlog',
    'requests',
    'pydantic'
]

setup(
    name='dm_api_account',
    version='0.0.3',
    packages=['dm_api_account', 'dm_api_account.apis', 'dm_api_account.models'],
    url='https://github.com/allezov/dm_api_account.git',
    license='Apache-2.0 license',
    author='lezov',
    author_email='-',
    install_requires=REQUIRES,
    description='dm_api_account'
)
