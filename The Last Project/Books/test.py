import datetime

from Controller import BookController
from library_da import LibraryDa
from library import Library
from Person_Controller import PersonController
from Bill_Controller import BillController
from datetime import *
from bill_da import BillDa
from bill import Bill

# lib = Library("aaa", "132132", "radman", "english", "action", 1)

# LibraryDa().save(lib)
# BookController().delete(8)
# BillController().save(str(datetime.now()), "12341234", "aaa")
BillController().save(datetime.now(), "12341234", "aaa", "1000")
print(BillController().find_all())