Contribution Guidelines
#######################

Whether reporting bugs, discussing improvements and new ideas: Contributions to
Pyfield are highly welcomed and appreciated! Here's how to get started:

1. Check for open issues or open a fresh issue to start a discussion around a
   feature idea, bug or typo error
2. Fork `the repository <https://githuv.com/Ublimjo/pyfield/>`_ on GitHub,
   create a new branch off the `master` branch and start making your changes
   (known as 
   `GitHub Flow <https://guides.github.com/introduction/flow/index.html>`_)
3. Write a test which shows that the bug was fixed or that the feature works as
   expected
4. Send a pull request and bug the maintainer until it gets merged and published :)


Report bugs
***********

Report bugs for pyfield in the
`issue tracker <https://github.com/Ublimjo/pyfield/issues>`_.

If you can write a demonstration test that currently fails but should pass
(xfail), that is a very useful commit to make as well, even if you cannot            fix the bug itself.


Branch
******

Use `master` branch for:

  - typo fix
  - small bug fix

Use `develop` branch for:

  - big bug fix
  - small feature
  - documentation

Use another branch for:

  - new idea
  - new big feature
  - ...


Code Conventions
****************

In general the pyfield source should always follow
`PEP 8 <http://legacy.python.org/dev/peps/pep-0008/>`_. However we make a small
axception concerning docstrings:

when using multiline docstrings, keep the opening and closing triple quotes on
their own lines and add an empty li'e after it. Using yapf is recommended.

.. code-block:: python

    def some_function():
        """
        Documentation ...
        """

        # implementation ...

Try to make:

  - 100% coverage
  - 10/10 pylint


Version Numbers
***************

Pyfield follows the `SemVer versioning guidelines <http://semver.org/>`_.
This implies that backwards incompatible changes in the API will increment
the major version. So think twice before making such changes.

Pyfield use pyscaffold API so the project version is on git tag.
