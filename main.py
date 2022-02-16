#!/usr/bin/python3



from asyncio import sleep
from random import random
import os
import time


def initGameMap(weight, height):
  gameMap = [];
  for y in range(0, height):
    gameMap.append([])
    for x in range(0, weight):
      if x == 0 or x == weight - 1 or y ==0 or y == height - 1:
        gameMap[y].append(1)
      else:
        gameMap[y].append(0)
  return gameMap

def initSnake():
  snake = []
  snake.append({ 'x': 11, 'y': 5 });
  snake.append({ 'x': 11, 'y': 6 });
  snake.append({ 'x': 11, 'y': 7 });
  return snake

def xyIsInBody(
  x,
  y,
  snake,
):
  isInBody = False
  for body in snake:
    if body['y'] == y and body['x'] == x:
      isInBody = True
      break
  return isInBody

def putFood(
  gameMap,
  snake,
):
  x = 0
  y = 0
  while True:
    x = 1 + int(random() * 18)
    y = 1 + int(random() * 8)
    if not xyIsInBody(x, y, snake):
      break
  gameMap[y][x] = 2

def render(
  gameMap,
  snake,
):
  y = 0
  for row in gameMap:
    x = 0
    rowStr = ''
    for land in row:
      if xyIsInBody(x, y, snake):
        rowStr += '●'
      else:
        if land == 0:
          rowStr += ' '
        elif land == 1:
          rowStr += '■'
        elif land == 2:
          rowStr += '☆'
      x += 1
    print(rowStr)
    y += 1

while True:
  os.system('clear')
  gameMap = initGameMap(20, 10)
  snake = initSnake()
  putFood(gameMap, snake)
  render(gameMap, snake)
  time.sleep(0.2)
