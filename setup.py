from setuptools import setup

setup(
  name='pycritty',
  version='0.1.0',
  author='Miguel Hernández',
  py_modules=['nesting'],
  install_requires=[
    'Click'
  ],
  entry_points={
    'console_scripts': [
      'pycritty = nesting:cli'
    ]
  }
)
