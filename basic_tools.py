HALV_SIZE = get_world_size() // 2

def hvst():
	if can_harvest():
		harvest()
		
def tosoil():
	if get_ground_type() != Grounds.Soil:
		till()

def togrsld():
	if get_ground_type() != Grounds.Grassland:
		togrsld()
		
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