# Doglang Web Playground

A Flask-based web playground is included for Doglang! You can write Doglang code in your browser, click 'Run', and see the output instantly.

## How to use

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the web playground:
   ```
   python web_playground.py
   ```
3. Open your browser and go to http://127.0.0.1:5000/

---

# Dog Lang 🐶
<!-- dogflang: The meme programming language for dog lovers -->
**View demo & docs [here](https://jimmydin7.github.io/custom-programming-language/docs)**

A meme programming language for dog lovers, built from scratch in Python.  
This is the official **dogflang** project. Includes full lexer (tokenizer), parser, and interpreter. This version supports basic features like:

- Variable declarations with `sniff` (e.g. `sniff name = string("Doggo")`)
- Printing output using `barg()`
- Arithmetic expressions with `+`, `-`, `*`, `/`
- User-defined functions with `doggo` and `bark`
- Repeat blocks for zoomies (`zoomies x { ... }`)
- Dog-themed if statement: `goodboy x = 5 { ... }`

---

## Example Code

```plaintext
barg("Hello, world!")

sniff x = int(2 + 3 * 4)
barg(x)

sniff myname = string("Doggo")
barg(myname)

zoomies 3 {
    barg("bark!")
}

goodboy x = 14 {
    barg("You are a good dog!")
}

doggo greet() {
    barg("Woof from a function!")
}
bark greet()
```

---

## How to Run

1. have **Python 3.x** installed
2. clone the repository
3. add your code to a `.txt` file
4. run the python file and add your source code's path as an argument
   ```bash
   python run.py sourcecode.txt
   ```

---

## Features

- [x] Integer & string variables with `sniff`
- [x] Print with `barg()`
- [x] Arithmetic expressions (`+`, `-`, `*`, `/`)
- [x] User-defined functions (`doggo`, `bark`)
- [x] Tokenizer and AST
- [x] Repeat blocks (`zoomies x { ... }`)
- [x] Dog-themed if statement (`goodboy x = value { ... }`)
- [ ] Error handling (improved)
- [ ] More control flow

---

## Planned for Future Versions

- More conditionals
- Loops (`while`, `for`)
- Functions with arguments
- Type checking
- Custom runtime errors

---

## Why?

This is a learning project to understand how programming languages work (tokenizing, parsing, interpreting) — now with more borks and zoomies!

---
**View demo & docs [here](https://jimmydin7.github.io/custom-programming-language/docs)**
