print('Imported Pokemon')
import os
from Game.Pokestats import Get_Pokemon
from Game.Pokestats import Get_Attacks
Get_Pokemon()
Get_Attacks()

class New_Pokemon:
    def __init__(self, name, pokefile = 'Pokemon_txt', resistfile = 'Resistances_txt'):
        self._pokefile = pokefile
        self._name = name
        self.get_stats()
        self.check_resistance(resistfile)
    def get_stats(self):
        """ extracts the statistics of each pokemon type to add to the class """
        types = []
        data_list = []
        with open(self._pokefile, 'r') as data:
            for line in data:
                line = line.strip()
                line = line.split(',')
                line.remove(line[-1])
                if(line == None):
                        pass
                else:
                    for dat in line:
                        if(line[0] == self._name):
                            if(self._name in dat):
                                pass
                            else:
                                try:
                                    dat = int(dat)
                                    data_list.append(dat)
                                except ValueError:
                                    types.append(dat)
        self.define_stats(data_list, types)
    def define_stats(self, stats, types):
        """ sets the changing statistics of the pokemon """
        self._attack = stats[2]
        self._health = stats[1]
        self._max_health = stats[1]
        self._poketype = types
        self._level = 1
        self._xp = 0
        self._level_up_xp = 100
        self._defence = stats[3]
        self._speed_attack = stats[4]
        self._speed_defence = stats[5]
        self._speed = stats[6]
        self._evolve_level = 20
        # self._evolution = stats['higher']
    def get_attack(self):
        """ returns the attack power of the pokemon """
        return self._attack
    def get_name(self):
        """ returns the name of the pokemon in the class """
        return self._name
    def get_health(self):
        """ returns the current health[0] and maximum health of pokemon[1] of the pokemon """
        return [self._health, self._max_health]
    def get_type(self):
        """ returns the pokemons type """
        return self._poketype
    def show_type(self):
        """ Return pokemon types in string list place """
        i = 0
        for type in self._poketype:
            if(i == 0):
                reply = str(type)
            else:
                reply = reply +(', ' + str(type))
            i += 1
        return reply
    def get_resistances(self):
        """ returns the resistances and damage values of the pokemon """
        return self._resistances
    def get_level_up(self):
        """ Returns the amount of xp required for next level up"""
        return self._level_up_xp
    def get_level(self):
        """ returns the level of the pokemon """
        return self._level
    def get_xp(self):
        """Returns the current amount of xp"""
        return self._xp
    def check_resistance(self, resistance_chart):
        """ Reads the resistances file and isolates the relative strength and weaknesses of the pokemon """
        self._resistances = {}
        key = []
        with open(resistance_chart, 'r') as resistance:
            for line in resistance:
                line = line.strip().split(',')
                if(line[0] == 'key'):
                    for key_name in line:
                        if(key_name == 'key'):
                            pass
                        else:
                            key.append(key_name)
                else:
                    for typ in self._poketype:
                        i = 0
                        n = len(self._poketype)
                        if(typ == line[0]):
                            for resist_value in line:
                                if(typ == str(resist_value)):
                                    pass
                                else:
                                    try:
                                        dat = self._resistances[key[i]]
                                        self._resistances[key[i]] = (float(dat) + float(resist_value))/n
                                    except KeyError:
                                        self._resistances[key[i]] = resist_value
                                    i += 1 
    def relative_damage(self, types):
        """ processing the pokemon taking damage in a fight """
        i = 0
        n= 0
        final_resistance = 0
        resistances = []
        for typ in types:
            resistances.append(self.get_resistances()[typ])
            i += 1
        while(n <= (i-1)):
            final_resistance = (final_resistance + float(resistances[n]))/(n+1)
            n += 1
        return final_resistance
    def gain_xp(self, opponent_level):
        """ gains xp based on the level of the opponent beaten """
        gained_xp = int(opponent_level)*10
        self._xp = gained_xp + self._xp
        if(self._xp >= self._level_up_xp):
            self.level_up()
    def check_evolve(self):
        """ checks if the xp is high enough to evolve """
        if(self._level >= self._evolve_level):
            self.evolve()
    def level_up(self):
        """ levels up the pokemon """
        self._level = int(self._level + 1)
        self._xp = self._xp - self._level_up_xp
        self._level_up_xp = self._level_up_xp + (10*self._level)
        self.check_evolve()
    def evolve(self):
        """ evolves the pokemon to its evolution state """
        print('Evolve')
        return 'evolve'