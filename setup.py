from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',  # Ensure the requests library is installed
    ],
    description="A package for emotion detection using Watson NLP",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://your-package-url.com",
)
