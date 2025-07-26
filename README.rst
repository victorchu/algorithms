Algorithms
==========

A collection of algorithm problems found online.

Most algorithms are implemented in Python3.
Few are implemented in Java as well.

Reference
*********
- https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/
- https://leetcode.com/problemset/top-interview-questions/

Setup
*********
Create a virtual environment:
::

    PROJ=Python-Algorithms
    pyenv versions
    pyenv virtualenv <version> $PROJ
    pyenv local $PROJ

Install other dependent modules, e.g. with poetry
::

    pip install -r requirements.txt

Add a IPython kernel for Jupyter.
::

    python -m ipykernel install --u --name $PROJ

