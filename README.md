# Dog Lang 🐶
**View demo & docs [here](https://jimmydin7.github.io/custom-programming-language/docs)**

A meme programming language for dog lovers, built from scratch in Python.  
Includes full lexer (tokenizer), parser, and interpreter. This version supports basic features like:

- Variable declarations with `sniff` (e.g. `sniff name = string("Doggo")`)
- Printing output using `barg()`
- Comment support (`#` for single-line comments)
- Repeat blocks for zoomies (`zoomies x { ... }`)
- Dog-themed if statement: `goodboy x = 5 { ... }`

---

## Example Code

```plaintext
# Print
barg("Hello, world!")

# Define a string
sniff myname = string("Doggo")

# Define an integer
sniff mynumber = int(42)

# Output the values
barg(myname)
barg(mynumber)

# Repeat block demo
zoomies 3 {
    barg("bark!")
}

# Dog-themed if statement
goodboy mynumber = 42 {
    barg("You are a good dog!")
}
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
- [x] Comments (`#`)
- [x] Tokenizer and AST
- [x] Repeat blocks (`zoomies x { ... }`)
- [x] Dog-themed if statement (`goodboy x = value { ... }`)
- [ ] Error handling (improved)
- [ ] Expressions / math
- [ ] More control flow

---

## Planned for Future Versions

- Arithmetic operations (`+`, `-`, etc.)
- More conditionals
- Loops (`while`, `for`)
- Functions
- Type checking
- Custom runtime errors

---

## Why?

This is a learning project to understand how programming languages work (tokenizing, parsing, interpreting) — now with more borks and zoomies!

---
**View demo & docs [here](https://jimmydin7.github.io/custom-programming-language/docs)**
