from setuptools import setup, find_packages


setup(
    name='pymdown-nomnoml',
    version='0.1.0',
    description='A PyMdown extension to format pymdown_nomnoml as an inline SVG',
    long_description='The pymdown-nomnoml provides a simple pymdown extension to automatically convert nomnoml'
                     'diagrams to inline images.',
    keywords='mkdocs pymdown nomnoml',
    url='https://github.com/shauser/pymdown-nomnoml/',
    author='Stephan Hauser',
    author_email='stephan@codefreeze.ch',
    license='MIT',
    python_requires='>=3.4',
    install_requires=[
        'pymdown-extensions'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    package_data={
        'pymdown_nomnoml': ['js/pymdown_nomnoml.js']
    }
)
