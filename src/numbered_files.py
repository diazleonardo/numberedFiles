
import sys
import os
import re
from pathlib import Path
from tempfile import gettempdir
import logging

logger = logging.getLogger(__name__)


class NumberedFiles:
    """Yield numbered files following the defined pattern.

    * pattern:str required

      - Patterns follow the definitions of
        `PEP 498 -- Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>`_
        with the caveat that only `d` integes are allowed

      - A common pattern format is `run{:4d}_simple.png` that will, in the simplest case,
        start-target_
        generate a file like `run0000_simple.png` followed by a name `run0001_simple.png`, etc.

    * path: str

      - The `path` argument defines where the files will be created.
        If the path is `None` (the default) the files will be created in the system temporary files
        structure, under [Li|U]nix `/tmp/`.

      - If `path` begins with a `os.sep` (forward/backward slash normally) it is assumed an absolute path
        and the files will be created on that directory (that will be created if necessary).

      - If `path` begins with a valid character for the file system (and locale), it is assumed relative to the
        current working directory, and , as before, will be created if necessary.


      .. _start-target:

    * start: int

      - forces the number to start the sequence.  May be usefull if you don't want to overwrite
        existing files, or may want to the starting digit as a run number (setting start to 1000 an
        the first run, 2000 on the second, etc)

    * reset: bool

      - This the only case where files may be overwritten.  If set to `True` it will start with the number
        set by `start` (or zero if None) and happily overwrite your previous work.  Default is `False`

      - Note that if a previous run created files up to 100 and the current run only to a smaller number,,
        say 90, files 91 to 100 will NOT be deeted.


    """

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
