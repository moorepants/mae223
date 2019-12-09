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
the problem, background on how the system works heuristically, a literature
search to identify previous work on this problem, and a relatively complete
discussion of the way you hope to use the dynamic simulation to learn what you
have chosen to learn. This should take several pages to do completely. I urge
you to begin the selection of your system immediately and to discuss it with me
office hours so that I can help you in this phase. This proposal should be no
longer that three pages.

Proposal Rubric
~~~~~~~~~~~~~~~

- [10] Research question

  - Defined a research question
  - Research question is present but not articulated clearly
  - Did not define a research question

- [10] Literature review

  - Identified more than one relevant work or extensive discussion of at least
    one
  - Identified and discussed at least one relevant work
  - Did not look into the literature

- [10] System description

  - System described from a dynamics perspective
  - System described but lacking in description of dynamics
  - System not described

- [10] Methods description

  - Clear plan on how analysis and simulation may be used to answer research
    question
  - Plan on how to answer question is murky
  - No discussion of how analysis and simulation may be used to answer
    research question

- [10] Writing

  - Clear, coherent, and well organized
  - Writing and organization needs improvement
  - Not clear, coherent, or well organized

Thursday, December 12th
-----------------------

The final report is due. No submissions will be accepted after this date due to
the time needed to grade them.

Project Rubric
~~~~~~~~~~~~~~

Score will be between 50-100.

- [5] Research question

  - Research question is present and clearly defined.
  - Research question is present but not articulated clearly.
  - Did not define a research question.

- [10] System and model description

  - Text, equations, and figures are used to clearly describe the
    configuration, possible motion, inertial characteristics, and important
    loads acting on and of the system.
  - Text, equations, or figures are used to describe the configuration,
    possible motion, inertial characteristics, and important loads acting on
    and of the system, but not all aspects are clear.
  - System and model poorly described without text, equations, and figures.

- [10] Model Design

  - Model is designed with sufficient complexity to answer your research
    question and is not overly complex.
  - Model is designed with sufficient complexity to answer your research
    question.
  - Model is not appropriate for answering research question.

- [10] Model Correctness

  - Equations of motion are correct and simulation shows that the model behaves
    as expected.
  - Equations of motion are mostly correct and simulation shows the model
    mostly behaves as expected.
  - Equations of motion are incorrect and model does not behave as expected.

- [10] Analysis and Interpretation

  - Simulation or other analysis is demonstrated through text, plots, and
    optionally animations to address the research question. Interpretation of
    the results is correct and answers the research question.
  - Simulation or other analysis is demonstrated through text, plots, and
    optionally animations to address the research question. Interpretation of
    the results is mostly correct and answers the research question.
  - Simulation or other analysis not present and research question is not
    answered.

- [5] Writing

  - Clear, coherent, and well organized. All variables defined, plots labeled
    and explained. No extraneous elements in the notebook.
  - Writing and organization needs improvement; missing clarity, organization,
    variable definitions, labeled and explained plots, etc.
  - Not clear, coherent, or well organized.

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

Benchmark Problems
------------------

Library of Computational Benchmark Problems: https://www.iftomm-multibody.org/benchmark

Mechanisms
----------

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/CMQ241yGFtQ" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

There are thousands of interesting mechanisms. Here are several collections of
mechanisms to get some ideas from:

- `Nguyen Duc Thang's Animated Mechanisms`_ - A huge searchable YouTube video
  list of thousands of mechanisms and movements.
- `Mechanism collection - TU Delft`_
- `Kinematic Models for Digital Design Library`_
- `507 Mechanical Movements`_

.. _Nguyen Duc Thang's Animated Mechanisms: https://www.youtube.com/user/thang010146/videos
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
vehicles that would offer opportunities for multibody modeling. For example,
bicycles, scooters, motorcycles, monocycles, single wheel trailers, titling
vehicles, snake boards, unicycles, etc. `Wikipedia gives a good starting point
<https://en.wikipedia.org/wiki/Bicycle_and_motorcycle_dynamics>`_.

.. image:: https://upload.wikimedia.org/wikipedia/commons/5/5c/Bike_weaving.gif

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

The "`Bicycle and Motorcycle Dynamics <http://bmdconf.org>`_" conference has
proceedings about these vehicles.

Biomechanics
------------

Human Locomotion
~~~~~~~~~~~~~~~~

There a different "simple walking models" that could be appropriate for a class
project. Here are some papers:

- Collins, S., Ruina, A., Tedrake, R. & Wisse, M. Efficient Bipedal Robots
  Based on Passive-Dynamic Walkers. Science 307, 1082–1085 (2005).
- Garcia, M., Chatterjee, A., Ruina, A. & Coleman, M. The Simplest Walking
  Model: Stability, Complexity, and Scaling. J Biomech Eng 120, 281–288 (1998).
- Kuo, A. D. A Simple Model of Bipedal Walking Predicts the Preferred
  Speed–Step Length Relationship. J Biomech Eng 123, 264–269 (2001).

The Dynamic Walking conference has the best work on these topics. Here are the
video abstracts from a past conference:
http://robots.ihmc.us/dynamic-walking-abstracts-and-videos2012

Animal Motion
~~~~~~~~~~~~~

Animals have evolved a very large variety of ways to locomote from hopping,
sliding, flying, multi-legged walking, etc. Here are some related papers:

- Schmitt, J. & Holmes, P. Mechanical models for insect locomotion: dynamics
  and stability in the horizontal plane I. Theory. Biol Cybern 83, 501–515
  (2000).
- Koditschek, D. E. & Bühler, M. Analysis of a Simplified Hopping Robot. The
  International Journal of Robotics Research 10, 587–605 (1991).
- Hyon, S. H. & Mita, T. Development of a biologically inspired hopping
  robot-"Kenken". in Proceedings 2002 IEEE International Conference on Robotics
  and Automation (Cat. No.02CH37292) 4, 3984–3991 vol.4 (2002).
- Brown, B. & Zeglin, G. The bow leg hopping robot. in Proceedings. 1998 IEEE
  International Conference on Robotics and Automation (Cat. No.98CH36146) 1,
  781–786 vol.1 (1998).

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/M0ZXmGRCuts" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/qFmeHPVtK0o" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

Sports Biomechanics
-------------------

The Skateboard
~~~~~~~~~~~~~~

The basic skateboard dynamics offering a nice non-holomonic system to model.
See this paper:

Hubbard, M. Human control of the skateboard. Journal of Biomechanics 13,
745–754 (1980).

Another interesting aspects is that skateboarders are able to jump with the
skateboard seemingly attached to their feet, yet it isn't. The technique is
called the "ollie" and revolutionized the sport when invented. The technique is
now the foundation for hundreds of similar tricks. The skateboarder uses a
combination of popping the board at and angle and then lifting the board using
the friction between their foot and the surface of the board to bring the board
into the air. The goal of this project would be to develop a model of a
skateboard that can be "ollied" and attempt to do so.

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/339k4XEvbxY" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

Toys
----

There are numerous toys that dynamicist's find interesting, for example the
walking rabbit, the oloid, the rattleback, gyroscopes, snakeboards, etc. These
often provide nicely scoped models for the class project.

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/fRqwYsfiME8" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

.. raw:: html

   <iframe width="560" height="315"
   src="https://www.youtube.com/embed/11NHjiEYnI0" frameborder="0"
   allow="accelerometer; autoplay; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>

Others:

- http://www.dct.tue.nl/New/Leine/toys.html

Papers:

- Kane, T. R. & Levinson, D. A. Realistic mathematical modeling of the
  rattleback. International Journal of Non-Linear Mechanics 17, 175–186 (1982).
- Garcia, A., Hubbard, M. & Bondi, H. Spin reversal of the rattleback: theory
  and experiment. Proceedings of the Royal Society of London. A. Mathematical
  and Physical Sciences 418, 165–197 (1988).

Make Luxo the Pixar Lamp Jump!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pixar modeled a lamp, Luxo_, back in 1986 to hop around like it was alive. They
used multibody dynamics and space time optimization techniques. The original
paper is:

Witkin, A. & Kass, M. Spacetime Constraints. 10 (1988).

.. _Luxo: https://en.wikipedia.org/wiki/Luxo_Jr

Where to Find Other Ideas
-------------------------

- The mechanical_gifs subreddit usually has all kinds of fun machines that may
  inspire. http://reddit.com/r/mechanical_gifs

Journals
~~~~~~~~

- The Journal of Multibody Dynamics http://journals.sagepub.com/home/pik
- Multibody System Dynamics Journal http://www.springer.com/engineering/mechanics/journal/11044
- Journal of Applied Mechanics http://appliedmechanics.asmedigitalcollection.asme.org/issue.aspx?journalid=112&issueid=26229
- Journal of Biomechanics http://www.jbiomech.com/
- Sports Engineering https://link.springer.com/journal/12283
- Journal of Sports Engineering and Technology http://journals.sagepub.com/home/pip
- Vehicle System Dynamics
