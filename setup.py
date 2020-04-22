from setuptools import setup

with open("README.md", "r") as readme:
    README = readme.read()

version = "0.1.1"

setup(
    name="Django-ddd",
    version=version,
    url="https://github.com/jdiazromeral/django-ddd",
    license="MIT License",
    author="Javier Díaz-Romeral Torralbo",
    author_email="javierdiazromeral@gmail.com",
    description="An app for a cleaner Django",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["django_ddd"],
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Django"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance" "Topic :: Utilities",
    ],
    python_requires=">=3.8",
)
