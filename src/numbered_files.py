import sys
import os
import re
from pathlib import Path
from tempfile import gettempdir
import logging

logger = logging.getLogger(__name__)


class NumberedFiles:
    """Yield numbered files following the defined pattern."""

    def __init__(self, pattern: str, path: str = None, start: int = 0, reset: bool = False):
        # get pattern splits
        r = re.match(r'([^{]*){:([^}]+)}(.*)$', pattern)
        foo = r.regs[1:]
        self._pre = pattern[foo[0][0]:foo[0][1]]
        digits = pattern[foo[1][0]:foo[1][1]]
        d = re.sub('[^0-9]', '', digits)
        self.max = 10 ** int(d)
        self._post = pattern[foo[2][0]:foo[2][1]]
        self.pattern = pattern
        self._path = gettempdir() if path is None else path
        self.start = self._find_largest_numbered_file(Path(self._path)) if not reset else start

    def _find_largest_numbered_file(self, root: Path) -> int:
        """ Find largest numbber on a file.

        :param Path root: root dir
        :return: largest number found (0 if none)
        :rtype: int
        """
        mmax = -1  # if nothing found, this will force a zero
        # find files matching pattern
        for filepath in root.rglob(self._pre + '*' + self._post):
            i = len(self._pre)
            k = len(filepath.name) - len(self._post)
            num = filepath.name[i:k]
            mmax = max(int(num), mmax)
        return mmax + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.max:
            foo = Path(self._path) / str(self.pattern.format(self.start))
        else:
            raise StopIteration(f"File pattern does not allow numbers larger than {self.start -1:,d}")
        self.start += 1
        return foo
