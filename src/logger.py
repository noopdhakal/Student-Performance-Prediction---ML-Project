import logging
import os
from datetime import datetime

# log exception that is comming

LOG_FILE=f"{datetime.now().strftime('mylogfile_%H_%M_%d_%m_%Y.log')}.log"
logs_path=os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO, 

)

if __name__=="__main__":
    logging.info('logging has started')

