import pygame as pg
from pygame.locals import *
import sys

WIDTH = 800
HEIGHT = 500
LENGTH = 100
FPS = 50
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (120, 120, 120)

test_def =[
			'2       ',
			'  S     ',
			'21  S   ',
			'13      ',
			'2 3     '
			]
test_off = [[0,4,28],[1,1,6],[2,0,10],[2,4,15],[2,2,16],[3,3,13]]


def	draw_grid(surface):
	n, m, length = HEIGHT // LENGTH, WIDTH // LENGTH, LENGTH
	for i in range(m):
		for j in range(n):
			if (i + j) % 2:
				pg.draw.rect(surface, GREY, pg.Rect(i * length, j * length, length, length))
			else:
				pg.draw.rect(surface, BLACK, pg.Rect(i * length, j * length, length, length))

def	draw_def(surface, def_list):
	n, m, length = HEIGHT // LENGTH, WIDTH // LENGTH, LENGTH
	for i in range(m):
		for j in range(n):
			if (def_list[j][i].isnumeric()):
				x = int(def_list[j][i])
				pg.draw.rect(surface, (0, 155 + 100 // (4 - x), 0), pg.Rect(i * length, j * length, length, length))
			elif (def_list[j][i] == 'S'):
				pg.draw.rect(surface, BLUE, pg.Rect(i * length, j * length, length, length))

def	draw_off(surface, off_list):
	n, m, length = HEIGHT // LENGTH, WIDTH // LENGTH, LENGTH
	for i in off_list:
		pg.draw.rect(surface, (55 + 200 // (29 - i[2]), 0, 0), pg.Rect((m - i[0] - 1) * length, i[1] * length, length, length))
pg.init()
surface = pg.display.set_mode((WIDTH,HEIGHT))
color = (255,0,0)
clock = pg.time.Clock()
while (1):
	clock.tick(FPS)
	for i in pg.event.get():
		if i.type == QUIT:
			pg.quit()
			sys.exit()
		elif i.type == KEYDOWN:
			print(i.key)
	draw_grid(surface)
	draw_def(surface, test_def)
	draw_off(surface, test_off)
	pg.display.flip()
