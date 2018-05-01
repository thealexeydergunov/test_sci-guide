class STATUS_URL_PROCESSING(object):
    """
    Choices for URLForProcessing model.

    Take CHOICES from this class for field into model or DICT for checking elements.
    """
    WAIT = 1
    PROCESS = 2
    SUCCESS = 3
    ERROR = 4

    CHOICES = (
        (WAIT, 'wait'),
        (PROCESS, 'process'),
        (SUCCESS, 'success'),
        (ERROR, 'error')
    )
    DICT = dict(CHOICES)
