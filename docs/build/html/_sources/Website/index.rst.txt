Web Dev
=======

Documentation for all web dev code.

.. toctree::
    :caption: Contents
    :maxdepth: 1

    Settings/index.rst

Setup
-----

1. Clone `CreateBase/Documentation <https://github.com/CreateBaseNZ/Documentation>`_ to your local machine
2. Open the repository root folder in VS Code
3. Open ``conf.py`` found in ``./docs/source`` and run it (``F5``) to activate a Python environment
4. Open the terminal console (``Ctrl + ~``)
5. Install Sphinx::

    pip install -U sphinx

6. Install JSDoc::

    npm install -g jsdoc

7. Install sphinx-js::

    pip install sphinx-js

8. Enable sphinx-js by adding it to ``extensions`` in ``conf.py``::

    extensions = ['sphinx_js']

9. Add path to the JavaScript files::

    # the path starts at conf.py
    js_source_path = 'path/to/application/public/javascripts'

10. Change directory to ``docs``
    ::
      
      cd docs

11. Compile ``.rst`` files by running
    ::

      make html

Restructred Text (reST) and Sphinx - Simple Guide
-------------------------------------------------

Basics
,,,,,,

*Italicised*, **bold**, ``verbatim``, and `hyperlinked <#>`_ text are written as so::

    *italic*
    **bold**
    ``verbatim``
    `link text <hyperlink>`_

Headings
,,,,,,,,

When it comes to writing headings, there are two rules:
1. Use at least as many characters as the length of the heading
2. Be consistent with character usage

To write a heading, just underline it. There is no heading heirarchy assigned to certain underline characters as it is determined by the succession of headings. For consistency, we will use the following convention::

    Section
    =======

    Subsection
    ----------

    Subsubsection
    ,,,,,,,,,,,,,

    Subsubsubsection
    ................

All headings are considered as internal hyperlinks and can be referred to using::
    
    `Basics`_

