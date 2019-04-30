from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = [] #single edge matrix
transform = new_matrix() #single master transformation matrix

parse_file( 'script', edges, transform, screen, color )
