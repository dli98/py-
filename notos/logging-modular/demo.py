import logging

logger = logging.root  #

logger.level = logging.DEBUG

logging.lastResort.level = logging.DEBUG       #

file_handler = logging.FileHandler('ds.log', encoding='utf-8')
logger.addHandler(file_handler)


format_ = logging.Formatter('[%(name)s] %(asctime)s %(levelname)-8s: %(message)s]')
file_handler.setFormatter(format_)


def add(a, b):
    logger.warning(f"a ={a}, b={b}")
    r = a + b
    logger.debug(f"result = {r}")

    return r

add(1, 2)
