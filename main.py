import pumpkin, carrot, sunflower, tree, grass

if __name__ == "__main__":
	clear()

	change_hat(Hats.Tree_Hat)
	do_a_flip()

	while True:
		pumpkin.zero_pcalc()
		sunflower.zero_scalc()
		for y in range(get_world_size()):
			for x in range(get_world_size()):
				# change to (not execute all the func, excute the func that I want)
				pumpkin.action_pumpkin()
				carrot.action_carrot()
				sunflower.action_sunflower()
				tree.action_tree()
				grass.action_grass()
				move(East)
			move(North)
	
		
		