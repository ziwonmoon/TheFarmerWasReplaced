import plan
from basic_tools import hvst, tosoil

def action_carrot():
	if plan.get_designated_produce(get_pos_x(), get_pos_y()) != Entities.Carrot:
		return False
		
	tosoil()
		
	hvst()
	plant(Entities.Carrot)
	
	return True
	
		
		