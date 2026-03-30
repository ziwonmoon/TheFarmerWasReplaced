from basic_tools import moveto, hvst, action_wildcard



while True:
	clear()
	moveto(0, 0)
	action_wildcard(Entities.Grass)
	temp = get_companion()

	companion_route = []
	while True:
		companion_route.append(temp[1])
		moveto(temp[1][0], temp[1][1])
		action_wildcard(temp[0])
		temp = get_companion()

		if temp[1] in companion_route:
			print(1)
			break

	for pos in companion_route:
		moveto(pos[0], pos[1])
		hvst()