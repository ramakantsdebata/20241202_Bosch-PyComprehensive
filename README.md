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

### Unit testing commands
* py -m unittest -v _01_FixturesCmdline/tests/test_1_simpleCalcTest.py
* py -m unittest -v _01_FixturesCmdline.tests.test_1_simpleCalcTest
* py -m unittest -v _01_FixturesCmdline.tests.test_1_simpleCalcTest.TestSimpleCalculator_02
* py -m unittest -v _01_FixturesCmdline.tests.test_1_simpleCalcTest.TestSimpleCalculator_02.test_SimpleMul
* py -m _01_FixturesCmdline.tests.test_3_Suite
* pip install parameterized
* pytest .
* pytest . -v
* pytest . -v --html=report.html
* pytest . -v --html=report.html --self-contained-html
* pytest -v tests


## Links
* [PEP 0 – Index of Python Enhancement Proposals (PEPs)](https://peps.python.org/)
* [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* [PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)
* [Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html)
    * [Escape Sequence](https://docs.python.org/3/reference/lexical_analysis.html)
    * [Format Specifiers](https://docs.python.org/3/reference/lexical_analysis.html)
* [Exception Hieirarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
* [pickle — Python object serialization](https://docs.python.org/3/library/pickle.html)
* ['re' - Regular Expressions](https://docs.python.org/3/library/re.html)
* [Pytest site](https://docs.pytest.org/en/stable/index.html)
    * [How to use unittest-based tests with pytest](https://docs.pytest.org/en/stable/how-to/unittest.html)
* [Pydantic](https://docs.pydantic.dev/latest/)
* [Simple OAuth2 using bearers and tokens](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)
* [OAuth2 Scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)

## Operational
* [Training Feedback](https://forms.gle/P1t12HHh1LSehpft9)
* [Mid-session Test](https://forms.gle/VViqBhZsN2bxtSqA6)
* [Post-session Test](https://forms.gle/jVRmBH6PpjiZ3CkC7)


## Contact
* ramakant.s.debata@gmail.com
