import warnings
notebook_not_found = """It looks the Jupyter Notebook is not installed.

Try (re)installing it using using `pip`:

    pip install notebook

or conda/mamba:

    conda install notebook
"""


try:
    from notebook.notebookapp import main
except ModuleNotFoundError:
    try:
        from nbclassic.notebookapp import main
    except ModuleNotFoundError:
        raise ModuleNotFoundError(notebook_not_found)
