# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Part 1


def greet(name, sentence='Hello, <name>!'):
    return sentence.replace('<name>', name)


print(greet('Henk'))
print(greet('Bob', "What's up, <name>!"))


# Part 2

def force(mass, body='earth'):
    body = body.lower()
    planets = {
        'earth': 9.8,
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }
    if body not in planets:
        return 'I don\'t know this planet! \nAre you an alien?'
    force = mass * planets[body]
    return round(force,2)


print(force(3))
print(force(15, 'MaRs'))
print(force(33, 'Andromia'))


# Part 3

def pull(m1, m2, d):  # m1/m2 in kg, d in meters
    g = 6.674 * 10**-11
    pull = g * ((m1 * m2) / (d**2))
    return pull


print(pull(800, 1500, 3))
print(pull(0.1, (5.972 * 10e24), (6.371 * 10e6)))
