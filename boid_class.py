import numpy as np
import numpy.random as rand

class Boid:

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def __init__(self):

    self.position_ary = (rand.random(2)-0.5)*10
    self.velocity_ary = (rand.random(2)-0.5)
    self.acceleration_ary = (rand.random(2)-0.5)
    self.max_velocity_float = 0.5
    self.max_acceleration_float = 1.0

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def get_position(self):

    return self.position_ary

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def get_velocity(self):

    return self.velocity_ary

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def get_acceleration(self):  

    return self.acceleration_ary

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def boids_rules(self, boid_set_):

    alignment_weight_float = 0.50
    cohesion_weight_float = 0.99
    separation_weight_float = 0.75

    max_interaction_radius_float = 2.5
    number_interactions_int = 0
    
    final_alignment_ary = np.zeros(2)
    final_cohesion_ary = np.zeros(2)
    final_separation_ary =  np.zeros(2)
    final_interaction_ary = np.zeros(2)

    for boid in boid_set_:

      distance_float = np.sqrt( np.sum( (self.position_ary[:]-boid.get_position()[:])**2 ) )

      if( boid != self and distance_float < max_interaction_radius_float ):

        final_alignment_ary += boid.get_velocity()

        final_cohesion_ary += boid.get_position()

        aux_distance_ary = self.position_ary - boid.get_position()
        final_separation_ary += aux_distance_ary/(distance_float*distance_float)

        number_interactions_int += 1

    if( number_interactions_int > 0 ):

      final_alignment_ary /= number_interactions_int
      final_alignment_ary = self.max_velocity_float*final_alignment_ary/np.linalg.norm(final_alignment_ary)
      final_alignment_ary -= self.velocity_ary
      final_alignment_ary = self.max_acceleration_float*final_alignment_ary/np.linalg.norm(final_alignment_ary)

      final_cohesion_ary /= number_interactions_int
      final_cohesion_ary -= self.position_ary
      final_cohesion_ary -= self.velocity_ary

      final_separation_ary /= number_interactions_int
      final_separation_ary = self.max_velocity_float*final_separation_ary/np.linalg.norm(final_separation_ary)
      final_separation_ary -= self.velocity_ary
      final_separation_ary = self.max_acceleration_float*final_separation_ary/np.linalg.norm(final_separation_ary)

      final_interaction_ary += alignment_weight_float*final_alignment_ary 
      final_interaction_ary += cohesion_weight_float*final_cohesion_ary 
      final_interaction_ary += separation_weight_float*final_separation_ary

    return final_interaction_ary
        
# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def boundary_condition( self, lattice_size_int_ ):

    pigsty_size_int_ = lattice_size_int_

    if(self.position_ary[0]>pigsty_size_int_):

      self.position_ary[0] = pigsty_size_int_ - self.position_ary[0]

    elif(self.position_ary[0]<0):

      self.position_ary[0] = pigsty_size_int_ + self.position_ary[0]

    if(self.position_ary[1]>pigsty_size_int_):

      self.position_ary[1] = pigsty_size_int_ - self.position_ary[1]

    elif(self.position_ary[1]<0):

      self.position_ary[1] = pigsty_size_int_ + self.position_ary[1]  

# # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

  def update(self, lattice_size_int_, boids_rules_ary_=np.zeros(2) ):

    self.boundary_condition( lattice_size_int_ )

    self.acceleration_ary += self.acceleration_ary + boids_rules_ary_
    # self.acceleration_ary *= self.max_acceleration_float

    # Explicit Euler 

    time_step_float = 0.1

    self.velocity_ary += self.acceleration_ary*time_step_float
    self.velocity_ary = self.max_velocity_float*(self.velocity_ary/np.linalg.norm(self.velocity_ary))
    self.position_ary += self.velocity_ary*time_step_float

    # Reset No-Memory Dynamics

    self.acceleration_ary = np.zeros(2)  