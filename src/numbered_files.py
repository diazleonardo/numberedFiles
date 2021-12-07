#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is mod:`NumberedFiles` from numberedFiles.

   
   
   Created by ldm on 2021-12-07 
"""
import sys
import os
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# avoid foreign logs of level
# for key in logging.Logger.manager.loggerDict:
#     print(key)
# for _ in ['']:
#     logging.getLogger(_).setLevel(logging.WARNING)


class NumberedFiles:
    """Yield numbered files following the defined pattern.

    * pattern

      - description of the pattern

      - numbering format

    * path

      - The `path` argument defines where the files will be created.
        If the path is `None` (the default) the files will be creted in the system temporary files
        structure, under [Li|U]nix `/tmp/`.

      - If `path` begins with a `os.sep` (forward/backward slash normally) it is assumed an absolute path
        and the files will be created on that directory (that will be created if necessary).

      - If `path` begins with a valid character for the file system (and locale), it is assumed relative to the
        current working directory, and , as before, will be created if necessary.

    """

    def __init__(self, pattern: str, path: str= None, reset: bool = False):
        """Constructor for NumberedFiles"""
        # TODO: Explain parameters


def main():
    nf = NumberedFiles("nf")
    nf.next()


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)-4.4s %(module)-9.9s %(lineno)4d - %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(__file__)
    logger.info("Starting %s", os.path.realpath(__file__))

    main()

    logger.info("Finished")
