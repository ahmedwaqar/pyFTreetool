import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyFTree", # Replace with your own username
    version="0.1",
    author="Waqar Ahmed",
    author_email="ahmedwaqardr@gmail.com",
    description="An open source tools for FTA",
    # long_description=long_description,
    # long_description_content_type="TODO",
    # url="https://github.com/ahmedwaqar/pyFTreetool",
    # project_urls={
        # "Bug Tracker": "https://github.com/ahmedwaqar/pyFTreetool/issues",
    # },
    install_requires=[
        "networkx",
        ],
    scripts=[
        "src/pyFTree",
        ],
    python_requires=">=3.6",
)
