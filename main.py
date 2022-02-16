#!/usr/bin/python3


from asyncio import sleep
from random import random
import os
import time

WEIGHT = 30
HEIGHT = 13

def initGameMap(weight, height):
  gameMap = [];
  for y in range(0, height):
    gameMap.append([])
    for x in range(0, weight):
      if xyIsWall(x, y, weight, height):
        gameMap[y].append(1)
      else:
        gameMap[y].append(0)
  return gameMap

def initSnake(width, height):
  snake = []
  initX = int(width / 2) + 1
  initY = int(height / 2)
  snake.append({ 'x': initX, 'y': initY });
  snake.append({ 'x': initX, 'y': initY + 1 });
  snake.append({ 'x': initX, 'y': initY + 2 });
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

def xyIsWall(x, y, width, height):
  return x == 0 or x == width - 1 or y == 0 or y == height - 1

def putFood(
  gameMap,
  snake,
  weight,
  height,
):
  x = 0
  y = 0
  while True:
    x = 1 + int(random() * weight - 2)
    y = 1 + int(random() * height - 2)
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
  gameMap = initGameMap(WEIGHT, HEIGHT)
  snake = initSnake(WEIGHT, HEIGHT)
  putFood(gameMap, snake, WEIGHT, HEIGHT)
  render(gameMap, snake)
  time.sleep(0.2)
