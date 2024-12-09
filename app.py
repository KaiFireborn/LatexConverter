import json
from mapping import mapping as mapping_read


def prompt():
    expression = input("Enter a unicode expression:\n")
    return expression


def output(parsed):
    print("The LaTeX equivalent is:")
    print(parsed)
    print("\n")


class Parser:
    def __init__(self):
        self.mapping = mapping_read

    def parse_to_latex(self, expression):
        # TODO: Rewrite continuous strings under \mathit{#} so their letters are written closer to one another
        
        parsed_symbols = [self.mapping.get(symbol, symbol) for symbol in expression]
        parsed_expression = "$" + " ".join(parsed_symbols) + "$"
        
        return parsed_expression


if __name__ == "__main__":
    while True:
        expression = prompt()
        p = Parser()
        parsed = p.parse_to_latex(expression)
        output(parsed)
