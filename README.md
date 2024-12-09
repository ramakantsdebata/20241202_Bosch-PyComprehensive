# 20241202_Bosch-PyComprehensive

## Notes
### Virtual environments

| Action                               | Command                             |
|--------------------------------------|-------------------------------------|
| **Create virtual environment**       | `python -m venv .env-trial`         |
| **Activate virtual environment**     | `source .env-trial/Scripts/activate`|
| **Deactivate virtual environment**   | `deactivate`                        |
| **List installed packages**          | `pip list`                          |
| **Install a package**                | `pip install multipledispatch`      |
| **Install packages from requirements file** | `pip install -r req.txt`   |
| **Export installed packages to requirements file** | `pip freeze > req_2.txt` |

### Operator Overloading
* Binary Operators:
    *     + (addition) - __add__
    *     - (subtraction) - __sub__
    *     * (multiplication) - __mul__
    *     / (division) - __truediv__
    *     // (floor division) - __floordiv__
    *     % (modulo) - __mod__
    *     ** (exponentiation) - __pow__
    *     << (left shift) - __lshift__
    *     >> (right shift) - __rshift__
    *     & (bitwise AND) - __and__
    *     | (bitwise OR) - __or__
    *     ^ (bitwise XOR) - __xor__
* Comparison Operators:
    *     < (less than) - __lt__
    *     > (greater than) - __gt__
    *     <= (less than or equal to) - __le__
    *     >= (greater than or equal to) - __ge__
    *     == (equal to) - __eq__
    *     != (not equal to) - __ne__
* In-Place Operators:
    *     += (in-place addition) - __iadd__
    *     -= (in-place subtraction) - __isub__
    *     *= (in-place multiplication) - __imul__
    *     /= (in-place division) - __itruediv__
    *     //= (in-place floor division) - __ifloordiv__
    *     %= (in-place modulo) - __imod__
    *     **= (in-place exponentiation) - __ipow__
    *     <<= (in-place left shift) - __ilshift__
    *     >>= (in-place right shift) - __irshift__
    *     &= (in-place bitwise AND) - __iand__
    *     |= (in-place bitwise OR) - __ior__
    *     ^= (in-place bitwise XOR) - __ixor__
* Unary Operators:
    *     - (negation) - __neg__
    *     + (positive) - __pos__
    *     ~ (bitwise NOT) - __invert__
    *     abs() (absolute value) - __abs__

## Links
* [PEP 0 – Index of Python Enhancement Proposals (PEPs)](https://peps.python.org/)
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)
* [Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html)
    * [Escape Sequence](https://docs.python.org/3/reference/lexical_analysis.html)
    * [Format Specifiers](https://docs.python.org/3/reference/lexical_analysis.html)
* [Exception Hieirarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

## Operational
* [Training Feedback](https://forms.gle/P1t12HHh1LSehpft9)
