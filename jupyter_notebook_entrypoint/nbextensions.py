from .utils import notebook_not_found

try:
    from notebook.nbextensions import main
except ModuleNotFoundError:
    try:
        from nbclassic.nbextensions import main
    except ModuleNotFoundError:
        raise ModuleNotFoundError(notebook_not_found)
