import os

if __name__ == "__main__":
    # Get the path to the current file
    path = os.path.dirname(os.path.abspath(__file__))
    # Get CONDA_PREFIX from environment
    conda_prefix = os.environ["CONDA_PREFIX"]
    # if not in conda environment, quit
    if conda_prefix == "":
        print("Not in a conda environment, quitting.")
        exit(1)
    # conda activate command
    conda_activate = os.path.join(conda_prefix, "Scripts", "activate.bat")
    # Write the launcher bat file
    with open(os.path.join(path, "click_to_run.bat"), "w") as f:
        f.write(f"call {conda_activate}\n")
        # change directory to the current file
        f.write(f"pushd {path}\n")
        f.write("python runner.py\n")

    # install requirements with pip
    os.system(f"pip install -r {os.path.join(path, 'requirements.txt')}")
