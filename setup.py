from setuptools import setup

from cuba_weather_owm import __version__

setup(
    name='cuba_weather_owm',
    version=__version__,
    packages=[
        'cuba_weather_owm',
        'cuba_weather_owm/data_providers',
        'cuba_weather_owm/models',
        'cuba_weather_owm/repositories',
        'cuba_weather_owm/utils'
    ],
    url='https://github.com/cuba-weather/cuba-weather-owm-python',
    license='MIT',
    author='Cuban Open Source Community',
    description='Python3 client for cuba-weather project using openweathermap',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['cuba-weather-municipality', 'pyowm'],
)
