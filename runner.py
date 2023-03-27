import os
from notebook.notebookapp import NotebookApp

if __name__ == "__main__":
    notebook_path = os.path.abspath("app.ipynb")
    app = NotebookApp()
    app.file_to_run = notebook_path
    app.initialize()
    app.start()
