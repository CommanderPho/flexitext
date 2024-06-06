from typing import List
from .blocks import BlockParser, BlockScanner


def make_texts(string) -> List:
    scanner = BlockScanner(string)
    scanner.scan()
    parser = BlockParser(scanner.tokens)
    parser.parse()
    texts = parser.texts
    return texts



def make_plaintext_string(formatted_string: str) -> str:
    """ Strips the formatting from a provided formatted_string and returns the unformatted plaintext content.

    Usage:

    from flexitext.parser.make_texts import make_texts, make_plaintext_string
    
    plaintext_title: str = make_plaintext_string(formatted_string=title)
    plaintext_title
    """
    if formatted_string is None:
        return None
    ## strip formatting to convert back to plaintext string:
    title_texts_obj: List = make_texts(formatted_string) # Text
    return ''.join([v.string for v in title_texts_obj])
