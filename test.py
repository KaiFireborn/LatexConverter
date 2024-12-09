import unittest
from app import Parser

class testParseToLatex(unittest.TestCase):
    def test_simple_logic_expression(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("A ∧ B").replace(" ", ""), "$A \\land B$".replace(" ", ""))
    def test_logic_expression_2(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("(¬(p ∨ (¬r ∨ q)) ∨ p)").replace(" ", ""), "$(\\neg (p \\lor (\\neg r \\lor q)) \\lor p)$".replace(" ", ""))
    #(p → q) → (q → p)
    def test_logic_expression_3(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("(p → q) → (q → p)").replace(" ", ""), "$(p \\rightarrow q) \\rightarrow (q \\rightarrow p)$".replace(" ", ""))
    #∀x. (∃y. (Q(x, y) ∧ ∃x. ¬Q(y, x)))
    def test_logic_expression_with_quantors(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("∀x. (∃y. (Q(x, y) ∧ ∃x. ¬Q(y, x)))").replace(" ", ""), "$\\forall x. (\\exists y. (Q(x, y) \\land \\exists x. \\neg Q(y, x)))$".replace(" ", ""))
    #¬∀x. P (x) ∨ ∃y. Q(x, y)
    def test_logic_expression_with_negated_quantors(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("¬∀x. P (x) ∨ ∃y. Q(x, y)").replace(" ", ""), "$\\neg \\forall x. P (x) \\lor \\exists y. Q(x, y)$".replace(" ", ""))
    #∀x. (∃y. P (x, y) ∧ ∀y. ¬Q(x, y) → ¬(∃y. P (x, y) ∧ true))
    def test_logic_expression_with_quantors_long(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("∀x. (∃y. P (x, y) ∧ ∀y. ¬Q(x, y) → ¬(∃y. P (x, y) ∧ true))").replace(" ", ""), "$\\forall x. (\\exists y. P (x, y) \\land \\forall y. \\neg Q(x, y) \\rightarrow \\neg (\\exists y. P (x, y) \\land true))$".replace(" ", ""))
    #∀x, y. (P (x, y) → P (y, x)) → ∀z. P (z, z)
    def test_logic_expression_with_quantors_complicated(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("∀x, y. (P (x, y) → P (y, x)) → ∀z. P (z, z)").replace(" ", ""), "$\\forall x, y. (P (x, y) \\rightarrow P (y, x)) \\rightarrow \\forall z. P (z, z)$".replace(" ", ""))
    #∀x. (P (x) → P (f (x)))
    def test_logic_expression_with_first_order_function(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("∀x. (P (x) → P (f (x))").replace(" ", ""), "$\\forall x. (P (x) \\rightarrow P (f (x))$".replace(" ", ""))
    #⟨Expr1⟩ ::= ⟨Expr1⟩ ‘ + ’ ⟨Expr2⟩ | ⟨Expr2⟩
    def test_grammar_expression_with_angles(self):
        p = Parser()
        self.assertEqual(p.parse_to_latex("⟨Expr1⟩ ::= ⟨Expr1⟩ ‘ + ’ ⟨Expr2⟩ | ⟨Expr2⟩").replace(" ", ""), "$\\langle Expr1 \\rangle ::= \\langle Expr1 \\rangle ‘ + ’ \\langle Expr2 \\rangle | \\langle Expr2 \\rangle$".replace(" ", ""))
        
if __name__ == '__main__':
    unittest.main()