
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

	SOUND:
		Progression bar for level selection options
		sound UI
OK)			move/cursor
OK)			Launch Game
OK)			select
OK)			OFF
OK)			ON
OK)			return
			bad input

3)		Create Sound Class
			init sound in
			access to them


	Player
		animation invulnerability

	Explosion
		Player
			no explosion animation but visual bell
			special sound


2) Change Enemies color

	Print Informations
		weapon

	Enemies
		generate spawn salve formation
			duo
			triple
			line
			delta formation
			etc...

	Shoot class
		generate salve

	Weapon
		targeted
		Bomb

	Loot

	MENU

	LEVEL
		Level script management

		Can win more "combo" point in function of the Y position of the player


<!--
################################################################################
################################################################################
################################################################################
-->

DONE:

	Clean all the Code
		Object style organization
		Create multiple files structures

	GAME
		Display background
			position
			scale
		Display player
			position
				center bottom
			scale
		Manage Input:
			manage multiple inputs
			manage inputs in different modes
		Manage game frequency
		Manage Collide with border

		Interruption Management (Future Menu)
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
	Zoom the current text position
		Main menu
			Start
			Options
			Quit
		Level menu
			Resume
			Restart
			Options
			Main menu
		Death_menu
			Remaining Lives
			Resume
			Restart
			Options
			Main menu
		End_game_menu
			Score
			Time
			Options
			Main menu
		Option Main Menu


	Change text for selectable options
		for Music / Sfx / Auto_shoot :
			On / Off

	EVENT
		Manage die
			manage life, hp, score and time
			remove current shots

		Event Management in Menu
			in level menu
				Resume level
				Restart Level
				Options
				Go to Main menu
			in main menu
				Start Game
				Restart Game
				Options ?
				Quit Game
			in Death menu
				Remaining lives
				continue
				restart_game
				options_level
				main menu

	COLLIDE
		Manage Perfect mask hitbox for all collide


	PLAYER
		Class PLAYER
		move()
		shoot()
		Collide enemies management
		Shoot frequency management
		Invulnerability for seconds after took a shoot
		Auto_shoot
		Movement animations


	ENEMIES
		Class Enemy
		Update()
			move()
			delete(), if go too out the window
		Manage x position at the creation to stay in the window
		Need to generate regularly
			manage number
			manage frequency
		Pseudo random spawn frequency
		Pseudo random shoot frequency
		Shoot in multiple direction
		Manage position to avoid collisions at creation

	WEAPONS
		Simple
		Double
		Triple

	ITEMS/LOOT
		ADD items
			Icon UI
				Lives counter
				Lives
				Weapons Up
				Hp
				Invulnerability
				slow motion time
		Create Class Item
			init()
			update()
		Manage interactivity with the player
			Collide
			Effects


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

	SOUND
		Choose and implement sounds:
			shots
			explosions
			music
		Manage activation of sound in options
			music
			sfx (shots and menu sounds)

	EXPLOSION
		animation
