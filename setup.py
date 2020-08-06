from setuptools import setup

setup(
    name='num11',
    version='0.0.1',
    description='My private package from private github repo',
    url='https://github.com/PoojaDurai97/num11',
    author='Pooja Durai',
    author_email='poojadurai1997@gmail.com',
    license='unlicense',
    packages=['num11'],
    install_requires=[
       
        'pandas==0.23.3',
        'numpy>=1.14.5',
        
    ]
    
)