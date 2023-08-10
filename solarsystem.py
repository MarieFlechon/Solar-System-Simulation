import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Paramètres de la simulation
G = 6.67430e-11  # Constante gravitationnelle
dt = 60 * 60 * 24  # Pas de temps (1 jour en secondes)
num_steps = 365  # Nombre d'étapes (1 an)

# Classe représentant un corps céleste
class CelestialBody:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)

# Initialisation des corps célestes (ex. : Soleil et Terre)
sun = CelestialBody(mass=1.989e30, position=[0, 0], velocity=[0, 0])
earth = CelestialBody(mass=5.972e24, position=[1.496e11, 0], velocity=[0, 29783])
mercury = CelestialBody(mass=3.3011e23, position=[-4.6e10, 0], velocity=[0, -47400])
venus = CelestialBody(mass=4.8675e24, position=[-1.07477e11, 0], velocity=[0, -35020])
mars = CelestialBody(mass=6.4171e23, position=[2.0662e11, 0], velocity=[0, 24007])
jupiter = CelestialBody(mass=1.8982e27, position=[7.4052e11, 0], velocity=[0, 13070])
saturn = CelestialBody(mass=5.6834e26, position=[1.35255e12, 0], velocity=[0, 9690])
uranus = CelestialBody(mass=8.6810e25, position=[2.74130e12, 0], velocity=[0, 6810])
neptune = CelestialBody(mass=1.02413e26, position=[4.44445e12, 0], velocity=[0, 5430])

# Liste de corps célestes
celestial_bodies = [sun, earth, mercury, venus, mars, jupiter, saturn, uranus, neptune]

# Couleurs correspondant à chaque planète
planet_colors = {
    "Soleil": "yellow",
    "Terre": "blue",
    "Mercure": "gray",
    "Vénus": "orange",
    "Mars": "red",
    "Jupiter": "brown",
    "Saturne": "gold",
    "Uranus": "cyan",
    "Neptune": "blue"
}

# Liste des noms de planètes
planet_names = list(planet_colors.keys())

# Fonction pour calculer les forces entre les corps
def calculate_forces(bodies):
    forces = np.zeros((len(bodies), 2))
    for i, body in enumerate(bodies):
        for j, other_body in enumerate(bodies):
            if i != j:
                displacement = other_body.position - body.position
                distance = np.linalg.norm(displacement)
                force_magnitude = (G * body.mass * other_body.mass) / (distance ** 2)
                force = force_magnitude * (displacement / distance)
                forces[i] += force
    return forces

# Fonction pour mettre à jour les positions et les vitesses
def update_positions_and_velocities(bodies, dt):
    forces = calculate_forces(bodies)
    for i, body in enumerate(bodies):
        acceleration = forces[i] / body.mass
        body.velocity += acceleration * dt
        body.position += body.velocity * dt

# Animation
fig, ax = plt.subplots()

def animate(frame):
    update_positions_and_velocities(celestial_bodies, dt)
    x = [body.position[0] for body in celestial_bodies]
    y = [body.position[1] for body in celestial_bodies]
    sc.set_offsets(np.c_[x, y])

    for name, body in zip(planet_names, celestial_bodies):
        ax.annotate(name, (body.position[0], body.position[1]), color=planet_colors[name], fontsize=8, ha='center')

    return sc,

x = [body.position[0] for body in celestial_bodies]
y = [body.position[1] for body in celestial_bodies]
sc = ax.scatter(x, y)

ax.set_xlim(-3e12, 3e12)
ax.set_ylim(-3e12, 3e12)
ax.set_title("Simulation du Système Solaire")

ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=100, blit=True)

# Afficher une légende avec les couleurs et les noms des planètes
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=8, label=name) for name, color in planet_colors.items()]
ax.legend(handles=legend_handles, loc='upper left')

plt.show()
