import plan
from basic_tools import hvst, tosoil

PUMPKIN_SIZE = 8 * 8
PUMPKIN_GROWN_UNIT_MEM = []

#OPTIMIZATIONS (TODO)
#Remember the fully grown pumpkin units, So
#the Drone can skip to check already grown pumpkin units


def action_pumpkin():
	if plan.get_designated_produce() != Entities.Pumpkin:
		return False
		
	if can_harvest() and get_entity_type() == Entities.Pumpkin:
		_add_pcalc()
	
	if can_harvest_pumpkin():
		hvst()
		
		
	#PUMPKIN'S OWN SEARCH MECHANISM

	tosoil()
	
	plant(Entities.Pumpkin)
	return True

		
_num_grown_pumpkins = 0
		
#call this func when the drone's location is at 0
def zero_pcalc(): #pumpkin counter initialization
	global _num_grown_pumpkins
	global PUMPKIN_GROWN_UNIT_MEM
	#_num_grown_pumpkins = len(PUMPKIN_GROWN_UNIT_MEM)
	_num_grown_pumpkins = 0

#_fix : only call this function in this file
#call this function when you can find a grown pumpkin unit
def _add_pcalc(): #pumpkin counter add
	global _num_grown_pumpkins
	_num_grown_pumpkins += 1
	global PUMPKIN_GROWN_UNIT_MEM
	PUMPKIN_GROWN_UNIT_MEM.append([get_pos_x(), get_pos_y()])
	
def can_harvest_pumpkin():
	if _num_grown_pumpkins >= PUMPKIN_SIZE:
		return True
	else:
		return False