from setuptools import find_packages, setup


install_requires = [
    'wagtail>=2.0,<2.9',
]

testing_extras = [
    'coverage>=3.7.0',
    'model-mommy>=2.0.0',
]

setup(
    name='wagtail-copyablemodeladmin',
    url='https://github.com/cfpb/wagtail-copyablemodeladmin',
    author='CFPB',
    author_email='tech@cfpb.gov',
    description='Copyable ModelAdmins for Django models used on Wagtail Sites',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    license='CC0',
    version='1.1.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
