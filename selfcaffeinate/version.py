from . import (
    __version__,
    __title__,
    __summary__
)


class SelfCaffeinateAbout:

    def __str__(self):
        return "%s %s version %s" % (__title__, __summary__, __version__)
