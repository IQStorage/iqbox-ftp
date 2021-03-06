from PySide.QtCore import QSettings


DEBUG = False
# Flag for anything related to development, ex: deleting log at start, QT debug workarounds:
WEARECODING = True

# To be used with the `QSettings` objects
SettingsKeys = {
    'host': 'Host',
    'username': 'Username',
    'passwd': 'Password',
    'localdir': 'LocalDir',
    'ssl': 'SSL',
    'synced': 'Synced'}


def get_settings():
    """
    Creates a `QSettings` object set up for the application.
    Returns a `QSettings` object.
    """
    
    return QSettings('IQStorage', 'IQBox')

