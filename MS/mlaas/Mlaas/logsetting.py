import logging

class LoggingClass:
    def check_logconfig(self,login_config = False):
        if login_config:
            LOGGING = {
                'version':1,
                'disable_existing_loggers': True,
                'loggers':{
                    'django':{
                        'handlers':['file1','file2','file3'],
                        'level' : 'DEBUG',
                    }
                },
                'handlers':{
                    'file1':{
                        'level' : 'ERROR',
                        'class':'logging.FileHandler',
                        'filename':'logs/error.log',
                        'formatter':'simple',
                    },
                    'file2':{
                        'level' : 'INFO',
                        'class':'logging.FileHandler',
                        'filename':'logs/info.log',
                        'formatter':'simple',
                    },
                    'file3':{
                        'level' : 'DEBUG',
                        'class':'logging.FileHandler',
                        'filename':'logs/debug.log',
                        'formatter':'simple',
                    }
                },
                'formatters':{
                    'simple':{
                        'format' : '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                        'style' : '{',
                    }
                }
            }
        else:
            LOGGING = None
            
        return LOGGING