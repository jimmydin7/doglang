from .environment import Environment
from ..parser.ast_nodes import VarAssign, Say, Repeat, GoodBoy

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()

    def run(self):
        for node in self.ast:
            self.execute(node)

    def execute(self, node):
        if isinstance(node, Say):
            if node.value_type == 'variable':
                value = self.env.get_variable(node.value)
                print(value)
            elif node.value_type == 'string':
                print(node.value)
            else:
                raise RuntimeError(f"Unknown value_type: {node.value_type}")

        elif isinstance(node, VarAssign):
            value = node.value
            if node.datatype == 'int':
                value = int(value)
            self.env.set_variable(node.name, value)

        elif isinstance(node, Repeat):
            for _ in range(node.count):
                for stmt in node.body:
                    self.execute(stmt)
        elif isinstance(node, GoodBoy):
            left_value = self.env.get_variable(node.left)
            right_value = node.right
            # Only equality for now, and int/string types
            if str(left_value) == str(right_value):
                for stmt in node.body:
                    self.execute(stmt)
        else:
            raise RuntimeError(f"Unknown AST node type: {type(node)}")
