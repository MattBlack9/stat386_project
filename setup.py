from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name = 'collegefood',                               
    version='0.0.1',                                   
    description = 'Package to aid in the analysis of a dataset found on https://www.kaggle.com/datasets/borapajo/food-choices',            # Describe your package
    author = 'Matthew Jensen, Matthew Blackley',                             
    author_email = 'mj638@byu.edu',               
    url = 'git@github.com:MattBlack9/stat386_project.git',  
    packages = find_packages(),  
                                                        # Automatically find all packages
    install_requires = requirements,                    # Package dependences
    classifiers = [                                     # Add package classifiers (OPTIONAL)
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    long_description = long_description,                # Use README content as long_description
    long_description_content_type = 'text/markdown',    # Specify the content type
    #package_data = {'collegefood': ['STAT386_PROJECT/college_food.csv']}, # Dataset to include in package
)

