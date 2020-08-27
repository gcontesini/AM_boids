########################################################################
# Name: Boids
# Author: Guilherme Contesini
# E-mail: gcontesini@gmail.com
# Date: 08 / 12 / 2016
# Purpose:
# 
# 
# 
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 

from boids_class_3d import *

def main():

  number_boids_int = 30
  lattice_size_int = 10
  total_time_int = 1e3
  time_step_float = 1e-1

  boid_rules_ary = np.zeros(2)

  data_file = open("boids_3d.dat","w")

  boid_set = set( "" )

  for i_int in np.arange( number_boids_int ):

    boid_set.add( Boid() )

  for t_int in np.arange( total_time_int ):

    for boid_boid in boid_set:

      boid_rules_ary = boid_boid.boids_rules( boid_set )
      boid_boid.update( lattice_size_int, boid_rules_ary )

      position_ary = boid_boid.get_position()  
      data_file.write( str(position_ary[0] ) + "\t" + str( position_ary[1] ) + "\t" + str( position_ary[2] )  + "\n" )

    data_file.write("\n\n")

  data_file.close()

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

if __name__ == '__main__':
  main()