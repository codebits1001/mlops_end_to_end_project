# Importing the necessary classes and functions from the setuptools

from setuptools import find_packages, setup
from typing import List

# lets create the function for this 

e_hyphen_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:

    # create the variables to save the strings 

    requirements = []

    # open the file which has been passed
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        # if e hypen is detected remove it 
        if e_hyphen_dot in requirements:
            requirements.remove(e_hyphen_dot)
    return requirements




setup(
    name  = 'mlops_project',
    version = '0.0.1',
    author = 'Braino_G',
    author_email = 'codebits1001@icloud.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)
