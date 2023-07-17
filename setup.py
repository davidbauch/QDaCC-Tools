from setuptools import setup

setup(
   name='QDLC Tools',
   version='1.0.1',
   author='David Bauch  ',
   author_email='dbauch@mail.upb.de',
   packages=['QDLC','QDLC.plot_tools', 'QDLC.eval_tools', 'QDLC.misc', 'QDLC.cluster', 'QDLC.gui'],
   description='Tools for QDLC',
   install_requires=[
       "matplotlib",
       "numpy",
       "pytest",
       "parse",
   ],
   include_package_data=True,
   package_data={'': ['misc/colormaps/**', 'gui/gui/resources/**']},
)