import setuptools

setuptools.setup(
    name='schoology',
    version='1.2',
    author='Aarav Borthakur',
    author_email='gadhaguy13@gmail.com',
    description='The Ultimate Schoology CLI',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    url='https://gadhagod.github.io/schoology',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'click',
        'schoolopy'
    ],
    scripts=['./bin/schoology'],
    python_requires='>=3.6'
)