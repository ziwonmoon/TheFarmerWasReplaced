import plan
from basic_tools import moveto, tosoil, hvst

def action_cactus():
	for temp_pos in plan.cactus_route:
		bubble = False
		for pos in plan.cactus_route:
			moveto(pos[0], pos[1])
			tosoil()
			plant(Entities.Cactus)
			if measure(East) != None:
				if measure() > measure(East):
					swap(East)
					bubble = True
			if measure(West) != None:
				if measure() < measure(West):
					swap(West)
					bubble = True
			if measure(South) != None:
				if measure() < measure(South):
					swap(South)
					bubble = True
			if measure(North) != None:
				if measure() > measure(North):
					swap(North)
					bubble = True
		if not bubble:
			break
	hvst()