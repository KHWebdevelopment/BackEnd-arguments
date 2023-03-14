# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# PART 1
def greet(name: str, greeting_template: str="Hello, <name>!") -> str:
    greeting = greeting_template.replace('<name>', name)
    return greeting
print(greet("Kato"))
print(greet("Kato", "What's up, <name>!"))

# PART 2
def force(mass, body="earth") -> float:
    gravity = {
        "sun" : 274,
        "jupiter" : 24.9,
        "neptune" : 11.2,
        "saturn" : 10.4,
        "earth" : 9.8,
        "uranus" : 8.9,
        "venus" : 8.9,
        "mars" : 3.7,
        "mercury" : 3.7,
        "moon" : 1.6,
        "pluto" : 0.6
    }
    return mass * gravity[body]
print(force(10,"sun"))

def pull(m1, m2, d):
    return (6.674 * 10 ** -11) * (m1 * m2) / d ** 2
print(pull(800, 1500, 3))


