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

Log into bicycle.ucdavis.edu with your UCD email address to access our local
JupyterHub server at http://bicycle.ucdavis.edu. You can then either create a
new terminal session or a "Python 3" Jupyter notebook.

Backing Up Your Work
====================

The JupyterHub server has an automated backup in place should any problems
occur, but it is recommended to regularly back up your own work. To do so,
open a terminal from the JupyterHub interface (go to ``New -> Terminal``). From
this terminal window, type ``backup-home``. This will find all of your files
and put them in a zip file called ``backup.zip``, which you should then be able
to see and download from JupyterHub interface. Any time you want to back up
your work, you can run this command again from the terminal and it will add any
new or changed files to the zip file on the server (you have to download it to
your own computer each time).

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

These are my recommended resources:

- The SciPy Lecture Notes: http://www.scipy-lectures.org/
- Effective Computation in Physics Anthony Scopatz & Kathryn Huff
  http://physics.codes/
- https://stackoverflow.com/ (Q & A site, search for topics of interest)

Each software package also has documentation:

- Jupyter: http://jupyter.org/documentation.html
- NumPy: https://docs.scipy.org/doc/numpy/
- SciPy: https://docs.scipy.org/doc/scipy/reference/
- SymPy: http://docs.sympy.org/latest/index.html
- matplotlib: https://matplotlib.org/contents.html
- PyDy: http://www.pydy.org/documentation.html

For beginning Python, I recommend ThinkPython_ by Allen Downey.

.. _ThinkPython: http://greenteapress.com/wp/think-python/

For Matlab users: `NumPy for Matlab Users
<https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html>`_.

There are thousands of other online resources that cover the full spectrum of
using Python for scientific and engineering computing.
