from setuptools import setup, find_packages

setup(
    name='code_quality_analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pylint',
        'radon',
        'streamlit',
        'openai',  # or 'transformers' if using Hugging Face
    ],
)
