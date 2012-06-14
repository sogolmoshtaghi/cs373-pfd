
# ---------------------------
# Sogol Moshtaghi
# Oscar chavarria
# PFD
# ---------------------------

# ------------
# PFD_read
# ------------

arrayprint = [[0]]

def PFD_read (r, a) :
    """
reads two ints into a[0] and a[1]
r is a reader
a is an array on int
return true if that succeeds, false otherwise
"""
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    size = len(a[0])
    l_idx = 1
    while size > 0 :
		assert int(l[l_idx]) > 0 
		assert int(l[l_idx]) < 101
		assert int(l[0]) != 0 
		a[int(l[0])][l_idx-1] = int(l[l_idx])
		l_idx += 1
		size -= 1
    arrayprint = a
    return True



def PFD_eval(i):
	return 1


def PFD_print(w,v):
#	size2 = len(arrayprint[0])
#	size3 = len(arrayprint)
#	idxtwo = 0
#	idx3 = 0
#	while size3 > 0 :
#		while size2 > 0 :
#			w.write(str(arrayprint[idxtwo][idx3])
#			idxtwo += 1
#			size2 -= 1
#		idx3 += 1
#		size3 -= 1
	w.write("high")	
	

def PFD_solve (r, w) :
    """
read, eval, print loop
r is a reader
w is a writer
"""
    s = r.readline()
    if s == "" :
		return false
    l = s.split()
    vertex_count = int(l[0])
    rule_count = int(l[1])
    idx = 0
    a = [[0]] * (vertex_count+1)
    while PFD_read(r, a) :
        v = PFD_eval(a)
        PFD_print(w,v)
