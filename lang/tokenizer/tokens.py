# dogflang: The meme programming language for dog lovers
TOKEN_TYPES = [
    ('COMMENT',   r'#.*'),
    ('ID',        r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('EQUALS',    r'='),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('STAR',      r'\*'),
    ('SLASH',     r'/'),
    ('INT',       r'\d+'),
    ('STRING',    r'"[^"]*"'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
    ('LBRACE',    r'\{'),
    ('RBRACE',    r'\}'),
    ('NEWLINE',   r'\n'),
    ('SKIP',      r'[ \t]+'),
    ('MISMATCH',  r'.'),
]
# Dog Lang keywords: 'barg', 'sniff', 'zoomies', 'goodboy' are handled in the parser as special IDs.
