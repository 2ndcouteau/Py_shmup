
TODO:


	Layout
		enemies
			color by type

	2) Print Informations
		score
		weapon
		hp
		lifes
		time

	Enemies
		generate spwan salve formation
			duo
			triple
			line
			delta formation
			etc...

	Shoot class
		generate salve

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
		Create multiple files structures


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


	LAYOUT
		Create Class
		Create method draw_sprites
		Create method scroll_background


	TEXT
		Create Class


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
		Shoot in multiple direction
		Manage position to avoid collisions at creation


	SHOOT
		generate shoot item
			type=ALLIES/ENNEMY
			speed
			Direction
			Position from shooter
		collide management (ALLIES and ENEMIES)

		Shoot in player direction
			Manage angle

		Update sprites with new media
