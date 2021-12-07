#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is mod:`__init__.py` from numberedFiles.

   
   
   Created by ldm on 2021-12-07 
"""

import logging
logger = logging.getLogger(__name__)

# avoid foreign logs of level
for key in logging.Logger.manager.loggerDict:
    print(key)
for _ in ['']:
    logging.getLogger(_).setLevel(logging.WARNING)
    
def main():
    pass

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)-4.4s %(module)-9.9s %(lineno)4d - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__file__)
    logger.info("Starting %s", os.path.realpath(__file__))

    main()

    logger.info("Finished")
