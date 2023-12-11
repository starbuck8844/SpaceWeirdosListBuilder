WarbandTraits = {
'No Trait': '',
 'Cyborgs': 'All members of the Warband can purchase 1 additional piece of equipment.',
 'Fanatics': 'Roll Willpower with +1DT for all rolls except Psychic Powers.',
 'Living Weapons': 'Unarmed attacks do not have -1DT to Prowess rolls.',
 'Heavily Armed': 'All Ranged weapons cost 1 point less.',
 'Mutants': 'Speed, Claws & Teeth, Horrible Claws & Teeth, and Whip/Tail cost 1 less point.',
 'Soldiers': 'Grenades, Heavy Armor, and Medkits may be purchased for free. They still use a model’s equipment slots.',
 'Undead': 'A second staggered condition does not take models in thisWarband out of action.'
}

class Warband:
    def __init__(self, name, trait = 'No Trait'):
        self.name = name
        self.trait = trait
        self.trait_dropdown=WarbandTraits
        self.weirdos = []  # list.append(geeks(22, 33))
        # self._last_weirdo_key = 0

    # def add_weirdo(self, weirdo):
    #     self._last_weirdo_key += 1
    #     self.weirdos[self._last_weirdo_key] = weirdo
    #
    # def delete_weirdo(self, weirdo_key):
    #     if weirdo_key in self.weirdos:
    #         del self.weirdos[weirdo_key]
    #
    # def get_weirdo(self, weirdo_key):
    #     weirdo = self.weirdos.get(weirdo_key)
    #     if weirdo is None:
    #         return None
    #     return weirdo
    #
    # def get_weirdos(self):
    #     weirdos = []
    #     for weirdo_key, weirdo in self.weirdos.items():
    #         weirdos.append(weirdo)
    #     return weirdos


# class Equipment:
#     def __init__(self, name, e_type, notes, points):
#         self.name = name
#         self.e_type = e_type  # P=passive stat increase or A=item action
#         self.notes = notes
#         self.points = points


# class PsychicPower:
#     def __init__(self, name, p_type, effect, points):
#         self.name = name
#         self.p_type = p_type  # P=passive stat increase or A=item action
#         self.effect = effect
#         self.points = points


# class Weapon:
#     def __init__(self, name, weapon_type, actions, notes, points):
#         self.name = name
#         self.weapon_type = weapon_type
#         self.actions = actions
#         self.notes = notes
#         self.points = points


# class Attribute:
#     def __init__(self, name, level, points):
#         self.name = name
#         self.level = level  # either dice or number for speed
#         self.points = points

class Weirdo:
    # leader_trait_id, is_leader, ranged_weapon_id,melee_weapon_id,
    def __init__(self, weirdo_id, name, total_points, speed_id, defense_id, firepower_id, prowess_id, willpower_id, warband_id): 
        self.warband_id = warband_id
        self.name = name
        self.weirdo_id = weirdo_id

        self.willpower_id = willpower_id
        self.prowess_id = prowess_id
        self.firepower_id = firepower_id
        self.defense_id = defense_id
        self.speed_id = speed_id


        self.total_points = total_points

        # self.melee_weapon_id = melee_weapon_id
        # self.ranged_weapon_id = ranged_weapon_id
        
        # self.leader_trait_id = leader_trait_id
        # self.is_leader = is_leader    
        