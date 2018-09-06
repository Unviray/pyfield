def task_clean_junk():
    """Remove junk file"""
    return {
        'actions': ['rm -rdf $(find . | grep pycache)'],
    }
