"""Test the numbered files class"""
import os
import logging

from src.numbered_files import NumberedFiles

logger = logging.getLogger(__name__)

# avoid foreign logs of level
for key in logging.Logger.manager.loggerDict:
    print(key)
for _ in ['']:
    logging.getLogger(_).setLevel(logging.WARNING)

# pylint: disable=logging-fstring-interpolation
def main():
    """Shut up PEP8"""
    numb_files = NumberedFiles("nf{:04d}.tmp")
    next_one = iter(numb_files)

    logger.debug(f"{next(next_one)}")
    logger.debug(f"{next(next_one)}")
    logger.debug(f"{next(next_one)}")


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)-4.4s %(module)-9.9s %(lineno)4d - %(message)s',
                        level=logging.DEBUG)
    logger = logging.getLogger(__file__)
    logger.info("Starting %s", os.path.realpath(__file__))

    main()

    logger.info("Finished")
