Web Dev
=======

Documentation for all web dev code.

.. toctree::
    :caption: Contents
    :maxdepth: 1

    global/index.rst
    settings/index.rst

Setup
-----

1. Clone `CreateBase/Documentation <https://github.com/CreateBaseNZ/Documentation>`_ to your local machine
2. Open the repository root folder in VS Code
3. Open ``conf.py`` found in ``docs/source`` and run it (``F5``) to activate a Python environment
4. Open the terminal console (``Ctrl + ~``)
5. Install Sphinx::

    pip install -U sphinx

6. Install JSDoc::

    npm install -g jsdoc

7. Install sphinx-js::

    pip install sphinx-js

8. Set automatic ``git submodule update`` on ``git pull`` by running in terminal::

    git config --global submodule.recurse true

9. Create a ``requirements.txt`` file in ``docs`` and enter::

    sphinx-js==3.1

10. Create a ``.readthedocs.yml`` file in the root directory and enter
    ::

      version: 2

      build:
        image: latest

      sphinx:
        configuration: docs/source/conf.py

      submodules:
        include: all

      python:
        version: 3.7
        install:
          - requirements: docs/requirements.txt

11. Update the ``application`` submodule with
    ::
      
      git submodule update --remote --merge

12. Compile ``.rst`` files by running in the ``docs`` directory
    ::

      cd docs
      make html

----

Useful Links
------------

- `rst CheatSheet <https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html>`_
- `Jsdoc cheatsheet <https://devhints.io/jsdoc>`_
- `Introducing sphinx-js, a better way to document large JavaScript projects <https://hacks.mozilla.org/2017/07/introducing-sphinx-js-a-better-way-to-document-large-javascript-projects/>`_
- `Utilising docstrings - Stack Overflow <https://hacks.mozilla.org/2017/07/introducing-sphinx-js-a-better-way-to-document-large-javascript-projects/>`_
- `sphinx-js 3.1 <https://pypi.org/project/sphinx-js/>`_
- `Configuration File - Read the Docs <https://docs.readthedocs.io/en/latest/config-file/index.html>`_
- `Is there a way to make git pull automatically update submodules? - Stack Overflow <https://stackoverflow.com/questions/4611512/is-there-a-way-to-make-git-pull-automatically-update-submodules>`_
