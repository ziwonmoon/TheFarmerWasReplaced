import pumpkin, carrot, sunflower, tree, grass, cactus
import plan
from basic_tools import moveto, modify_route, action_wildcard

if __name__ == "__main__":
	clear()
	change_hat(Hats.Traffic_Cone)

	plan.generate_plan_data()

	modify_route(plan.sunflower_route)
	modify_route(plan.grass_and_tree_route)
	modify_route(plan.carrot_route)
	modify_route(plan.pumpkin_route)
	modify_route(plan.cactus_route)
	
	do_a_flip()

	while True:
		## Sunflower Phase
		change_hat(Hats.Sunflower_Hat)
		sunflower.action_sunflower()

		## Grass and Tree Phase
		change_hat(Hats.Straw_Hat)
		for pos in plan.grass_and_tree_route:
			moveto(pos[0], pos[1])
			action_wildcard(plan.get_designated_produce(get_pos_x(),get_pos_y()))

		## Carrot Phase
		change_hat(Hats.Carrot_Hat)
		for pos in plan.carrot_route:
			moveto(pos[0], pos[1])
			carrot.action_carrot()

		## Pumpkin Phase
		change_hat(Hats.Pumpkin_Hat)
		pumpkin.action_pumpkin()
		
		
		## Cactus Phase
		change_hat(Hats.Gray_Hat)
		cactus.action_cactus()

		
	