import os
import subprocess
import time

# Change to the directory where the script is located
os.chdir(os.path.dirname(__file__))

# Start the scripts
p1 = subprocess.Popen(['python', 'p1.py'])
p2 = subprocess.Popen(['python', 'p2.py'])

# Wait for the scripts to finish
time.sleep(3)

# Terminate p1
p1.terminate()

# Terminate p2
p2.terminate()


