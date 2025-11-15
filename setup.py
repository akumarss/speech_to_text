from setuptools import setup, find_packages

setup(
    name="stt_call_summary",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "datasets",
        "torch",
        "torchaudio",
        "accelerate",
        "sentencepiece",
    ],
)
