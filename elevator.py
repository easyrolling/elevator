import sys

def elevate(start, moves, mode):
	floors = 0
	stops = [start]
	i = 0
	
	while i < len(moves):
		move = moves[i]
		
		lstops = []
		
		lstops.append(move[0])
		lstops.append(move[1])
		
		if mode == 'B': # if B, iterate through next moves in the same direction and populate lstops list
			while (i+1) < len(moves):
				if (moves[i+1][1] - moves[i+1][0])*(move[1] - move[0]) > 0: # next move is in the same direction
					if moves[i+1][0] not in lstops:
						lstops.append(moves[i+1][0])
					if moves[i+1][1] not in lstops:
						lstops.append(moves[i+1][1])
					i += 1
				else:
					break;
			# sort stops according to the direction
			if (move[1] - move[0]) > 0: #up
				lstops.sort()
			else: #down
				lstops.sort(reverse=True)
			
		if(lstops[0] == stops[len(stops)-1]): # check if previous stop isn't the same as the next pickup
			lstops.pop(0)
		
		stops.extend(lstops)
		i += 1
	
	# calculate the distance
	last = stops.pop(0)
	for stop in stops: # calculate floors
		floors += abs(stop - last)
		last = stop
			
	print start, ' '.join([str(n) for n in stops]), '(', floors, ')'
	
def parse(input):
	a = input.split(':')
	start = int(a[0])
	parts = a[1].split(',')
	moves = [[int(n) for n in part.split('-')] for part in parts ]
	return (start, moves)


if __name__ == "__main__":
	input = ''
	if(len(sys.argv) > 1):
		input = sys.argv[1]
	else:
		print 'no input file specified'
		exit()
	
	mode = 'A'
	if(len(sys.argv) >2):
		mode = sys.argv[2]
		
	f = open(input, 'r')
	for line in f:
		(start, moves) = parse(line)
		elevate(start, moves, mode)	
	
	
		
	
	
		

