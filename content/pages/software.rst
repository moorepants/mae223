:title: Software
:sortorder: 2

I will be using two main pieces of software to demonstrate the principles in
the class. The first is SymPy_ which a computer algebra system that includes a
package for deriving analytical equations of motion. The second main software
is PyDy_ which is a simulation and visualization tool for models created with
SymPy. Both of these are open source software packages and are part of the
Scientific Python ecosystem of software packages.

.. _SymPy: http://sympy.org
.. _PyDy: http://pydy.org

Running The Software
====================

Log into http://jupyter.libretexts.org with your UCD email address to access
our local JupyterHub server. You can then either create a new terminal session
or a "Python 3" Jupyter notebook.

Backing Up Your Work
====================

The JupyterHub server has an automated backup in place should any problems
occur, but it is recommended to regularly back up your own work. Make sure to
download any important files from the service reguarly.

Installing the Software On Your Personal Computer
=================================================

We recommend that you install the Anaconda_ distribution of Python which
includes most all of the packages you will need.

.. _Anaconda: https://www.anaconda.com/download/

You can open up either Jupyter notebooks or use the Spyder IDE (which also can
open notebooks).

More instructions for getting PyDy and other more specialized packages
installed will be added here at a later date.

Learning Python For Engineering Computation
===========================================

Start with the SymPy tutorial to get familiar with symbolic manipulation in
Python:

https://docs.sympy.org/latest/tutorial/

The SymPy Physics Vector and Mechanics documentation provides explanations for
the advanced features for rigid body mechanics;

- https://docs.sympy.org/latest/modules/physics/vector
- https://docs.sympy.org/latest/modules/physics/mechanics

There is also a PyDy tutorial which starts with SymPy and ends with simulation
with PyDy:

https://github.com/pydy/pydy-tutorial-human-standing/

To learn the core Python language (not scientific oriented computing) there are
many many resources. My recommendations for beginners are:

- Allen Downey's book ThinkPython_.
- The tutorial on Python.org: https://docs.python.org/3/tutorial/

.. _ThinkPython: http://greenteapress.com/wp/think-python/

Python becomes most powerful for engineers by using the various packages in the
Scientific Python Ecosystem. Here are my recommend resources for learning these
topics:

- The SciPy Lecture Notes is a wholistic resource for all things numerical
  computing in Python: http://www.scipy-lectures.org/
- The book "Effective Computation in Physics" by Anthony Scopatz & Kathryn Huff is
  a guide that starts at ground zero for Python and leads you through the tools
  and methods to be a computational engineer. http://physics.codes/
- If you know some Matlab this guide is very helpful for looking up equivalent
  commands in NumPy: `NumPy for Matlab Users
  <https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html>`_.
- Getting good at asking Google programming questions will almost always lead
  you to https://stackoverflow.com/ which is a key resources for all kind of
  programming questions.

Each software package also has documentation:

- Jupyter: http://jupyter.org/documentation.html
- NumPy: https://docs.scipy.org/doc/numpy/
- SciPy: https://docs.scipy.org/doc/scipy/reference/
- SymPy: http://docs.sympy.org/latest/index.html
- matplotlib: https://matplotlib.org/contents.html
- PyDy: http://www.pydy.org/documentation.html
