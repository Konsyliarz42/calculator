import logging

logging.basicConfig(
        format = '%(asctime)s | %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        level = logging.DEBUG,
        handlers=[
            logging.FileHandler("debug.log", 'w', encoding='utf-8'),
        ]
    )

log = logging.getLogger('log')