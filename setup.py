from setuptools import find_packages, setup
import typing as List

#since we have `-e . in the requirements.txt which was to trigerred setup.py but
# we dont want it to be used in the requirements while using the list for downlaoding the 
# library so we will use some condition before for this`

Hypen_e_dot = '-e .'

def get_requirements(file_path:str) ->List[str]:
    '''
        this function will returns list, we will strings as library name 
    
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if Hypen_e_dot in requirements:
              requirements.remove(Hypen_e_dot)
    return requirements


setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'Braino_G',
    author_email = 'codbits1001@icloud.com',
    packages = find_packages(),
    # install_requires = ['pandas, numpy, seaborn'], # since we can have many packages instead of manually passing as the list, we created the helper functions for this
    install_requires = get_requirements('requirements.txt')

)

