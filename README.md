# technical-writing-lab

This repository contains a small Python lab used for the assignment.

PythonLab/
- main.py : small palindrome checker with a command-line entrypoint.
- test.py : pytest tests covering the implementation.

How to run tests
1. Ensure Python 3 is installed.
2. (Optional) Install dependencies: python -m pip install -r PythonLab\requirements.txt
3. Run tests: python -m pytest -q PythonLab

How to run the checker

python PythonLab\main.py "A man, a plan, a canal: Panama"
# prints YES

If no argument is supplied, the program reads from stdin.
