import pumpkin, carrot, sunflower, tree, grass
import plan
from basic_tools import moveto

if __name__ == "__main__":
	clear()
	change_hat(Hats.Traffic_Cone)
	plan.generate_plan_data()
	
	do_a_flip()

	while True:
		## Sunflower Phase
		change_hat(Hats.Purple_Hat)
		sunflower.zero_scalc()
		for pos in plan.sunflower_map:
			moveto(pos[0], pos[1])
			sunflower.action_sunflower()

		## Grass and Tree Phase
		change_hat(Hats.Straw_Hat)
		for pos in plan.grass_and_tree_map:
			moveto(pos[0], pos[1])
			grass.action_grass()
			tree.action_tree()

		## Carrot Phase
		change_hat(Hats.Carrot_Hat)
		for pos in plan.carrot_map:
			moveto(pos[0], pos[1])
			carrot.action_carrot()

		## Pumpkin Phase
		change_hat(Hats.Pumpkin_Hat)
		pumpkin.action_pumpkin()
			