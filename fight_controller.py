def fight_controller(attacker, target, attacktype):
    if attacktype == 'physical':
        target.stats["health"] -= attacker.stats["strength"]
        print(repr(attacker) + " attacked " + repr(target) + " with " +
              str(attacker.stats["strength"]) + " power ")
    if attacktype == 'magical':
        target.stats["health"] -= attacker.stats["magical"]
        print(repr(attacker) + " attacked " + repr(target) + " with " +
              str(attacker.stats["magical"]) + " power ")