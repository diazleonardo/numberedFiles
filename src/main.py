import os
import logging

from numbered_files import NumberedFiles


def main():
    nf_class = NumberedFiles("nf{:04d}.tmp")
    nf = iter(nf_class)

    logger.debug(f"{next(nf)}")
    logger.debug(f"{next(nf)}")
    logger.debug(f"{next(nf)}")


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)-4.4s %(module)-9.9s %(lineno)4d - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__file__)
    logger.info("Starting %s", os.path.realpath(__file__))

    main()

    logger.info("Finished")
