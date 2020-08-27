reset

max_time_int = 1000
number_boids_int = 10

set terminal gif animate delay 2.5

# unset tics
unset key

set grid
set xrange[0:10]
set yrange[0:10]
set zrange[0:10]

set output "flocking_boids_3d.gif"

boids_data_file = "boids_3d.dat"

do for [time_int=0:max_time_int] {

  splot boids_data_file index time_int using 1:2:3 with points pt 7 ps 0.75

}


reset