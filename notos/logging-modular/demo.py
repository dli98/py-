import logging

# logger = logging.root  #

logger = logging.getLogger(__name__)

logger.level = logging.DEBUG

logging.lastResort.level = logging.INFO       #

# file_handler = logging.FileHandler('ds.log', encoding='utf-8')
# logger.addHandler(file_handler)
#
#
# format_ = logging.Formatter('[%(name)s] %(asctime)s %(levelname)-8s: %(message)s]')
# file_handler.setFormatter(format_)


def add(a, b):
    # print(a)

    logger.warning("This is a warning")
    logger.warning(f"a ={a}, b={b}")
    r = a + b
    logger.debug(f"aaaaaaaaaaaaaaaaresult = {r}")
    logger.info(f"result = {r}")
    return r

add(1, 2)
