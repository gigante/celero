from split_settings.tools import include

base_settings = [
    'base.py',  # standard django settings
    'apps.py',  # extra apps
]

# Include settings:
include(*base_settings)
