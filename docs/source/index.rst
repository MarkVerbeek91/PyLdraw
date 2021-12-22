.. pyldraw documentation master file, created by
   sphinx-quickstart on Sat Dec 18 20:19:55 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyldraw2's documentation!
====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   examples.rst


From LDraw.org:

   LDraw(TM) is an open standard for LEGO CAD programs that allow the user to create virtual LEGO models and scenes. You can use it to document models you have physically built, create building instructions just like LEGO, render 3D photo realistic images of your virtual models and even make animations. The possibilities are endless. Unlike real LEGO bricks where you are limited by the number of parts and colors, in LDraw nothing is impossible.

About Pyldraw2:

   Building on top of the original Pyldraw created by rienafairefr, which build his code on top of David Boddie code. Pyldraw2 is build from the group up, using modern software development techniques. It aims to be a stable, robust and fast interface between python and the LDraw standard.

Common use cases to be considered for this module, no particular order:

* create a python script to generate a repetitive structure in ldr. Like trees in a forrest.
* combining existing ldr models in to one module with a few lines of code
* be a basis for fast blender import plugins
* be a basis for fast pov-ray file export
* easy animation like the lua scripts in LDCad. (using the power python simulation might also become possible)

Examples
========

A few examples to demonstrate this module::

>>> # Create a model in python, add a brick and save to file
>>> from pathlib import Path
>>> from pyldraw.model import LdrModel
>>> from pyldraw.brick import Brick
>>>
>>> model = LdrModel(Path())
>>> model.add(Brick())
>>>
>>> model.save(Path('example1'))

Load a model from file::

>>> # Load a model from file, turn it 90 degrees around
>>> from pathlib import Path
>>> import numpy as np
>>> from pyldraw.model import LdrModel
>>>
>>> model = LdrModel(Path('example.ldr'))
>>> # np.rot90(model)

more example can be found here_

.. _here: examples.html

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
