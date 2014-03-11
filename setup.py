from distutils.core import setup

setup(
        name = 'testimg',
        version = '0.0.1',
        author = 'Madison McGaffin',
        author_email = 'greyhill@gmail.com',
        packages = [ 'testimg' ],
        scripts = [],
        url = '',
        description = 'Image processing standard test images',
        include_package_data = True,
        install_requires = [
            'numpy'
            ]
        )

