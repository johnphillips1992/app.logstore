from os.path import dirname, join

from setuptools import setup, find_packages



version = '14.5'


setup(
    name = 'tamu.coa.app.logstore',
    version = version,
    description = "User Profiles",
    long_description = open(join(dirname(__file__), 'README')).read() + "\n" +
                       open(join(dirname(__file__), 'HISTORY')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"],
    keywords = 'django alumni coa tamu',
    author = 'TAMU COA ITS',
    author_email = 'webadmin@arch.tamu.edu',
    url = 'http://webadmin.arch.tamu.edu',
    packages = find_packages(),
    namespace_packages = ['tamu', 'tamu.coa', 'tamu.coa.app' ],
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'beanstalkc',
        'PyYAML',
        'django-form-utils',
    ],
)
