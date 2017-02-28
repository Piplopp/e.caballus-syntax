# This python code example is from the MagicStack/MagikPython repository
# Just added a few dummy things for testing purposes

import asyncio
from foo import bar as baz

class foo():
    number = 0
    def foo():
        self.number = 10.0 % 5
    # todo

class bar(foo):
    # todo

# This is a comment
def showcase():
    """Some code to showcase the syntax.

    Docstrings are recognized and have an additional scope.
    Color schemas can render them differently from other strings. but this line is really long

    HACK doctests are highlighted too.

        >>> print('''hello
        ... world''')
    """

    @decorator(param='spam')
    async def coroutine(db:aio_db.DatabaseConnection) -> List[str]:
        r"""A coroutine."""

        await logger.log('working\x12with %r', aio_db)

        async with db.transaction():
            result = await db.query(...)
            print(f'Result: {result!r}')

    mapping = None     # type: Dict[int, Any] # PEP 484

    # a regular expression
    get_regex = lambda: re.compile(     # type: ignore
        r"""\A
            word
            (?:                         # a comment
               (?P<fill>.)?
               (?P<align>[<>=^])        (?# another comment)
            )?
            another word\.\.\.
            (?:\.(?P<precision>0|(?!0)\d+))?
        \Z""",
        re.VERBOSE | re.DOTALL)

    # NOTE Numbers with leading zeros are invalid in Python 3,
    # use 0o...
    answer = func(0xdeadbeef + 0b00100001 + 0123 + 0o123 +
                  1_005_123 + # PEP 515
                  # complex numbers
                  .10e12 + 2j) @ mat

    return R'''No escapes '\' in this \one'''
