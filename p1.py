import time
import os
import dotenv

dotenv.load_dotenv('local_environment.env')

while True:

    START = os.getenv('START_P1')

    if START == 'False':
        print('stopping p1.py')

    if START:
        time.sleep(1)
        print('start p1.py')
        # Update env file
        os.environ['START_P1'] = 'False'