from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Edit below variables as per your requirements
REPO_NAME = "Anime_recommendation"
AUTHOR_USER_NAME = "akirakod"
SRC_REPO = "src"  # Adjust this if your source code is in a different directory
LIST_OF_REQUIREMENTS = [
    'streamlit',
    'numpy',
    'pandas',
    'matplotlib',
    'seaborn',
    'scikit-learn',
    'scipy',
    'requests',
    'openai',
    'pillow'
]

setup(
    name=REPO_NAME.lower(),  # Package name in lowercase
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email="yst1303@gmail.com",
    description="A small package for Anime Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=find_packages(where=SRC_REPO),  # Finds packages in the 'src' directory
    package_dir={"": SRC_REPO},  # Tells setuptools that packages are under 'src'
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS,
    include_package_data=True,  # Ensures non-code files are included if specified
)
