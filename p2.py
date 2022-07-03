import time
import os
import dotenv

dotenv.load_dotenv('local_environment.env')

while True:

    START = os.getenv('START_P2')

    if START == 'False':
        print('stopping p2.py')

    if START:
        time.sleep(1)
        print('start p2.py')
        # Update env file
        os.environ['START_P2'] = 'False'