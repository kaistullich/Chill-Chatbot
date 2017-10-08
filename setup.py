from distutils.core import setup

setup(
    name='weather-chatbot',
    version='1.0.0',
    packages=[''],
    url='https://github.com/kaistullich/weather-chatbot',
    license='MIT',
    author='Kai Stullich',
    author_email='kairstullich@gmail.com',
    description='A chatbot for getting weather information and if you just want to have some small talk.',
    requires=['flask', 'rivescript', 'pyowm']
)
