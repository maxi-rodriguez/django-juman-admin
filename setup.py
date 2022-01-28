#!/usr/bin/env python

from setuptools import setup, find_packages
from juman_admin import VERSION

github_url = 'https://github.com/maxi-89/django-juman-admin'
long_desc = '''
%s

%s
''' % (open('README').read(), open('CHANGELOG').read())

setup(
    name='django-juman-admin',
    version=VERSION.replace(' ', '-'),
    description='A juman theme for the django admin site',
    long_description=long_desc,
    author='Maximiliano Rodriguez',
    author_email='maxi.rodriguez.3105@gmail.com',
    url=github_url,
    download_url='%s/archive/%s.tar.gz' % (github_url, VERSION),
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
)