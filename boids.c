/* 
Author: Guilherme Contesini
Code: Boids (Cellular-Automaton for simulating bird flocking or fish schooling)
ref: https://en.wikipedia.org/wiki/Boids
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_rng.h>

#define number_boids_int 10
#define max_time_int 1000

struct boids_stct{

  int uid_int;
  float postiion_ary[3];
  float velocity_ary[3];
  float aceleration_ary[3];

};

struct grid_stct{
// Square-Lattice

  boids_stct flock_ary[ number_boids_int ];

// Quad-Tree

  // boids_stct sq_lattive_ptr[ number_boids_int ];
// https://en.wikipedia.org/wiki/Quadtree

// Kd-Tree

// https://en.wikipedia.org/wiki/K-d_tree

};

// float aligment( struct boids_stct, struct grid_stct ){

// }

// float cohesion( struct boids_stct, struct grid_stct ){

// }

// float separation( struct boids_stct, struct grid_stct ){

// }

// float boundery_condition(struct boids_stct){

// }

void main(){

  int t_int = 0;
  int i_int = 0;
  int j_int = 0;
  int max_distance_int = 0;
  float max_aceleration_float = 0.0;
  float max_force_float = 0.0;

  grid_stct *grid_ptr=NULL;

  FILE *file_ptr = NULL;

  file_ptr = fopen("boids_data.dat","w");

  if(file_ptr==NULL){
    printf("File Error!");
    return 0;
  }
  grid_ptr = (struct boids_stct)malloc(number_boids_int*boids_stct);

  for( i_int=0; i_int<number_boids_int;i_int++ ){
   grid_stct 
  }

  for( t_int=0; t_int<max_time_int; t_int++ ){
    for( i_int=0; i_int<number_boids_int; i_int++ ){

    }
  }

  fclose(file_ptr);
  
  return 0;
}
