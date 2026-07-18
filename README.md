# 🔢 Calculator

A resizable, square-grid calculator built with CustomTkinter — a modern Python GUI toolkit that delivers a native-looking interface across all platforms.

## ✨ Features

- **Resizable Window** – Starts at 400x500 and adapts seamlessly when maximized
- **Square Grid Layout** – 4-column responsive grid with proportional button sizing
- **Basic Arithmetic** – Addition (+), subtraction (-), multiplication (*), division (/)
- **Advanced Operations** – Square root, absolute value, power, logarithm
- **Mathematical Constants** – Pi (π) and Euler's number (e) support
- **Dual Input Modes** – "=" for simple arithmetic, "Execute" for advanced expressions
- **Equality Checking** – Compare expressions using the "=" operator
- **Keyboard Support** – Press Enter to calculate, use "C" button to clear

## 📋 Requirements

- Python 3.13 or higher
- CustomTkinter

## 🚀 Installation

```bash
pip install customtkinter
```

## 🎯 Usage

Run the calculator:
```bash
python calculator.py
```

### Button Layout

```
[Display Entry Field]
[Result Label]
────────────────────
[7] [8] [9] [/]
[4] [5] [6] [*]
[1] [2] [3] [-]
[0] [.] [+] [=]
[sqrt] [abs] [pow] [log]
[C]     [Execute]
```

### Operations

| Operation | Method | Example | Result |
|-----------|--------|---------|--------|
| Addition | Type `+` or click | `5+3` | `8` |
| Subtraction | Type `-` or click | `10-4` | `6` |
| Multiplication | Type `*` or click | `3*7` | `21` |
| Division | Type `/` or click | `20/4` | `5.0` |
| Square Root | Type `sqrt(16)` + Execute | `sqrt(16)` | `4.0` |
| Absolute Value | Type `abs(-5)` + Execute | `abs(-5)` | `5` |
| Power | Type `pow(2,3)` + Execute | `pow(2,3)` | `8` |
| Logarithm | Type `log(100)` + Execute | `log(100)` | `4.605...` |
| Equality Check | Type expression + = | `5+3=8` | `True` |
| Constants | `pi` or `e` | `pi` | `3.14159...` |

### Keyboard Shortcuts

- **Enter** – Calculate the expression
- **C Button** – Clear the entry field and result

## 📝 Examples

**Basic Arithmetic:**
```
Input: 2+3*4
Press: =
Output: 14
```

**Advanced Functions:**
```
Input: sqrt(25)
Press: Execute
Output: 5.0
```

**Equality Check:**
```
Input: 2+3=5
Press: =
Output: True
```

**Mathematical Constants:**
```
Input: pi*2
Press: Execute
Output: 6.283...
```

## 🛠️ Technical Details

- Uses `eval()` with restricted namespaces for safe mathematical expression evaluation
- Responsive grid system with equal weight distribution across 8 rows and 4 columns
- Display includes both entry field and result label for clear feedback
- Error handling with user-friendly error messages

---

Built with CustomTkinter for a modern, native-looking interface across all platforms.
