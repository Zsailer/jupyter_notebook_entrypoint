from .utils import notebook_not_found

try:
    from notebook.bundler.bundlerextensions import main
except ModuleNotFoundError:
    try:
        from nbclassic.bundler.bundlerextensions import main
    except ModuleNotFoundError:
        raise ModuleNotFoundError(notebook_not_found)
