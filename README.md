![Django CI](https://github.com/jdiazromeral/django-ddd/workflows/Django%20CI/badge.svg)

# Django the Domain Driven Design way 
This is a proof of concept to model django apps on a domain driven design way.
The idea is to move Django app related stuff under infrastructure folder, 
so ideally an app folder structure would be:

    app_folder/
        application/
        domain/
        infrastructure/
            migrations/
            admin.py
            models.py
            __init__.py
        __init__.py
         
## Installation
To install from source, download the source code, then run this:

```bash
python setup.py install
```

Or install with pip

```bash
pip install django-ddd
```

## Configuration
Select your desired app folder structure and add these settings to your project.

##### `CUSTOM_MODELS_MODULE`
Where Django should look for your app models.

>Default: `models`
>
>Example: `infrastructure.models`

##### `CUSTOM_MIGRATIONS_MODULE`
Where Django should look for your app migrations.

>Default `migrations`
>
>Example: `infrastructure.migrations`

##### `CUSTOM_ADMIN_MODULE`
Where Django should look for your app admin configuration.

> Default `admin`
>
> Example: `infrastructure.admin`

## Usage

### To use custom locations
Install django-ddd to your project requirements and add settings so Django 
can find your apps modules as seen on configuration.
You don't need to add django-ddd it to `INSTALLED_APPS`

Then, on your package `apps.py` import django-ddd custom app config:

    from django_ddd.apps_config import CleanAppConfig

    class AppNameConfig(CleanAppConfig):
        name = "app_name" # package folder name

On the app package `__init__.py` add where to find your app config. If it is in 
`app_name.infrastructure.apps.py`: 

    default_app_config = "app_name.infrastructure.apps.AppNameConfig"
    
Add your new application to `INSTALLED_APPS`

### To use start_clean_app
This command creates a new Django app with a Domain Driven Design structure. 

To use it, you need to add django-ddd to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ...
    "django_ddd",
    # ...
]
```
Then, just call:
```bash
python manage.py start_clean_app app_name
```
This will create a new context with previously seen structure:

    app_name/
        application/
        domain/
        infrastructure/
            migrations/
            admin.py
            models.py
            __init__.py
        __init__.py

Here all Django details are under `infrastructure` folder. Package level `__init__.py` 
has route to app config: 
```python
default_app_config = "app_name.infrastructure.apps.AppNaemAppConfig"
```

You can move this folder to your sources 
and add it to `INSTALLED_APPS` so Django can recognize it.

## Contributing / Running project locally
Build the docker image:
```bash
docker build . -t django-ddd-dev
```

Run tests:
```bash
 docker run -v $(pwd)/.:/usr/src/app django-ddd-dev bash -c "pipenv run python manage.py test"
```
