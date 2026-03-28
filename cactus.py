import plan
from basic_tools import moveto, tosoil, hvst

def action_cactus():
	for pos in plan.cactus_route:
		moveto(pos[0], pos[1])
		tosoil()
		hvst()
		plant(Entities.Cactus)
		