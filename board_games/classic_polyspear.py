import os

class Vector2i:
	x : int = 0
	y : int = 0
	def __init__(self, x_ : int, y_ : int):
		self.x = int(x_)
		self.y = int(y_)

	def __add__(self, value):
		return Vector2i(self.x + value.x, self.y + value.y)

	def __sub__(self, value):
		return Vector2i(self.x - value.x, self.y - value.y)
	def __str__(self):
		return "|" + str(self.x) + "_" + str(self.y) + "|"

	def __repr__(self):
		return "|" + str(self.x) + "_" + str(self.y) + "|"

	def __eq__(self, value):
		return self.x == value.x and self.y == value.y

#symbols:
EMPTY = 0
AXE = 1
SPEAR = 2
SHIELD = 3
BOW = 4
PUSH = 5


class Unit:
	unit_name_ids = ["elf1", "elf2", "elf3", "orc1", "orc2", "orc3"]

	ELF1 = [SPEAR, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
	ELF2 = [BOW, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
	ELF3 = [SPEAR, SHIELD, EMPTY, EMPTY, EMPTY, SHIELD]

	ORC1 = [AXE, AXE, EMPTY, EMPTY, EMPTY, AXE]
	ORC2 = [AXE, PUSH, EMPTY, PUSH, EMPTY, PUSH]
	ORC3 = [SPEAR, SPEAR, EMPTY, EMPTY, EMPTY, SPEAR]

	UNIT_TYPES = [ELF1, ELF2, ELF3, ORC1, ORC2, ORC3]

	unit_rotation : int
	coord : Vector2i = Vector2i(0, 0)
	controller : bool = True # elf or not elf -> orc
	symbols = []
	unit_name = ""
	def __init__(self, race : bool, symbol_data_idx):
		self.controller = race
		self.symbols = Unit.UNIT_TYPES[symbol_data_idx]
		self.unit_name = Unit.unit_name_ids[symbol_data_idx]

	def __repr__(self):
		return self.unit_name

	def can_defend(self, side : int) -> bool:
		return self.get_symbol(side) == SHIELD


	def get_symbol(self, side : int) -> int:
		return self.symbols[(side - self.unit_rotation) % 6]

	def rotate(self, value):
		self.unit_rotation = value


class Grid:
	SENTINEL = 0
	DEFAULT = 1
	ATTACKER_TILE = 2
	DEFENDER_TILE = 3

	unit_grid : list[list[Unit]] = []
	
	def get_unit_grid(self, x, y):
		if x < len(self.unit_grid) and y < len(self.unit_grid[x]):
			return self.unit_grid[x][y]
		return None
	
	grid_width : int = 5
	grid_height : int = 5
	border_size : int = 1

	hex_grid : list[list[int]] = [
					[0, 0, 0, 0, 2],
					[0, 0, 2, 2, 1],
					[2, 2, 1, 1, 1],
					[1, 1, 1, 1, 1],
					[1, 1, 1, 3, 3],
					[1, 3, 3, 0, 0],
					[3, 0, 0, 0, 0]]

	current_spawn : int = 0

	DIRECTIONS = [
		Vector2i(-1, 0),  # 0 LEFT
		Vector2i(0, -1),  # 1 TOP-LEFT
		Vector2i(1, -1),  # 2 TOP-RIGHT
		Vector2i(1, 0),   # 3 RIGHT
		Vector2i(0, 1),   # 4 BOTTOM-RIGHT
		Vector2i(-1, 1)]  # 5 BOTTOM-LEFT

	def get_tile_type(self, coord : Vector2i) -> int:
		if coord.x < len(self.hex_grid) and coord.y < len(self.hex_grid[coord.x]):
			return self.hex_grid[coord.x][coord.y]
		return 0



	def get_unit(self, coord : Vector2i) -> Unit:
		return self.get_unit_grid(coord.x, coord.y)


	def change_unit_position(self, unit : Unit, coord : Vector2i) -> None:
		self.unit_grid[unit.coord.x][unit.coord.y] = None  # clean your previous location
		self.unit_grid[coord.x][coord.y] = unit  # unit_grid Update
		unit.coord = coord  # update Unit Index


	def remove_unit(self, unit) -> None:
		coord : Vector2i = unit.coord
		self.unit_grid[coord.x][coord.y] = None # Remove unit from gameplay grid


	#region Coordinates tools
	def adjacent_units(self, base_coord : Vector2i) -> list[Unit]:
		# Returns 6 elements list, elements can be None
		units : list[Unit] = []
		for side in range(6):
			coord = self.adjacent_cord(base_coord, side)
			Neighbour = self.get_unit_grid(coord.x, coord.y)
			#if (Neighbour != None)
			units.append(Neighbour)
		return units


	def get_shot_target(self, start_coord : Vector2i, side : int):
		while self.get_tile_type(start_coord) != Grid.SENTINEL:
			start_coord += self.DIRECTIONS[side]
			target : Unit = self.get_unit_grid(start_coord.x, start_coord.y)
			if target is not None:
				return target
		return None


	def get_distant_unit(self, start_coord : Vector2i, side : int, distance : int) -> Unit:
		for _ in range(distance):
			start_coord += Grid.DIRECTIONS[side]

		return self.get_unit_grid(start_coord.x, start_coord.y)


	def get_distant_tile_type(self, start_coord : Vector2i, side : int, distance : int) -> int:
		for _ in range(distance):
			start_coord += Grid.DIRECTIONS[side]
		return self.get_tile_type(start_coord)

	@staticmethod
	def GetDistantCord(start_coord : Vector2i, side : int, distance : int) -> Vector2i:
		result_coord = start_coord
		for _ in range(distance):
			result_coord += Grid.DIRECTIONS[side]
		return result_coord


	@staticmethod
	def IsAdjacent(Cord1 : Vector2i, Cord2 : Vector2i) -> bool:
		return (Cord2 - Cord1) in Grid.DIRECTIONS


	@staticmethod
	def AdjacentSide(Cord1 : Vector2i, Cord2 : Vector2i) -> int:
		"""
		Return shared side between Cord1 and Cord2, if the Cords are adjacent
		@param Cord1
		@param Cord2
		@return int32 side
		@note -1 is return, when Cord1 and Cord2 don't have shared side
		"""
		if (Cord2 - Cord1) in Grid.DIRECTIONS:
			return Grid.DIRECTIONS.index(Cord2 - Cord1)
		return -1

	@staticmethod
	def adjacent_cord(base_coord : Vector2i, side : int) -> Vector2i:
		"""
		Return coord adjacent to BaseCord at given side

		@param base_coord
		@param side {0, 1, ..., 5}
		@return Vector2i coord adjacent to base_coord
		"""
		return base_coord + Grid.DIRECTIONS[side]

	#endregion


	#region GenerateGrid

	def adjust_grid_size(self) -> None:
		# sentinels appear on both sides
		self.grid_width += (self.border_size * 2)
		self.grid_height += (self.border_size * 2)
		self.grid_width += int(self.grid_height / 2) # adjustment for Axial grid system







	#endregion GenerateGrid




class BattleManager:
	EMPTY = 0
	AXE = 1
	SPEAR = 2
	SHIELD = 3
	BOW = 4
	PUSH = 5

	GRID : Grid

	#region BM Variables

	ATTACKER = 0
	DEFENDER = 1



	# end of the battle verification
	attacker_units = []
	defender_units = []

	current_player : int = ATTACKER
	selected_unit : Unit = Unit(True, 0)

	units_left_to_be_summoned : int

	#endregion

	#region Tools
	def switch_player_turn(self):
		if self.current_player == self.ATTACKER:
			self.current_player = self.DEFENDER
		else:
			self.current_player = self.ATTACKER

	def is_legal_move(self, coord : Vector2i) -> int:
		"""
		Function checks 2 things:
		* 1 target coord is a Neighbour of a selected_unit
		* 2 if selected_unit doesn't have push symbol on it's front (none currently have it yet)
		*	 target coord doesn't contatin an Enemy Unit with a SHIELD pointing at our selected_unit
		*
		* @param coord
		* @param result_side
		* @return True if selected Unit can move on a given coord
		"""
		# 1
		result_side = self.GRID.AdjacentSide(self.selected_unit.coord, coord)
		if result_side is None:
			return -1
		# 2
		enemy_unit = self.GRID.get_unit(coord)
		if enemy_unit is None:  # Is there a Unit in this spot?
			return result_side

		if self.selected_unit.symbols[0] == SHIELD:
			return -1 # selected_unit can't deal with enemy_unit
		elif self.selected_unit.symbols[0] == PUSH:
				return result_side # selected_unit ignores enemy_unit SHIELD

		# Does enemy_unit has a SHIELD?
		if enemy_unit.get_symbol(result_side + 3) == SHIELD:
			return -1
		return result_side

	def move_unit(self, unit : Unit, end_cord : Vector2i, side : int) -> None:
		# Move General function
		"""
		* Move this unit to end_cord
		*
		* @param end_cord Position at which unit will be placed
		"""
		unit.rotate(side) # 1
		#TODO: if SHIELDs: # maybe check for every unit
		if self.enemy_damage(unit):
			self.kill_unit(unit)
			return
		self.unit_action(unit)

		self.GRID.change_unit_position(unit, end_cord)
		if self.enemy_damage(unit):
			self.kill_unit(unit)
			return

		self.unit_action(unit)


	def enemy_damage(self, target : Unit) -> bool:
		# Returns True is Enemy spear can kill the target
		units = self.GRID.adjacent_units(target.coord)
		for side in range(6):
			if (units[side] != None and units[side].controller != target.controller):
				if (target.get_symbol(side) == SHIELD):  # Do we have a SHIELD?
					continue
				if (units[side].get_symbol(side + 3) == SPEAR): # Does enemy has a spear?
					return True
		return False

	def kill_unit(self, target) -> None:
		if (target.controller == BattleManager.DEFENDER):
			self.defender_units.remove(target)
		else:
			self.attacker_units.remove(target)

		self.GRID.remove_unit(target)
		if len(self.defender_units) == 0:
			print("Attacker won")
		elif len(self.attacker_units) == 0:
			print("Defender won")
		
	def unit_action(self, unit) -> None:
		units = self.GRID.adjacent_units(unit.coord)
		for side in range(6):
			unit_weapon = unit.get_symbol(side)
			if unit_weapon == SHIELD or unit_weapon == EMPTY:
					continue # We don't have a weapon
			elif unit_weapon == BOW:
				target = self.GRID.get_shot_target(unit.coord, side)
				if target is None:
					continue
				if target.controller == unit.controller:
					continue
				if (target.get_symbol(side + 3) != SHIELD):  # Does Enemy has a SHIELD?
					self.kill_unit(target)
				continue

				
			if units[side] is None or units[side].controller == unit.controller:
				# no one to hit
				continue
			enemy_unit = units[side]
			if unit_weapon == PUSH:
				# PUSH LOGIC
				TargetTileType = self.GRID.get_distant_tile_type(unit.coord, side, 2)
				if TargetTileType == Grid.SENTINEL:  # Pushing outside the map
					# Kill
					self.kill_unit(enemy_unit)
					continue
				target = self.GRID.get_distant_unit(unit.coord, side, 2)
				if target != None: # Spot isn't empty
					self.kill_unit(enemy_unit)
					continue
				self.GRID.change_unit_position(enemy_unit, self.GRID.GetDistantCord(unit.coord, side, 2))
				if self.enemy_damage(enemy_unit): # Simple push	
					self.kill_unit(enemy_unit)
				continue
			
			# Rotation is based on where the unit is pointing toward
			if enemy_unit.get_symbol(side + 3) != SHIELD:# Does Enemy has a SHIELD?
				self.kill_unit(units[side])
			
					
	def select_unit(self, coord : Vector2i) -> bool:
		"""
		* Select friendly Unit on a given coord
		*
		* @return True if unit has been selected in this operation
		"""
		NewSelection : Unit = self.GRID.get_unit(coord)
		if NewSelection != None and NewSelection.controller == self.current_player:
			self.selected_unit = NewSelection
			print("You have selected a Unit")
			return True
		return False
	#endregion Tools


	#region Main Functions

	def input_listener(self, coord : Vector2i) -> None:
		#print(coord)
		if self.select_unit(coord) or self.selected_unit is None:
			return # selected a new unit or wrong input which didn't select any ally unit
		if self.units_left_to_be_summoned > 0: # Summon phase
			"""
			* Units are placed by the players in subsequent order on their chosen "Starting Locations"
			* inside the area of the gameplay board.
			"""
			self.summon_unit(coord)
		else:  # gameplay phase
			self.gameplay(coord)
		self.selected_unit = None  # IMPORTANT


	def gameplay(self, coord : Vector2i) -> None:
		#print("gameplay is working")
		side = self.is_legal_move(coord) # Gets Updated with is_legal_move()
		if side != -1: # spot is empty + we aren't hitting a SHIELD
			# 1 rotate
			# 2 Check for Spear
			# 3 Actions
			# 4 Move
			# 5 Check for Spear
			# 6 Actions
			self.move_unit(self.selected_unit, coord, side)
			#print(FString::Printf(TEXT("DIRECTION_%d"), side))
			#testkill_unit(coord)

			#self.GRID.change_unit_position(selected_unit, coord)
			#.rotateUnit(selected_unit, side)
			self.switch_player_turn()


	def summon_unit(self, coord : Vector2i) -> None:
		"""
		* Summon currently selected unit to a gameplay Board
		*
		*
		* @param coord cordinate, on which Unit will be summoned
		"""
		
		# check if unit is already summoned
		selected_unit_tile_type : int = self.GRID.get_tile_type(self.selected_unit.coord)
		if selected_unit_tile_type != Grid.SENTINEL:
			print("This Unit has been already summoned")
			return
		
		selected_hex_type = self.GRID.get_tile_type(coord)
		bSelectedcurrent_playerSpawn = \
			(selected_hex_type == Grid.ATTACKER_TILE and self.current_player == BattleManager.ATTACKER) or \
			(selected_hex_type == Grid.DEFENDER_TILE and self.current_player == BattleManager.DEFENDER)
		if not bSelectedcurrent_playerSpawn:
			print("That's a wrong summon location")  # TODO: Don't reset selected_unit
			return
		print("You summoned a Unit")

		self.GRID.change_unit_position(self.selected_unit, coord)
		if self.current_player == BattleManager.ATTACKER:
			self.attacker_units.append(self.selected_unit)
			self.selected_unit.unit_rotation = 3
		else:
			self.defender_units.append(self.selected_unit)
			self.selected_unit.unit_rotation = 0
		self.switch_player_turn()
		self.units_left_to_be_summoned -= 1
	#endregion

	#region GameSetup
	def spawn_units(self) -> None:
		"""
		
		"""
		self.units_left_to_be_summoned = 6  # Flag that manages the state of the game

	def setup_game(self):
		self.GRID = Grid()
		self.current_player = BattleManager.ATTACKER

		self.GRID.unit_grid = []
		for i in range(7):
			self.GRID.unit_grid.append([])
			for j in range(5):
				self.GRID.unit_grid[i].append(None)
		self.spawn_units()


#region Replay translator

def translate_position_to_simple_form(unit):
	result = 0
	match unit.coord.y:
		case 0:
			result = unit.coord.x - 2
		case 1:
				result = 6 + unit.coord.x - 2
		case 2:
			result = 10 + unit.coord.x - 1
		case 3:
			result = 15 + unit.coord.x - 2
		case 4:
			result = 19 + unit.coord.x
	return result + 2  # 0 is for dead unit, 1 is for unsummoned unit

def deep_test_map_save(unit_grid : list[list[Unit]], is_summon_phase : bool = False):
	unit_name_ids = ["elf1", "elf2", "elf3", "orc1", "orc2", "orc3"]
	result = [0, 0,  0, 0,  0, 0,
			  0, 0,  0, 0,  0, 0]
	if is_summon_phase:
		result = [1, 0, 1, 0, 1, 0,
				  1, 0, 1, 0, 1, 0]
	for row in unit_grid:
		for unit in row:
			if unit is None:
				continue
			unit_id = unit_name_ids.index(unit.unit_name) * 2
			result[unit_id] = translate_position_to_simple_form(unit)
			result[unit_id + 1] = unit.unit_rotation

	return result

def main_translator(file_name : str, replay_idx : int = 1):
	replay_file : str = open(file_name, "r")
	replay_text = replay_file.read()
	replay_text = replay_text.split("script = ExtResource(") #
	#print(replay_text[2])

	# first part is file start, last is the move generated by the end of the match

	# first 6 moves in classic are always unit placements moves ("summons")

	#get unit ID's (randomized for every replay)
	
	unit_name_ids = ["elf1", "elf2", "elf3", "orc1", "orc2", "orc3"]
	unit_id_names = {}


	unit_id_text = replay_text[0].split("\n")




	for unit in unit_id_text[2:11]:
		#print(unit[59:63])
		if unit[59:63] == "Unit":
			unit_id_names[unit[88:95]] = unit[73:77]
			#unit_id_names[unit[88]] = unit[73:77]

	print(unit_id_names)

	BM = BattleManager()
	BM.setup_game()

	replay_output_for_ai : str = ""
	if replay_idx == 2:
		print("xd")

	for i, summon_move in enumerate(replay_text[1:7]):
		summon_move_split = summon_move.split("\n")
		#unit_id
		target_tile_coord = Vector2i(summon_move_split[4][-5], summon_move_split[4][-2])
		#print(unit_id)
		#unit_name = unit_id_names[summon_move_split[2][-3]]
		unit_key_name = summon_move_split[2][27:-2]
		unit_name = unit_id_names[unit_key_name]
		print(unit_name, "->", target_tile_coord)

		BM.selected_unit = Unit(i % 2, unit_name_ids.index(unit_name))
		BM.input_listener(target_tile_coord)

		game_state = deep_test_map_save(BM.GRID.unit_grid, True)
		replay_output_for_ai += str(game_state) + "\n"


	for i, action_move in enumerate(replay_text[7:-1]):
		action_move_split = action_move.split("\n")
		#unit_id
		move_source_coord = Vector2i(action_move_split[2][-5], action_move_split[2][-2])
		target_tile_coord = Vector2i(action_move_split[3][-5], action_move_split[3][-2])
		#print(unit_id)

		if False:
			print("---------------------")
			for row_id, row in enumerate(BM.GRID.unit_grid):
				print(row_id, "|", end="")
				for tile in row:
					if tile is None:
						print("    |", end="")
					else:
						print("", tile, "|", sep="", end="")
				print("")
			print("---------------------")

		print(move_source_coord, "->", target_tile_coord)

		BM.input_listener(move_source_coord)
		if i == 8: # 7
			print("check")
		BM.input_listener(target_tile_coord)
		game_state = deep_test_map_save(BM.GRID.unit_grid)
		print(game_state)
		replay_output_for_ai += str(game_state) + "\n"


	print("---------------------")
	for row_id, row in enumerate(BM.GRID.unit_grid):
		print(row_id, "|", end="")
		for tile in row:
			if tile is None:
				print("    |", end="")
			else:
				print("", tile, "|", sep="", end="")
		print("")
	print("---------------------")
	
	print("end of replay")

	finish_replay_for_ai(replay_output_for_ai, game_state, replay_idx)


def finish_replay_for_ai(replay_text : str, last_state : list[int], replay_idx : int) -> None:
	# used to calculate how big of an advantage winner got (this point system is also used during tournament play)
	UNIT_POINTS = [2, 3, 4]
	attacker_points = 0
	defender_points = 0
	unit_idx = -1
	for unit_from_table_idx in range(0, len(last_state), 2):
		unit_idx += 1
		if last_state[unit_from_table_idx] > 0:
			if unit_idx < 3:
				attacker_points += UNIT_POINTS[unit_idx]
			else:
				defender_points += UNIT_POINTS[unit_idx % 3]
	if attacker_points * defender_points != 0:  # only one of the team should have points left
		print("ERROR: replay doesn't contain the game end")
		return
	winner = 0  # Attacker won
	if attacker_points < defender_points:
		winner = 1

	title : str = str(winner) + "_" + str(attacker_points + defender_points) + "_" + str(replay_idx)
	replay_text = "\n".join([title, replay_text])

	# saving file
	new_replay_file = open(title + ".txt", "w")
	new_replay_file.write(replay_text)






#endregion








if __name__ == "__main__":
	folder_path = "C:/Users/user_name/AppData/Roaming/Godot/app_userdata/Polyspear/replays"
	replay_name = "2024-12-09T22_31_07-deathguard12_Wiolarz.tres"
	replay_name = "2024-12-09T22_29_21-Wiolarz_deathguard12.tres"

	folder_path += "/turniej_V"

	#relative_path_to_file = os.path.join(folder_path, replay_name)
	#absolute_path_to_file = os.path.realpath(relative_path_to_file)

	absolute_folder_path = os.path.realpath(os.path.join(folder_path))
	#main_translator(absolute_path_to_file)
	replay_idx = 0
	for replay in os.listdir(absolute_folder_path):
		replay_idx += 1
		if replay_idx == 3:
			break

		relative_path_to_file = os.path.join(folder_path, replay)
		absolute_path_to_file = os.path.realpath(relative_path_to_file)
		main_translator(absolute_path_to_file, replay_idx)
	