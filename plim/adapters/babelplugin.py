"""gettext message extraction via Babel: http://babel.edgewall.org/"""
from mako.ext.babelplugin import extract as _extract_mako

from .. import lexer
from ..util import StringIO



def extract(fileobj, keywords, comment_tags, options):
    """Extract messages from Plim templates.

    :param fileobj: the file-like object the messages should be extracted from
    :param keywords: a list of keywords (i.e. function names) that should be
                     recognized as translation functions
    :param comment_tags: a list of translator tags to search for and include
                         in the results
    :param options: a dictionary of additional options (optional)
    :return: an iterator over ``(lineno, funcname, message, comments)`` tuples
    :rtype: ``iterator``
    """
    fileobj = StringIO(lexer.compile_plim_source(fileobj))
    for extracted in _extract_mako(fileobj, keywords, comment_tags, options):
        yield extracted
