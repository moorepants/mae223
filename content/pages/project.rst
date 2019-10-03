:title: Project
:sortorder: 3

A portion of your grade will be assigned based on a quarter long project
involving analysis of the dynamics of a multibody system using Kane's method
and SymPy/PyDy. You must select a reasonably complex system (including possibly
significant damping and other interesting dynamic components). This is an ideal
opportunity to get started on the dynamic analysis of a thesis topic (with free
consulting!). Next you must suggest a set of well-posed questions about the
system which the simulation can help you to answer, derive the differential
equations of motion, study the system by simulating the system dynamics, and
present you results in a well formatted written report in the form of a
`Jupyter notebook`_ (or set of) including whatever charts, tables, figures, and
visualizations you may need to clearly communicate your results.

.. _Jupyter notebook: http://jupyter.org/

Many students believe that once the equations are written and the simulation is
completed, the job is finished. Actually, the task has only begun. Dynamic
simulations are merely a tool to learn about the possible dynamic behaviors
that a system can exhibit and how these dynamics depend on other parameters.
They must be used cleverly and resourcefully to elucidate the behavior of the
system. This involves asking the right questions about the system and
understanding which parametric dependencies are of interest. Usually this will
come from some engineering job requirements and specifications or from some
scientific question which one would like answered (e.g. "Design an antenna
deployment system for a communication satellite which works in the near earth
orbit, deploys in less that 10 sec, ..., etc." or "What are the important
parameters which limit the maximum range of achievable in a throw of the discus
and how should it be launched optimally?"). In this project you will be
responsible for generating this project requirement before writing the
simulation to help you answer the question you have asked. A good, precise
statement of an interesting question is every bit as important as good answer.
Indeed, poorly defined or worded questions are often impossible to answer in a
satisfying and fulfilling way.

Your grade will be based on the following aspects:

1. Sophistication, interest, and difficulty of system and the questions(s) you
   will ask about it
2. Correctness of equations/analysis and interpretation
3. The cleverness and resourcefulness with which you use the simulation to
   learn about the dynamics of the system and answer the questions posed
4. Your written discussion of the system and the presentation of the results of
   your study/interpretation.
5. Clarity, coherence and general organization of your report

Deadlines
=========

Friday October 18th
-------------------

Report to me in writing the system of your choice, including a motivation for
the problem, background on how to system works heuristically, a literature
search to identify previous work on this problem, and a relatively complete
discussion of the way you hope to use the dynamic simulation to learn what you
have chosen to learn. This should take several pages to do completely. I urge
you to begin the selection of your system immediately and to discuss it with me
office hours so that I can help you in this phase. This proposal should be no
longer that three pages.

Thursday, December 12th
-----------------------

The final report is due. No submissions will be accepted after this date due to
the time needed to grade them.

Thursday, December 12th
-----------------------

You will present a 5 minute lightning talk to the class explaining your
project, methods, and the results.

Example Notebooks
=================

To get an idea of what you can do with Jupyter notebooks, here are some
examples:

- https://nbviewer.jupyter.org/
- A tutorial I gave at SciPy 2017: http://www.sympy.org/scipy-2017-codegen-tutorial/
- The PyDy Human Standing Tutorial: https://github.com/pydy/pydy-tutorial-human-standing
- CFDPython: https://github.com/barbagroup/CFDPython
- Notebook gallery: http://nb.bianp.net/sort/views/

Project Ideas
=============

Mechanisms
----------

There are thousands of intersting mechanisms. Here are several collections of
mechanisms to get some ideas from:

- `Nguyen Duc Thang' Animated Mechanisms`_ - A huge searchable youtube video
  list of thousands of mechanisms and movements.
- `Mechanism collection - TU Delft`_
- `Kinematic Models for Digital Design Library`_
- `507 Mechanical Movements`_

.. _Animated Mechanisms: https://www.youtube.com/user/thang010146/videos
.. _Mechanism collection - TU Delft: http://www.mechanisms.antonkb.nl/
.. _Kinematic Models for Digital Design Library: http://kmoddl.library.cornell.edu/model.php
.. _507 Mechanical Movements: http://507movements.com/

Kinetic Sculptures
------------------

Google searches for "kinetic sculptures" or "`kinetic art`_" will provide you
with many interesting multibody systems. One of my favorites are the
strandbeesten from Theo Jansen:

.. _kinetic art: https://en.wikipedia.org/wiki/Kinetic_art

Theo Jansen's Strandbeesten
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Theo Jansen developed a multi-bar linkage that translates rotational motion
into linear motion that works well for making walking machines. He deploys it
in his Strandbeesten "Beach Animals":

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/LewVEF2B_pM" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

Modeling and analyzing the leg linkages or something similar would work well
for a project.

- https://en.wikipedia.org/wiki/Theo_Jansen
- https://www.strandbeest.com

Vehicles
--------

Single Track and Titling Vehicles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Single track and titling vehicles are particularly interesting because they
must be both balanced and directed. There are many interesting single track
vehicles that would offer opportunties for mutlibody modeling. For example,
bicycies, scooters, motorcycles, monocycles, single wheel trailers, titling
vehicles.  snake boards, unicycles

Some good papers:

- Sharp, R. S. The Stability and Control of Motorcycles. Journal of Mechanical
  Engineering Science 13, 316–329 (1971).
- Meijaard, J. P., Papadopoulos, J. M., Ruina, A. & Schwab, A. L. Linearized
  dynamics equations for the balance and steer of a bicycle: A benchmark and
  review. Proceedings of the Royal Society A: Mathematical, Physical and
  Engineering Sciences 463, 1955–1982 (2007).
- Kooijman, J. D. G., Meijaard, J. P., Papadopoulos, J. M., Ruina, A. & Schwab,
  A. L. A Bicycle Can Be Self-Stable Without Gyroscopic or Caster Effects.
  Science 332, 339–342 (2011).
- Karnopp, D. Tilt Control for Gyro-Stabilized Two-Wheeled Vehicles. Vehicle
  System Dynamics 37, 145–156 (2002).

The "`Bicycle and Motorcycle Dynamics <http:bmdconf.org>`_" conference has
proceedings about these vehicles.

Biomechanics
------------

Animal Motion
~~~~~~~~~~~~~

Animals have evolved a very large variety of ways to locomote from hopping,
sliding, flywing, to multileg walking

Walking
~~~~~~~

Sports Biomechanics
-------------------

The Skateboard Ollie
~~~~~~~~~~~~~~~~~~~~

Skateboarders are able to jump with the skateboard seemingly attached to their
feet, yet it isn't. The technique is called the "ollie" and revolutionzed the
sport when invented. The technique is now the foundation for hundreds of
similar tricks. The skateboarder uses a combination of popping the board at and
angle and then lifting the board usign the friction between their foot and the
surface of the board to bring the board into the air. The goal of this project
would be to develop a model of a skateboard that can be "ollied" and attempt to
do so.

Robots
------

Robotic Arms
~~~~~~~~~~~~

Boston Dynamic's Spot
~~~~~~~~~~~~~~~~~~~~~

Toys
----

The walking rabbit, the oloid, the rattleback,

http://www.dct.tue.nl/New/Leine/toys.html

Make Luxo the Pixar Lamp Jump!




Where to Find Other Ideas
-------------------------

- The mechanical_gifs subreddit usually has all kinds of fun machines that may
  inspire. http://reddit.com/r/mechanical_gifs
- The Journal of Multibody Dynamics http://journals.sagepub.com/home/pik
- Multibody System Dynamics Journal http://www.springer.com/engineering/mechanics/journal/11044
- Journal of Applied Mechanics http://appliedmechanics.asmedigitalcollection.asme.org/issue.aspx?journalid=112&issueid=26229
- Journal of Biomechanics http://www.jbiomech.com/
- Sports Engineering https://link.springer.com/journal/12283
- Journal of Sports Engineering and Technology http://journals.sagepub.com/home/pip
- Vehicle System Dynamics
- Computational Benchmark Problems: http://real.uwaterloo.ca/benchmarks
