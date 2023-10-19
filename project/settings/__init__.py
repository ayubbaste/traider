import os

# local or base (if local does not exists) settings is default
if os.environ.get('DJANGO_SETTINGS_MODULE', u'') == 'project.settings':
    try:
        from .local import *
    except ImportError:
        from .base import *