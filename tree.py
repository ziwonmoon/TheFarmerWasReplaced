import plan
from basic_tools import hvst

def action_tree():
	if plan.get_designated_produce() != Entities.Tree:
		return False
		
	hvst()
	plant(Entities.Tree)
		
	return True