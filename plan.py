import module_list

plan_map = [] #[[tree, tree], [tree, sunflower]]
sunflower_route = [] #[[1, 2], [3, 4]]
grass_and_tree_route = [] #[[1, 2], [3, 4]]
carrot_route = []
pumpkin_route = []
cactus_route = []

NUM_SUNFLOWER = 0
NUM_PUMPKIN = 0


#RULE : 해바라기와 선인장은 인접해서는 안 된다. (대각선은 허용)
def get_designated_produce(x, y):
	if x == 1:
		return Entities.Sunflower
	elif x == 0 or x == 2:
		return Entities.Carrot
	elif y < 3:
		if (x % 3 == 0 and y % 2 == 0) or (x % 3 == 1 and y % 2 == 1):
			return Entities.Tree
		else:
			return Entities.Grass
	elif x >= 5 and y >= 5:
		return Entities.Pumpkin
	else:
		return Entities.Cactus
	
def generate_plan_data():
	global NUM_SUNFLOWER
	global NUM_PUMPKIN
	global plan_map
	global sunflower_route
	global grass_and_tree_route
	global carrot_route
	global pumpkin_route
	global cactus_route

	for x in range(get_world_size()):
		plan_map.append([])
		for y in range(get_world_size()):
			temp_area_kind = get_designated_produce(x, y)
			plan_map[x].append(temp_area_kind)
			if temp_area_kind == Entities.Sunflower:
				sunflower_route.append([x, y])
				NUM_SUNFLOWER += 1
			elif temp_area_kind == Entities.Grass or temp_area_kind == Entities.Tree:
				grass_and_tree_route.append([x, y])
			elif temp_area_kind == Entities.Carrot:
				carrot_route.append([x, y])
			elif temp_area_kind == Entities.Pumpkin:
				NUM_PUMPKIN += 1
				pumpkin_route.append([x, y])
			else:
				cactus_route.append([x, y])