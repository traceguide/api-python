from setuptools import setup, find_packages

setup(
    name='lightstep',
    version='1.0.32',
    description='Official LightStep Python OpenTracing Implementation',
    long_description='',
    author='Resonance Labs, Inc.',
    license='',
    install_requires=['thrift==0.9.2',
                      'opentracing==0.5.2',
                      'jsonpickle'],
    tests_require=['sphinx',
                   'sphinx-epytext'],

    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        # 'Programming Language :: Python :: 3',
    ],

    keywords='traceguide',
    packages=find_packages(exclude=['docs*', 'tests*', 'sample*']),
)
