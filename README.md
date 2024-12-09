## What is this?

By default, the app converts a unicode expression (like `∀x. (∃y. P (x, y) ∧ ∀y. ¬Q(x, y) → ¬(∃y. P (x, y) ∧ true))` you copied and transforms it into LaTeX syntax when launched. Can also be reconfigured in `settings.json` to continuously take terminal input.

## How does/doesn't this work?

Currently it's just a giant dict converting each character to the LaTeX equivalent... To add support for new characters, edit `mapping.py`.

## Can I contribute?

Yes please! There are probably some unresolved #TODOs lying around, too.