
## to build your app as a package itself, hosted on PyPi

from setuptools import find_packages, setup
from typing import List


def get_requirements(filepath:str) -> List[str]:
    
    reqs = []
    with open(filepath, 'r') as opfile:
        reqs = opfile.readlines()
        reqs = [item.replace("\n", "") for item in reqs]
        if '-e .' in reqs:
            reqs.remove('-e .')
    
    return reqs



setup (
    name = 'MLProject',
    version = '0.0.1',
    author =  'Utsav Ajay',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)

## find_packages will build __init__.py in the src folder