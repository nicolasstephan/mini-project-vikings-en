import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    
    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []
 
    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)

        result = randomSaxon.receiveDamage(randomViking.strength)

        if randomSaxon.health <= 0:
            self.saxonArmy.remove(randomSaxon)
        return result


        # What about "Saxon not attacking back"?
    
    def saxonAttack(self):
        # your code here
        randomSaxon = random.choice(self.saxonArmy)
        randomViking = random.choice(self.vikingArmy)

        result = randomViking.receiveDamage(randomSaxon.strength)
        
        if randomViking.health <= 0:
            self.vikingArmy.remove(randomViking)
        return result

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"

        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass


