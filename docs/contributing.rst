.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/micahjohnson150/spatialnc/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

spatialnc could always use more documentation, whether as part of the
official spatialnc docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/micahjohnson150/spatialnc/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `spatialnc` for local development.

1. Fork the `spatialnc` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/spatialnc.git

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development::

    $ mkvirtualenv spatialnc
    $ cd spatialnc/
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the tests::

    $ flake8 spatialnc tests
    $ python setup.py test or pytest
    
   To get flake8, just pip install them into your virtualenv.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.rst.
3. The pull request should work for Python 3.6 and above. Check
   https://github.com/USDA-ARS-NWRC/spatialnc/actions
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ pytest tests.test_spatialnc


Releasing to PyPI
-----------------
To create a new release on `Pypi.org <https://pypi.org/>`_, follow these steps:

#. Create a new release for spatialnc
#. Name the tag and release the version number, for example `v0.4.1 <https://github.com/USDA-ARS-NWRC/spatialnc/releases/v0.4.1>`_
#. Add documentation about the release and why it's different from the previous.
   Especially highlight any changes that will break existing integrations.
#. Publish new release which will trigger a build to release to PyPI