from setuptools import setup, find_packages

setup(
  name='pycritty',
  version='0.1.0',
  author='Miguel Hernández',
  include_package_data=True,
  packages=find_packages(),
  install_requires=[
    'Click'
  ],
  entry_points={
    'console_scripts': [
      'pycritty = pycritty.scripts.greet:cli'
    ]
  }
  # py_modules=['nesting'],
)
