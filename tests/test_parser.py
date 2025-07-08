import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lang.parser.parser import Parser
from lang.ast.var_assign import VarAssign

def test_parse_var_assign():
    tokens = [
        ('ID', 'sniff', 1),
        ('ID', 'x', 1),
        ('EQUALS', '=', 1),
        ('ID', 'int', 1),
        ('LPAREN', '(', 1),
        ('INT', '5', 1),
        ('RPAREN', ')', 1)
    ]
    parser = Parser(tokens)
    ast = parser.parse()

    expected = [
        VarAssign('x', 'int', '5')
    ]
    assert len(ast) == 1
    assert isinstance(ast[0], VarAssign)
    assert ast[0].name == 'x'
    assert ast[0].datatype == 'int'
    assert ast[0].value == '5'
    