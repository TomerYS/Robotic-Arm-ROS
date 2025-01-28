import os
from setuptools import find_packages, setup

package_name = 'description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Install the package.xml
        ('share/' + package_name, ['package.xml']),
        # Install the URDF and mesh files
        ('share/' + package_name + '/urdf', ['urdf/my_rover.urdf']),
        ('share/' + package_name, [
            'meshes/base_link.STL',
            'meshes/end_effector.STL',
            'meshes/link_1.STL',
            'meshes/link_2.STL',
            'meshes/link_3.STL',
            'meshes/link_4.STL',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tauver',
    maintainer_email='tauver@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)


