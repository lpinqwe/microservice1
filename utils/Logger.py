import logging

import decor


@decor.singletone
class LoggerAll:
    logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    logger = logging.getLogger()
