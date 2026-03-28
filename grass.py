import plan
from basic_tools import hvst

def action_grass():
	if plan.get_designated_produce() != Entities.Grass:
		return False
		
	hvst()
	plant(Entities.Grass)