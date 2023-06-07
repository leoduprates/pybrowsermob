from setuptools import setup, find_packages

setup(
    name='pybrowsermob',
    version='0.1.0',
    description='A library for interacting with the Browsermob Proxy',
    author='David Burns',
    maintainer='Leonardo Duprates',
    url='https://github.com/leoduprates/pybrowsermob',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=find_packages(),
    install_requires=['requests>=2.9.1'],
)
