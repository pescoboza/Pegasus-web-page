# Useful Details
**A. K. A.** little practical coding/markdown insights to keep in mind in special situations.

### Python relative imports
Use the `'.'` operator to mean this package. Double `.` (`..`) means on the level of sibling modules/packages.

Use the `'.'` operator as in "from . import object" for objects in the `__init__.py` file. 

In a child package `'.'` used as above means "parent.child" as in: `from .. import object` actually means `from parent.this_package import object`.

When one wants to import from a sibling package use `..`. Example: `from ..package import object` translates to `from parent.sibling_package import object`.
