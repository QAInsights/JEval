import enum


@enum.unique
class Icon(enum.Enum):
    """
    Enum class for ASCII icons used in JEval
    """
    INFO = "\u2139"
    CHECK_MARK = "\u2713"
    RED_X = "\u2718"
    EMPTY = ""
