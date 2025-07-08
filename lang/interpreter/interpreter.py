# dogflang: The meme programming language for dog lovers
from .environment import Environment
from ..parser.ast_nodes import VarAssign, Say, Repeat, GoodBoy, Expression, FunctionDef, FunctionCall

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.env = Environment()
        self.functions = {}

    def run(self):
        for node in self.ast:
            self.execute(node)

    def execute(self, node):
        if isinstance(node, Say):
            if node.value_type == 'expression':
                value = self.eval_expression(node.value)
                print(value)
            elif node.value_type == 'string':
                print(node.value)
            else:
                raise RuntimeError(f"Unknown value_type: {node.value_type}")

        elif isinstance(node, VarAssign):
            value = node.value
            if node.datatype == 'int':
                value = self.eval_expression(value)
                value = int(value)
            elif node.datatype == 'string':
                value = self.eval_expression(value) if isinstance(value, Expression) else value
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
        elif isinstance(node, FunctionDef):
            self.functions[node.name] = node
        elif isinstance(node, FunctionCall):
            func = self.functions.get(node.name)
            if not func:
                raise RuntimeError(f"Function '{node.name}' is not defined")
            for stmt in func.body:
                self.execute(stmt)
        else:
            raise RuntimeError(f"Unknown AST node type: {type(node)}")

    def eval_expression(self, expr):
        if isinstance(expr, Expression):
            if expr.op is None:
                # Leaf: int literal or variable
                if isinstance(expr.left, str) and expr.left.isdigit():
                    return int(expr.left)
                elif isinstance(expr.left, str):
                    return self.env.get_variable(expr.left)
                else:
                    return expr.left
            left = self.eval_expression(expr.left)
            right = self.eval_expression(expr.right)
            if expr.op == '+':
                return left + right
            elif expr.op == '-':
                return left - right
            elif expr.op == '*':
                return left * right
            elif expr.op == '/':
                return left // right if isinstance(left, int) and isinstance(right, int) else left / right
            else:
                raise RuntimeError(f"Unknown operator: {expr.op}")
        else:
            return expr
