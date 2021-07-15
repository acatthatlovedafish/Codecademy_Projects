# Act as a physics teacher providing students with functions that will help them calculate fundamental physical properties.

train_mass = float(input("Enter the weight of the train in kilogramms: "))
train_acceleration = float(input("Enter the acceleration of the train in m/h: "))
train_distance = float(input("Enter the distance in meters: "))
bomb_mass = float(input("Enter the mass of the bomb in kilogramms: "))

def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
    return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("\nThe GE train supplies " + str(train_force) + " Newtons of force.")

c = 3 * 10 ** 8
def get_energy(mass, c):
  return mass * (c ** 2)

bomb_energy = get_energy(bomb_mass, c)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration) * distance
  return force

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
