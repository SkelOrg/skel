# skel - Python Library
A Python library containing features from other great libraries, all in one!
___
## Index
* [Usage](#usage)
* [Used Libraries](#used-libraries)
___
## Main Utilities
* 4 operator (multiplication, division, subtraction and addition) calculations
* UUID4 and secure key generator
* PI, degrees and radian functions
* Ability to get the current time as well as date
* Random Number Generator (RNG)
* Ability to remove and create folders as well as list the contents of folders
* Sin, cos, tan and square rooting capabilities
* Advanced version of 'print()' with error and warning messages
___
## Used Libraries
* [datetime](https://docs.python.org/3/library/datetime.html)
* [random](https://docs.python.org/3/library/random.html)
* [secrets](https://docs.python.org/3/library/secrets.html)
* [uuid](https://docs.python.org/3/library/uuid.html)
* [math](https://docs.python.org/3/library/math.html)
* [os](https://docs.python.org/3/library/os.html)
___
## Usage
Download main.py and move it over to where you want it, then in your python file, write the following at the top:
```python
import sys
sys.dont_write_bytecode = True
from main import skel
```
(main.py MUST be in the same directory as the file that's using it, otherwise it will return an error.)
That will give you access to the class 'skel', which contains all the utilities.
___
