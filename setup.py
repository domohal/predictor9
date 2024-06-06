from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith(HYPHEN_E_DOT)]

    return requirements


setup(
    name='predictor9',
    version='0.0.1',
    author='Dom OHalloran',
    author_email='dom.ohalloran86@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # This points to the function which looks in the requirement file
)
