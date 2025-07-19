import os
import datetime

# OS operations
print("Current directory:", os.getcwd())
print("Files in current dir:", os.listdir())

# Date/time
now = datetime.datetime.now()
print("Current datetime:", now)
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))