from notebook.services.config import ConfigManager

ConfigManager().update('notebook', 
                      {'load_extensions': {'toc': True, 
                                           'toggle-headers': True, 
                                           'search-replace': True, 
                                           'python-markdown': True }})