HALV_SIZE = get_world_size() // 2
import module_list

def action_wildcard(entity):
	if entity == Entities.Carrot:
		import carrot
		carrot.action_carrot()
	elif entity == Entities.Tree:
		import tree
		tree.action_tree()
	elif entity == Entities.Grass:
		import grass
		grass.action_grass()
	elif entity == Entities.Bush:
		import bush
		bush.action_bush()
	else:
		print(-1)

def hvst():
	if can_harvest():
		harvest()
		
def tosoil():
	if get_ground_type() != Grounds.Soil:
		till()

def togrsld():
	if get_ground_type() != Grounds.Grassland:
		till()
		
def moveto(x, y):
	while True:
		abs_res_x = get_pos_x() - x
		if abs_res_x < 0:
			abs_res_x *= -1
		abs_res_y = get_pos_y() - y
		if abs_res_y < 0:
			abs_res_y *= -1
		
		if abs_res_x == 0 and abs_res_y == 0:
			break
			
		if x - get_pos_x() > 0:
			if abs_res_x < HALV_SIZE:
				move(East)
			else:
				move(West)
		elif x - get_pos_x() < 0:
			if abs_res_x < HALV_SIZE:
				move(West)
			else:
				move(East)
		if y - get_pos_y() > 0:
			if abs_res_y < HALV_SIZE:
				move(North)
			else:
				move(South)
		elif y - get_pos_y() < 0:
			if abs_res_y < HALV_SIZE:
				move(South)
			else:
				move(North)


def modify_route(route):
	prev_x = route[0][0]
	double_listed = []
	double_listed.append([])
	i = 0

	
	for pos in route:
		if prev_x == pos[0]:
			double_listed[i].append(pos)
		else:
			prev_x = pos[0]
			i += 1
			double_listed.append([])
			double_listed[i].append(pos)
	
	for i in range(len(double_listed)):
		if i % 2 == 1:
			module_list.flip(double_listed[i])
	

	for i in range(len(route)):
		route.pop()

	for li in double_listed:
		for ji in li:
			route.append(ji)
		
