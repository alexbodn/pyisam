'''
This module provides the exceptions raised by the package, this avoids a cyclic dependancy from being
created between the vaious sub-modules.
'''
__all__ = ('IsamException', 'IsamNotOpen', 'IsamOpened', 'IsamNotWritable',
           'IsamRecordMutable', 'IsamFuncFailed', 'IsamNoRecord')

# Define the shared exceptions raised by the package
class IsamException(Exception):
  'General exception raised by ISAM'
class IsamNotOpen(IsamException):
  'Exception raised when ISAM table not open'
class IsamOpened(IsamException):
  'Exception when ISAM table already opened'
class IsamNotWritable(IsamNotOpen):
  'Exception raised when ISAM table not opened with writable mode'
class IsamRecordMutable(IsamException):
  'Exception raised when given a not mutable buffer'
class IsamFunctionFailed(IsamException):
  'Exception raised when an ISAM function is not found in the libaray'
  def __init__(self, tabname, errno, errstr=None):
    self.tabname = tabname
    self.errno = errno
    self.errstr = errstr
  def __str__(self):
    return '{0.tabname}: {0.errno}' if self.errstr is None else '{0.tabname}: {0.errstr} ({0.errno})'.format(self)
class IsamNoRecord(IsamException):
  'Exception raised when no record was found'
class IsamNoIndex(IsamException):
  'Exception raised when an index is missing from a table instance'
  def __init__(self, tabname, idxname):
    self.tabname = tabname
    self.idxname = idxname
  def __str__(self):
    return "Index '{0.idxname.name}' is not available on table '{0.tabname}'".format(self)
