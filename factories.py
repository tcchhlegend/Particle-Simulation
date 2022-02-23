import numpy as np
from things import *

RED = (255, 0, 0)

class ParticleFactory:
    @staticmethod
    def random_circle(x_min, x_max, y_min, y_max, mu, sigma,
               color=RED, radius=10, mass=1, force=0):
        """
            create a circle with uniform distribution of position
            and gaussian distribution of velocity
        """
        x = np.random.uniform(x_min, x_max)
        y = np.random.uniform(y_min, y_max)
        v = np.random.multivariate_normal(mu, sigma)
        return Circle([x, y], v, color, radius, mass, force)
