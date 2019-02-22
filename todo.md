
TODO:

	Format Render, Binary
		Freeze Format distribution		
		-- check pyinstaller (Osx/linux)
		-- py2app(Osx)
		-- bbfreeze (linux) -- Nop (Only python 2.X)

~)	Sound
		Add Music
OK			In Menu
OK			In Game
		Add SFX
			menu
				move selection
				selection validation
				selection invalid
			game
OK				shoot player
OK				shoot enemies
OK				explosion enemies
				loose game
				(
				win game (define some objectives before PLZ)
				special dodge movement
				)

~~	Clean Event class
		use dict/hash table function for manage input

	Layout
		enemies
			color by type

	Collide
		Manage hitbox

	Explosion
		Player
			no explosion animation but visual bell
			special sound


3)	Print Informations
		weapon
	make back-end for all informations

	Enemies
		generate spwan salve formation
			duo
			triple
			line
			delta formation
			etc...

	EVENT
4)		Manage die
			manage life, hp, score and time

	Player
2)		invulnerability for seconds after took a shoot


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
		slow motion time

3)	MENU

		Manage event with layout selection
			in level menu
			in main menu
				Start Game
				Restart Game
				Options ?
				Quit Game
		Event Animations
			Change text for selectable options
				On / Off
			Progression bar for level selection options
				Music / Sfx

	LEVEL
		Level script management

		Can win more "combo" point in function of the Y position of the player

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

		Menu Management
			Main Menu
			Level Menu
			Game
			--> Can move from one to another

		Clean Background and Text Classes

	LAYOUT
		Create Class
		Create method draw_sprites
		Create method scroll_background

		Print informations
			score
			hp
			life
			time



	TEXT
		Create Class
		Clean and reduce Text method for menu in one class

	MENU
		Main menu
			Start
			Options
			Quit
		Level menu
			Resume
			Restart
			Options
			Main menu
		Zoom the current text position


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


	EXPLOSION
		animation
