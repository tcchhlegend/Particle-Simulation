import pygame
import numpy as np
from numpy.linalg import norm

class Thing:
    def __init__(self, pos, color):
        self._pos = np.array(pos)
        self._color = color


class Particle(Thing):
    def __init__(self, pos, velocity, mass, force, color):
        super().__init__(pos, color)
        self._velocity = np.array(velocity)
        self._mass = mass
        self._force = force


class Circle(Particle):
    def __init__(self, pos, velocity, color, radius, mass=1, force=0):
        super().__init__(pos, velocity, mass, force, color)

        self._radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen,
                           self._color,
                           self._pos,
                           self._radius)

    def is_collide(self, other):
        distance_close_enough = distance(self._pos, other._pos) <= self._radius + other._radius
        normal_vec = other._pos - self._pos
        towards_each_other = np.dot(normal_vec, self._velocity) / norm(self._velocity) \
                             > np.dot(normal_vec, other._velocity) / norm(other._velocity)
        return distance_close_enough and towards_each_other

    def make_collide(self, other: Particle):
        """ 碰撞 """
        normal_vec = other._pos - self._pos
        normal_vec /= np.linalg.norm(normal_vec)
        new_v_self = self._velocity + (2 * self._mass * other._mass) / \
                     (self._mass ** 2 + self._mass * other._mass) * \
                     np.dot(normal_vec, other._velocity - self._velocity) \
                     * normal_vec
        new_v_othe = other._velocity + (2 * self._mass * other._mass) / \
                     (other._mass ** 2 + self._mass * other._mass) * \
                     np.dot(normal_vec, self._velocity - other._velocity) \
                     * normal_vec
        self._velocity = new_v_self
        other._velocity = new_v_othe

    def make_collide_wall(self, x_max, y_max):
        x, y = self._pos
        if x < self._radius and self._velocity[0] < 0:
            self._velocity[0] *= -1
            return
        if x > x_max - self._radius and self._velocity[0] > 0:
            self._velocity[0] *= -1
            return
        if y < self._radius and self._velocity[1] < 0:
            self._velocity[1] *= -1
            return
        if y > y_max - self._radius and self._velocity[1] > 0:
            self._velocity[1] *= -1
            return

    def update(self, dt):
        self._pos += dt * self._velocity
        self._velocity += dt * self._force / self._mass

    def update_force(self, force):
        self._force = force


def distance(x, y):
    return np.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
