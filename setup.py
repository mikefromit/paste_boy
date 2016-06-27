from setuptools import find_packages, setup

setup(
    name="paste-boy",
    version="0.0.1",
    author="mikefromit",
    author_email="mike.arbelaez@gmail.com",
    py_modules=['wsgi'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django==1.9.7",
        "django-filter==0.13.0",
        "djangorestframework==3.3.3",
        "gunicorn==19.6.0",
        "Markdown==2.6.6",
        "Pygments==2.1.3",
    ]
)
