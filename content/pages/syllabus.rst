:title: Syllabus
:url:
:save_as: index.html
:sortorder: 0

Course Description
==================

| University of California, Davis
| Department of Mechanical and Aerospace Engineering
| Multibody Dynamics
| Fall 2017, Lecture: MW 10:00-11:50 AM
| CRN: 63597

After the completion of this class you will have developed the skills to model,
interpret, simulate, and analyze `multibody systems`_, i.e. systems which are
made up of interconnected rigid bodies with arbitrary constraints and applied
loads. Mathematical models of multibody systems are typically very useful at
predicting the motion of macro scale objects. `Newton's laws of motion`_ are
the foundation of developing predictive models of these systems.  Examples of
systems you will be able to model are: spacecraft trajectories, human/animal
biomechanics, vehicle motion, robot motion, etc.

.. _multibody systems: https://en.wikipedia.org/wiki/Multibody_system
.. _Newton's laws of motion: https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion

Catalog Description
-------------------

   Lecture—4 hours. Prerequisite: Engineering 102. Coupled rigid-body
   kinematics/dynamics; reference frames; vector differentiation; configuration
   and motion constraints; holonomicity; generalized speeds; partial
   velocities; mass; inertia tensor/theorems; angular momentum; generalized
   forces; comparing Newton/Euler, Lagrange's, Kane's methods; computer-aided
   equation derivation; orientation; Euler; Rodrigues parameters. (Same course
   as Biomedical Engineering 223.)—W, S. (W.) Eke, Ravani

Learning Objectives
-------------------

Students will be able to:

- formulate a model and free body diagram of multibody systems
- derive the equations of motion of a multibody system
- incorporate holonomic and nonholonomic constraints into a multibody system
- simulate the motion of a multibody system with a computer
- interpret and analyze the results of simulation

Prerequites
-----------

The only required prerequisite is Engineering 102 or a similar course in
introductory dynamics. You should also be proficient at at least one scientific
programming language. We will be using Python in class.

Instructor
==========

| Jason K. Moore
| 2095 Bainer Hall
| 530-752-4805
| jkm@ucdavis.edu

Time and Location
=================

We will meet in Bainer 1070 on Mondays and Wednesday from 10:00 AM to 11:50 AM.

**If you have any conflicts with the schedule you must tell me by email in the
first week of class (emergencies will be the only exception).**

Office Hours
============

Office hours are TBA. If you can't make the regular scheduled office hours,
check Jason's `work calendar`_ for an open time slot between 8AM and 6:30PM on
weekdays and email him with a request for a meeting.

.. _work calendar: http://www.moorepants.info/work-calendar.html

Academic Integrity
==================

Academic dishonesty will not be tolerated. Please visit the `Academic Integrity
web page`_ from UC Davis Office of Student Judicial Affairs to review the
campus' policy on academic responsibility and integrity and read the UC Davis
`code of academic conduct`_.

.. _Academic Integrity web page: http://sja.ucdavis.edu/academic-integrity.html
.. _code of academic conduct: http://sja.ucdavis.edu/cac.html

Course Text and Materials
=========================

The majority of preparation and readings for the lectures will come from this
textbook:

   Thomas R. Kane, and David A. Levinson. Dynamics, Theory and Application.
   McGraw Hill, 1985. http://hdl.handle.net/1813/638.

Note that the book is out of print, but you can download a PDF copy from
Cornell's eCommons digital repository for personal use. Additionally, the
following book may also be a useful reference for some topics:

   Thomas R. Kane, Peter W. Likins, and David A. Levinson. Spacecraft Dynamics.
   McGraw Hill, 1983. http://hdl.handle.net/1813/637.

There are many advanced dynamics books that provide useful information but
these two present the material in the context and notation that we will use in
class. Other useful references will be added to the resources tab of this
website as we move through the course.

Software
========

We will be making extensive use of PyDy_ and SymPy_ to model and simulate
multibody systems. These packages are written in the open source Python
programming language and leverage the SciPy ecosystem of scientific and
engineering computing tools. You will have access to these through our
JupyterHub server at bicycle.ucdavis.edu_. You may also install the software on
your own computer. You will need to bring your laptop, tablet, or phone to
class to follow along with the interactive sessions. See the `software page`_
on this website for more information.

.. _PyDy: http://pydy.org
.. _SymPy: http://sympy.org
.. _bicycle.ucdavis.edu: https://bicycle.ucdavis.edu

Assignments & Grades
====================

Being a graduate class, we will not be focused on grading many different
detailed aspects of the class. You will be expected to do as much or little
practice as needed to pass the exams and complete your project. Homework
problems will be suggested but not graded. I recommend talking through homework
solutions with your classmates and me during office hours.

Grades will be available in the canvas.ucdavis.edu_ grade book periodically
throughout the course along with class statistics. Check the website on a
regular basis to gauge your performance. Keep in mind that **15% is deducted
per business day late** on any graded assignments.

.. _canvas.ucdavis.edu: http://canvas.ucdavis.edu

=========================  ===
Assignment                 %
=========================  ===
Exam 1                     30%
Exam 2                     30%
Project                    40%
=========================  ===

Exams
   Two take home exams will be given. These must be completed individually. You
   can use any materials you want but you are on your honor to not discuss the
   exams questions with any other person other than the instructor.
Project
   You will be expected to complete a modeling, simulation, and analysis
   project that you design on your own. You are encouraged to discuss this
   project with others, but you must do all of the work and presentation
   yourself. You will give a short lightning presentation on the results to the
   class during the final exam time.

Canvas
======

We will make use of Canvas for the course. Log in to canvas.ucdavis.edu_ with
your Kerberos ID and passphrase then select **MAE 223 001 FQ 2017**.

We will be using several features in Canvas:

Announcements
   This will be my primary communication avenue to you. These announcements
   will be forwarded automatically to your UCD email address. You are expected
   to read these either through your email program or on the Canvas website.
Assignments
   Any assignments will be distributed here and collected here.
Grades
   Your grades and basic stats on your relative performance will be available
   as the course goes along.
Files
   Copyrighted and private files, documents, and other resources will be
   available here for download. The rest will be available for download on this
   website.

Communication
=============

This class requires a lot of communication: among your team, with your
sponsors, with your mentors, and with the instructors. This can quickly get
unmanageable, especially for the instructors' email inboxes. So here are some
simple rules to follow with respect to communication:

`Piazza <http://piazza.com/ucdavis/fall2017/mae223>`_
   This is the first place to ask questions. Use this forum to ask questions
   that are general for the class. Try to restructure your less general
   questions into general ones so you can ask here. This minimizes the number
   of times a question has to be answered and allows both students and
   instructors to collectively answer questions. Note that there is a single
   instructor answer and a single student(s) answer. Your contributions to
   answering questions on Piazza will be used to boost your grade on borderline
   cases.
Email
   Use email for individualized communication, i.e. for questions about project
   specifics or other personal needs. Prepend "[MAE223]" to their subject line.
Office Hours
   Please come visit me in office hours to discuss your work. The earlier, the
   better.
Appointments
   You may schedule an appointment with me outside of office hours if all of
   the above doesn't work for some reason. Use this as a last resort.
