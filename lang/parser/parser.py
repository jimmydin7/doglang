#AST Generator
from .ast_nodes import VarAssign, Say, Repeat, GoodBoy
from helpers.utils import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.ast = []

    def peek(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None
    
    def advance(self):
        self.pos += 1

    def parse(self):
        while self.pos < len(self.tokens):
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'barg':
                    self.ast.append(self.parse_barg())
                elif token[1] == 'zoomies':
                    self.ast.append(self.parse_zoomies())
                elif token[1] == 'goodboy':
                    self.ast.append(self.parse_goodboy())
                elif token[1] == 'sniff':
                    self.ast.append(self.parse_var_assign())
                else:
                    self.error(f"Unexpected identifier {token[1]}")
            else:
                self.error(f"Unexpected token {token}")
        return self.ast
    
    def parse_var_assign(self):
        self.expect('ID')  # 'sniff'
        name = self.expect('ID')[1]
        self.expect('EQUALS')
        datatype = self.expect('ID')[1]
        self.expect('LPAREN') # (

        if datatype == 'string':
            value_token = self.expect('STRING')
        elif datatype == 'int':
            value_token = self.expect('INT')
        else:
            self.error("Unexpected datatype")

        value = value_token[1].strip('"') #remove quotes
        self.expect('RPAREN') #)
        return VarAssign(name, datatype, value)

    
    def parse_barg(self): #allowing barg("custom text")
        self.expect('ID')                    # 'barg'
        self.expect('LPAREN')                

        token = self.peek()
        if token[0] == 'ID':
            value = self.expect('ID')[1]
            value_type = 'variable'
        elif token[0] == 'STRING':
            raw_value = self.expect('STRING')[1]  
            value = strip_quotes(raw_value)     
            value_type = 'string'
        else:
            self.error(f"Expected variable name or string, got {token}")

        self.expect('RPAREN')                 # )

        return Say(value, value_type)

    def parse_zoomies(self):
        self.expect('ID')  # 'zoomies'
        count_token = self.expect('INT')
        count = int(count_token[1])
        self.expect('LBRACE')

        body = []
        while self.peek() and self.peek()[0] != 'RBRACE':
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'barg':
                    body.append(self.parse_barg())
                elif token[1] == 'zoomies':
                    body.append(self.parse_zoomies())
                elif token[1] == 'goodboy':
                    body.append(self.parse_goodboy())
                elif token[1] == 'sniff':
                    body.append(self.parse_var_assign())
                else:
                    self.error(f"Unexpected identifier {token[1]} in zoomies body")
            else:
                self.error(f"Unexpected token {token} in zoomies body")

        self.expect('RBRACE')
        return Repeat(count, body)

    def parse_goodboy(self):
        self.expect('ID')  # 'goodboy'
        left = self.expect('ID')[1]
        op = self.expect('EQUALS')[1]  # Only '=' supported for now
        right_token = self.peek()
        if right_token[0] == 'INT':
            right = self.expect('INT')[1]
        elif right_token[0] == 'STRING':
            right = strip_quotes(self.expect('STRING')[1])
        else:
            self.error(f"Expected int or string for goodboy condition, got {right_token}")
        self.expect('LBRACE')
        body = []
        while self.peek() and self.peek()[0] != 'RBRACE':
            token = self.peek()
            if token[0] == 'ID':
                if token[1] == 'barg':
                    body.append(self.parse_barg())
                elif token[1] == 'zoomies':
                    body.append(self.parse_zoomies())
                elif token[1] == 'goodboy':
                    body.append(self.parse_goodboy())
                elif token[1] == 'sniff':
                    body.append(self.parse_var_assign())
                else:
                    self.error(f"Unexpected identifier {token[1]} in goodboy body")
            else:
                self.error(f"Unexpected token {token} in goodboy body")
        self.expect('RBRACE')
        return GoodBoy(left, op, right, body)

    def expect(self, expected_type):
        token = self.peek()
        if token is None or token[0] != expected_type:
            self.error(f"Expected {expected_type}, got {token}")
        self.advance()
        return token

    def error(self, message):
        raise SyntaxError(message)