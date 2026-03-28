import plan
from basic_tools import hvst, tosoil, moveto

def action_sunflower():
	num_leaves = [] #잎의 개수 리스트, 정렬 : 라우트와 같음
	leaves_ordered_route = [] #라우트, 정렬 : 잎 개수 순

	for pos in plan.sunflower_route:
		moveto(pos[0], pos[1])
		tosoil()
		plant(Entities.Sunflower)
		num_leaves.append(measure())


	#삽입정렬.. 아 오랫만이라.. 너무.. 머리가..멍청해..
	temp_leaves = [] #잎의 개수 리스트. 정렬:내림차순
	
	temp_leaves.append(num_leaves[0])
	leaves_ordered_route.append(plan.sunflower_route[0])

	for i in range(len(num_leaves)):
		inserted = False
		for j in range(len(temp_leaves)):
			if num_leaves[i] >= temp_leaves[j]:
				temp_leaves.insert(j, num_leaves[i])
				leaves_ordered_route.insert(j, plan.sunflower_route[i])
				inserted = True
				break
		if not inserted:
			temp_leaves.append(num_leaves[i])
			leaves_ordered_route.append(plan.sunflower_route[i])

	# 삽입정렬 끝

	for i in range(plan.NUM_SUNFLOWER - 10):
		moveto(leaves_ordered_route[i][0], leaves_ordered_route[i][1])
		hvst()

	for i in range(plan.NUM_SUNFLOWER - 10):
		moveto(leaves_ordered_route[i][0], leaves_ordered_route[i][1])
		plant(Entities.Sunflower)

	return True
	
	
	
	