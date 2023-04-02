from setuptools import find_packages,setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str):
    """
    This function will return list of requirements
    """
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines() # In requirements.txt the packages will be in the seaparate lines, readlines will read it line by line
        requirements = [req.replace('\n','') for req in requirements] # While reading line by line the \n will come at the end of each line we replace that

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # -e . will automatically get installed from requirements.txt to setup.py and we need not install it again over here

    return requirements
            
setup( 
    name='mlproject',
    version='0.0.1',
    author='Shrey',
    author_email='imshrey26@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'))