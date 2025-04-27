import logging

import src.package_data_to_format.decor


@src.package_data_to_format.decor.singletone
class LoggerAll:
    logging.basicConfig(filename="newfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    logger = logging.getLogger()
