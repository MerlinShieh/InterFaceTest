import logging
class Log:
    def debug(self, message, filename='test.log', level=logging.DEBUG):
        logging.basicConfig(filename=filename,
                            format='%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s',
                            level=level)
        logging.debug(message)
    def info(self,message, filename='test.log',level=logging.INFO):
        logging.basicConfig(filename=filename,
                            format='%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s',
                            level=level)
        logging.info(message)
    def warning(self,message, filename='test.log',level=logging.WARNING):
        logging.basicConfig(filename=filename,
                            format='%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s',
                            level=level)
        logging.warning(message)
    def error(self,message, filename='test.log',level=logging.ERROR):
        logging.basicConfig(filename=filename,
                            format='%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s',
                            level=level)
        logging.error(message)
    def critical(self,message, filename='test.log',level=logging.CRITICAL):
        logging.basicConfig(filename=filename,
                            format='%(asctime)s - %(levelname)s - %(name)s -%(funcName)s - %(lineno)d - %(message)s',
                            level=level)
        logging.critical(message)