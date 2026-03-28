def get_designated_produce():
	if (get_pos_x() < 4 and get_pos_y() < 4):
		return Entities.Sunflower
	elif get_pos_x() >= 4 and get_pos_y() < 4:
		if (get_pos_x() % 3 == 0 and get_pos_y() % 2 == 0) or (get_pos_x() % 3 == 1 and get_pos_y() % 2 == 1):
			return Entities.Tree
		else:
			return Entities.Grass
	elif get_pos_x() < 4 and get_pos_y() >= 4:
		return Entities.Carrot
	else:
		return Entities.Pumpkin