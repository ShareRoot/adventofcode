import sys
presents_filename = sys.argv[1]
presents_file = open(presents_filename, "r")
total_surface_area = 0
for present in presents_file:
	dimensions = present.split('x')
	l = int(dimensions[0])
	print l
	w = int(dimensions[1])
	print w
	h = int(dimensions[2])
	print h
	curr_surface_area = 2*l*w + 2*w*h + 2*h*l
	smallest_side = w*h
	if smallest_side > h*l:
		smallest_side = h*l
	if smallest_side > l*w:
	    smallest_side = l*w
	total_surface_area = total_surface_area + curr_surface_area + smallest_side
print total_surface_area