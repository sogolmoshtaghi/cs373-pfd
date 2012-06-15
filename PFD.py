
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
    while l_idx < size :
		assert int(l[l_idx]) > 0 
		assert int(l[l_idx]) < 101
		assert int(l[0]) != 0 
		a[int(l[0])][l_idx-1] = int(l[l_idx])
		l_idx += 1
		#size -= 1
    return True



def PFD_eval(i,j):
	i_size = len(i[0])
	idx = 1
	while i_size >  idx :
		jdx = 1
		while i_size > jdx :
			if i[idx][jdx] != None :
				j[i[idx][jdx]].append(idx)
			jdx += 1
		idx += 1
	return j

	
	
	


def PFD_print(w,v):

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
    a = [[None]*(vertex_count+1) for _ in range(vertex_count+1)]	#Creates 2D list that has individual references to each cell
    successors = [[None]*(1) for _ in range(vertex_count+1)]
    print successors
    while PFD_read(r, a) :											#Reads individual lines, with the first one already read in line #66
        v = PFD_eval(a, successors)												
        PFD_print(w,v)												
