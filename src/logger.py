import logging
import os
from datetime import datetime
import logger

#logging.error(self.emessage)

LOGFILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOGFILE)

os.makedirs(logs_path, exist_ok = True)

LOGFILEPATH = os.path.join(logs_path, LOGFILE)

logging.basicConfig(
    filename=LOGFILEPATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)