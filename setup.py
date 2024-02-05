from setuptools import find_packages, setup

package_name = 'cv_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='reid',
    maintainer_email='rgraves@andrew.cmu.edu',
    description='cv bridge camera publisher and subscriber',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = cv_basics.camera_publisher:main',
            'img_subscriber = cv_basics.video_subscriber:main',
        ],
    },
)
