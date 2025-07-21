# This can be run inside your virtualenv
import subprocess

# Install or upgrade packages
subprocess.run(["pip", "install", "--upgrade", "pip"])
subprocess.run(["pip", "install", "numpy", "pandas", "matplotlib"])