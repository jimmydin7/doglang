import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lang.interpreter.interpreter import Interpreter
from lang.parser.ast_nodes import VarAssign, Say

def test_say_statement(capsys):
    ast = [
        VarAssign('x', 'string', 'hello'),
        Say('x', 'variable')
    ]
    interpreter = Interpreter(ast)
    interpreter.run()

    captured = capsys.readouterr()
    assert captured.out.strip() == 'hello'
    
