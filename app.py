import json
from mapping import mapping as mapping_read
import pyperclip


CLIPBOARD_INPUT = True


def prompt_for_input():
    expression = input("Enter a unicode expression:\n")
    return expression

def get_input_from_clipboard():
    expression = pyperclip.paste()
    return expression
    

def output(parsed):
    print("The LaTeX equivalent is:")
    print(parsed)
    print("\n")

def output_to_clipboard(parsed):
    pyperclip.copy(parsed)
    print("The unicode expression from your clipboard has been converted to LaTeX and copied back to your clipboard.")


class Parser:
    def __init__(self):
        self.mapping = mapping_read

    def parse_to_latex(self, expression):
        # TODO: Rewrite continuous strings under \mathit{#} so their letters are written closer to one another
        # TODO: instead of the " ".join come up with better logic so 'false' doesn't become 'f a l s e'

        parsed_symbols = [self.mapping.get(symbol, symbol) for symbol in expression]
        parsed_expression = "$" + " ".join(parsed_symbols) + "$"

        return parsed_expression


if __name__ == "__main__":
    p = Parser()
    if CLIPBOARD_INPUT:
        expression = get_input_from_clipboard()
        parsed = p.parse_to_latex(expression)
        output_to_clipboard(parsed)
    else:
        while True:
            expression = prompt_for_input()
            parsed = p.parse_to_latex(expression)
            output(parsed)
