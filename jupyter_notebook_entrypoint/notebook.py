from jupyter_notebook_entrypoint.utils import notebook_not_found

# Attempt to load form notebook v7 first.
try:
    from notebook.app import main
except ModuleNotFoundError:
    # If using notebook v6 is installed, use that.
    try:
        from notebook.notebookapp import main
    except ModuleNotFoundError:
        # If notebook is not installed, fallback to nbclassic.
        try:
            from nbclassic.notebookapp import main
        except ModuleNotFoundError:
            raise ModuleNotFoundError(notebook_not_found)
