# [missing-docstring]
# pylint: disable=too-few-public-methods

def public_documented():
    """It has a docstring."""


def _private_undocumented():
    # Doesn't need a docstring
    pass


def _private_documented():
    """It has a docstring."""


class ClassDocumented(object):
    """It has a docstring."""


class ClassUndocumented(object): # [missing-docstring]
    pass


def public_undocumented(): # [missing-docstring]
    pass