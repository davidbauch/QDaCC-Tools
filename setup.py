from setuptools import setup

setup(
   name='QDLC Tools',
   version='1.0.1',
   author='David Bauch  ',
   author_email='dbauch@mail.upb.de',
   packages=['QDLC','QDLC.plot_tools', 'QDLC.eval_tools', 'QDLC.misc', 'QDLC.cluster'],
   #scripts=['bin/script1','bin/script2'],
   #url='http://pypi.python.org/pypi/PackageName/',
   #license='LICENSE.txt',
   description='Tools for QDLC',
   #long_description=open('README.txt').read(),
   install_requires=[
       "matplotlib",
       "numpy",
       "pytest",
       "parse",
   ],
   include_package_data=True,
   package_data={'': ['misc/colormaps/**']},
)