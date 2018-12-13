from setuptools import setup

import aiolambda

with open('requirements.txt') as f:
    requirements = f.read().strip().split('\n')

with open('requirements_test.txt') as f:
    requirements_test = f.read().strip().split('\n')[1:]


def read_file(file_name):
    """Read file and return its contents."""
    with open(file_name, 'r') as f:
        return f.read()


if __name__ == '__main__':
    setup(name='aiolambda',
          version=aiolambda.__version__,
          description='Python async microservices fasts!',
          long_description=read_file('README.md'),
          long_description_content_type='text/markdown',
          classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Programming Language :: Python :: 3.7',
            'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
            'Intended Audience :: Developers',
          ],
          keywords='aiolambda asyncio aiohttp asyncpg aio-pika',
          url='http://github.com/pando85/aiolambda',
          author='Pando85',
          author_email='pand855@gmail.com',
          license='GPLv3+',
          packages=['aiolambda',
                    'aiolambda-cli'],
          scripts=['bin/aiolambda-cli'],
          install_requires=requirements,
          include_package_data=True,
          tests_require=requirements_test,
          zip_safe=False)
