import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="geonode_cdu",
    version="0.2",
    author="",
    author_email="",
    description="geonode_cdu, based on GeoNode",
    long_description=(read('README.rst')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="geonode_cdu geonode django",
    url='https://github.com/geonode_cdu/geonode_cdu',
    packages=['geonode_cdu',],
    include_package_data=True,
    zip_safe=False,
)
