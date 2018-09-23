def task_clean_junk():
    """Remove junk file"""
    return {
        'actions': ['rm -rf $(find . | grep pycache)'],
    }
