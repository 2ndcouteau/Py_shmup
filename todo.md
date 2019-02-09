
Todo:
	Enemies:
		Manage position to avoid collisions at creation
		generate salve
		shoot in player direction
			diff enemy position and player position

	Shoot class
		generate salve
		shoot in multiple direction

	Print Informations
		score
		weapon
		hp
		lifes
		time

	Weapon
		basic
		double
		triple
		targeted
		Bomb

	Loot
		weapon
		life
		hp+
		speed boost

	MENU
		Manage event
			Start Game
			Restart Game
			Options ?
			Quit Game

	LEVEL
		Level script management

DONE:
	Clean all the Code
		Oject style organisation

	GAME
		Display background
			postion
			scale
		Display player
			position
				center bottom
			scale
		Manage Input:
			manage multiple inputs
			manage inputs in differentes modes
		Manage game frequency
		Manage Collide with border

		Interuption Management (Futur Menu)
			Pause
			Die Management
			Restart Game Management
				reinitialization fct() for player, background

	PLAYER
		Class PLAYER
		move()
		shoot()
		Collide enemies management
		Shoot frequency management

	ENEMIES
		Class Enemy
		Update()
			move()
			delete(), if go too out the window
		Manage x position at the creation to stay in the window
		Need to generate regulary
			manage number
			manage frequency
		Pseudo random spawn frequency
		Pseudo random shoot frequency

	SHOOT
		generate shoot item
			type=ALLIES/ENNEMY
			speed
			Direction
			Position from shooter
		collide management (ALLIES and ENEMIES)
