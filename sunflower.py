import plan
from basic_tools import hvst, tosoil, moveto

NUM_SUNFLOWER = 16

much_leaves_pos = [-1, -1]
_num_counted_sunflowers = 0
num_much_leaves = -1

def _add_num_counted_sunflowers():
	global _num_counted_sunflowers
	_num_counted_sunflowers += 1

def zero_scalc():
	global _num_counted_sunflowers
	_num_counted_sunflowers = 0

def action_sunflower():
	if plan.get_designated_produce() != Entities.Sunflower:
		return False
		
	tosoil()
	
		
	plant(Entities.Sunflower)
	
	global num_much_leaves
	global much_leaves_pos
	
	temp_num_leaves = measure()
	if temp_num_leaves > num_much_leaves:
		num_much_leaves = temp_num_leaves
		much_leaves_pos = [get_pos_x(), get_pos_y()]
	_add_num_counted_sunflowers()
	
	global _num_counted_sunflowers
	if _num_counted_sunflowers >= NUM_SUNFLOWER:
		current_pos = [get_pos_x(), get_pos_y()]
		moveto(much_leaves_pos[0], much_leaves_pos[1])
		hvst()
		plant(Entities.Sunflower)
		moveto(current_pos[0], current_pos[1])
		_num_counted_sunflowers = 0
		much_leaves_pos = [-1, -1]
		num_much_leaves = -1
	
	return True
	
	
	
	