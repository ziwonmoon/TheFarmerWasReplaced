import plan
from basic_tools import hvst

def action_tree():
	if plan.get_designated_produce(get_pos_x(), get_pos_y()) != Entities.Tree:
		return False
		
	hvst()
	plant(Entities.Tree)
		
	return True