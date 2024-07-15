from setuptools import setup, find_packages

setup(
    name="ImportReliantIrrigation",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "geopandas",
        "matplotlib",
        "rasterio",
        "shapely",
    ],
)
