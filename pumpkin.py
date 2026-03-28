import plan
from basic_tools import hvst, tosoil, moveto

PUMPKIN_SIZE = 8 * 8
pumpkin_grown_unit_mem = []

#OPTIMIZATIONS (TODO)
#Remember the fully grown pumpkin units, So
#the Drone can skip to check already grown pumpkin units


def action_pumpkin():
	again = True
	while again:
		again = False
		#"""이거는 셀 하나하나 호출이 아니라, 한번 호출하면 알아서 그 영역을 해결"""
		temp_pumpkin_route = []
		global pumpkin_grown_unit_mem

		for pos in plan.pumpkin_route:
			temp_pumpkin_route.append(pos)

		for pos in pumpkin_grown_unit_mem:
			if pos in temp_pumpkin_route:
				temp_pumpkin_route.remove(pos)
		
		for pos in temp_pumpkin_route:
			moveto(pos[0], pos[1])
			tosoil()

			if can_harvest() and (pos not in pumpkin_grown_unit_mem):
				_add_pcalc()
			else:
				plant(Entities.Pumpkin)
		
		if can_harvest_pumpkin():
			hvst()
			zero_pcalc()
			again = True
	
	return True

		
_num_grown_pumpkins = 0
		
#call this func when the drone's location is at 0
def zero_pcalc(): #pumpkin counter initialization
	global _num_grown_pumpkins
	global pumpkin_grown_unit_mem
	_num_grown_pumpkins = 0
	pumpkin_grown_unit_mem = []

#_fix : only call this function in this file
#call this function when you can find a grown pumpkin unit
def _add_pcalc(): #pumpkin counter add
	global _num_grown_pumpkins
	_num_grown_pumpkins += 1
	global pumpkin_grown_unit_mem
	pumpkin_grown_unit_mem.append([get_pos_x(), get_pos_y()])
	
def can_harvest_pumpkin():
	if _num_grown_pumpkins >= PUMPKIN_SIZE:
		return True
	else:
		return False