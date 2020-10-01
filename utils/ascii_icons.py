import enum


@enum.unique
class Icons(enum.Enum):
    """
    Enum class for ASCII icons used in JEval
    """
    NONE = ""
    INFO = "\u2139"
    CHECK_MARK = "\u2713"
    RED_X = "\u2718"
