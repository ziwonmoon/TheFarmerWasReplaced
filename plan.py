plan_map = [] #[[tree, tree], [tree, sunflower]]
sunflower_map = [] #[[1, 2], [3, 4]]
grass_and_tree_map = [] #[[1, 2], [3, 4]]
carrot_map = []
pumpkin_map = []

def get_designated_produce(x, y):
	if (x < 4 and y < 4):
		return Entities.Sunflower
	elif x >= 4 and y < 4:
		if (x % 3 == 0 and y % 2 == 0) or (x % 3 == 1 and y % 2 == 1):
			return Entities.Tree
		else:
			return Entities.Grass
	elif x < 4 and y >= 4:
		return Entities.Carrot
	else:
		return Entities.Pumpkin
	
def generate_plan_data():
	global plan_map
	global sunflower_map
	global grass_map
	global tree_map
	global carrot_map
	global pumpkin_map

	for x in range(get_world_size()):
		plan_map.append([])
		for y in range(get_world_size()):
			temp_area_kind = get_designated_produce(x, y)
			plan_map[x].append(temp_area_kind)
			if temp_area_kind == Entities.Sunflower:
				sunflower_map.append([x, y])
			elif temp_area_kind == Entities.Grass or temp_area_kind == Entities.Tree:
				grass_and_tree_map.append([x, y])
			elif temp_area_kind == Entities.Carrot:
				carrot_map.append([x, y])
			else:
				pumpkin_map.append([x, y])
				
