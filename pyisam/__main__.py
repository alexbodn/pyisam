from .isam import ISAMobject,StartMode,OpenMode
from .utils import ISAM_str
import os
import sys

if len(sys.argv) > 1 and sys.argv[1] in '1234':
  run_name = '__main{}__'.format(sys.argv[1])
elif __name__ == '__main__':
  run_name = '__main1__'
else:
  run_name = None

if run_name == '__main1__':
  from .table import ISAMtable
  from .tabdefns.stxtables import DEFILEdefn
  DEFILE = ISAMtable(DEFILEdefn)
  tabname = 'ref'
  def_rec = DEFILE.read(StartMode.ISGREAT,'key',tabname)
  while def_rec.filename == tabname:
    print(def_rec)
    def_rec = DEFILE.read()

if run_name == '__main2__':
  isamobj = ISAMobject()
  for errno in range(100,isamobj.is_nerr):
    print(errno,isamobj.strerror(errno))

if run_name == '__main3__':
  isamobj = ISAMobject()
  print(ISAM_str(isamobj.isversnumber))

if run_name == '__main4__':
  isamobj = ISAMobject()
  print(OpenMode.ISFIXLEN.value,OpenMode.ISFIXLEN.name)
