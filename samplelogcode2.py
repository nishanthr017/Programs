import logging
import jsonlogger

formatter = jsonlogger.JsonFormatter()

json_handler = logging.FileHandler(filename='/var/log/my-log.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)
logger.info('Sign up', extra={'referral_code': '52d6ce'})





