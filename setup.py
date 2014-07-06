try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='simpleversions',
    version='0.1.4',
    description='Library that performs simple version comparison operations',
    url='https://github.com/amplify-education/simpleversions',
    py_modules=['simpleversions'],
    zip_safe=False,
)
