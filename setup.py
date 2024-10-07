import setuptools

with open("README.md") as fh:
    long_description = fh.read()
    
setuptools.setup(name="OrderProcessingLibrary",
                 version="0.0.1",
                 author="Venkat",
                 author_email="vke.1743@gmail.com",
                 description="Standard Python Practices",
                 long_description=long_description,
                 long_description_content_type="/text/markdown",
                 url="",
                 packages=setuptools.find_packages(),
                 python_requires=">=3.6",
                 install_requires = [])