

# -------------------------------
# Sogol Moshtaghi
# Oscar chavarria
# -------------------------------

"""
To test the program:
% python TestPFD.py >& TestPFD.py.out
% chmod ugo+x TestPFD.py
% TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import unittest

from PFD import PFD_read, PFD_eval, PFD_print, PFD_solve

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO.StringIO("1 1 2\n")
        a = [[0]*(3) for _ in range(3)]
        b = PFD_read(r, a)
        #self.assert_(b == True)
        #self.assert_(a[2][0] == 2)
        
	# ----
    # eval
    # ----

    def test_eval(self) :
		a = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [2, 5, 3, 0, 0, 0], [2, 1, 5, 0, 0, 0], [1, 3, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]]
		b = [[0]*(1) for _ in range(6)]
		v = PFD_eval(a, b)
		print v

    def test_PFD_removal(self) :
		a = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [2, 5, 3, 0, 0, 0], [2, 1, 5, 0, 0, 0], [1, 3, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]]
		b = [[0]*(1) for _ in range(6)]
		v = PFD_eval(a, b)
		print "result= ",v
        
        
        
        
        
# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
