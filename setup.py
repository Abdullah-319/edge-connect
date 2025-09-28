from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="edge-connect-face-reconstruction",
    version="1.0.0",
    author="ABDULLAH AHMAD",
    author_email="your.email@example.com",
    description="EdgeConnect-inspired face reconstruction for inpainting masked facial regions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction",
    project_urls={
        "Bug Reports": "https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/issues",
        "Source": "https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction",
        "Documentation": "https://github.com/ABDULLAH-AHMAD-OFFICIAL/edge-connect-face-reconstruction/wiki",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "isort>=5.0",
            "jupyter>=1.0",
            "notebook>=6.0",
        ],
        "gpu": [
            "torch>=1.9.0+cu111",
            "torchvision>=0.10.0+cu111",
        ],
    },
    entry_points={
        "console_scripts": [
            "face-reconstruct=scripts.process_user_image:main",
            "face-test=scripts.test_reconstruction:main",
        ],
    },
    keywords="computer-vision image-inpainting face-reconstruction edge-connect deep-learning",
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
)