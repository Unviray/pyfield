def task_junk():
    """Remove junk file"""
    return {
        'actions': ['rm -rf $(find . | grep pycache)'], }


def task_test():
    """Run tests"""
    return {
        'actions': ['pytest'], }
