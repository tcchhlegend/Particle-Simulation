class CollisionManager:
    @staticmethod
    def collide(particles: list, x_max, y_max):
        n = len(particles)
        for i in range(n):
            particles[i].make_collide_wall(x_max, y_max)
        for i in range(n):
            for j in range(i):
                if particles[i].is_collide(particles[j]):
                    particles[i].make_collide(particles[j])
