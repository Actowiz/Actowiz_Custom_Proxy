from setuptools import find_packages, setup


setup(
    name="actowiz_custom_proxy",
    version="0.0.22",
    description="",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description="actowiz custom proxy",
    long_description_content_type="text/markdown",
    url="",
    author="VISHAL AGHERA",
    author_email="",
    license="ACTOWIZ",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["elasticsearch >= 8.11.1", "scrapy >= 2.11.0"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
