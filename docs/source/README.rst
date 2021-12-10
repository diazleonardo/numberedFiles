README
======


Yield numbered files following the defined pattern.

:pattern: str required

  - Patterns follow the definitions of
    `PEP 498 -- Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>`_
    with the caveat that only `d` integes are allowed

  - A common pattern format is `run{:4d}_simple.png` that will, in the simplest case,
    start-target_
    generate a file like `run0000_simple.png` followed by a name `run0001_simple.png`, etc.

:path: str (None)

  - The `path` argument defines where the files will be created.
    If the path is `None` (the default) the files will be created in the system temporary files
    structure, under [Li|U]nix `/tmp/`.

  - If `path` begins with a `os.sep` (forward/backward slash normally) it is assumed an absolute path
    and the files will be created on that directory (that will be created if necessary).

  - If `path` begins with a valid character for the file system (and locale), it is assumed relative to the
    current working directory, and , as before, will be created if necessary.


  .. _start-target:

:start: int (0)

  - forces the number to start the sequence.  May be usefull if you don't want to overwrite
    existing files, or may want to the starting digit as a run number (setting start to 1000 an
    the first run, 2000 on the second, etc)

:reset: bool (False)

  - This the only case where files may be overwritten.  If set to `True` it will start with the number
    set by `start` (or zero if None) and happily overwrite your previous work.  Default is `False`

  - Note that if a previous run created files up to 100 and the current run only to a smaller number,,
    say 90, files 91 to 100 will NOT be deeted.

Example usage
-------------

>>> nf_class = NumberedFiles("nf{:04d}.tmp")
>>> nf = iter(nf_class)
>>> print( f"{next(nf)}")
