#!/opt/homebrew/bin/python3


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

def xyIsFood(x, y, gameMap):
  return gameMap[y][x] == 2

def clearFood(
  gameMap,
):
  y = 0
  x = 0
  for row in gameMap:
    for land in row:
      if land == 2:
        gameMap[y][x] = 0
      x += 1
    y += 1
      

def putFood(
  gameMap,
  snake,
  weight,
  height,
):
  # clearFood(gameMap)
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

def snakeMove(
  gameMap,
  snake,
  direction,
):
  head = snake[0]
  targetX = 0
  targetY = 0
  if direction == 'UP':
    targetY = head['y'] - 1
    targetX = head['x']
  elif direction == 'DOWN':
    targetY = head['y'] + 1
    targetX = head['x']
  elif direction == 'LEFT':
    targetY = head['y']
    targetX = head['x'] - 1
  elif direction == 'RIGHT':
    targetY = head['y']
    targetX = head['x'] + 1
  if xyIsInBody(targetX, targetY, snake):
    return '撞自己'
  if xyIsWall(targetX, targetY, WEIGHT, HEIGHT):
    return '撞墙'
  newHead = {
    'x': targetX,
    'y': targetY,
  }
  snake.insert(0, newHead)
  if xyIsFood(targetX, targetY, gameMap):
    putFood(gameMap, snake, WEIGHT, HEIGHT)
  else:
    snake.pop()
  return '平安'

gameMap = initGameMap(WEIGHT, HEIGHT)
snake = initSnake(WEIGHT, HEIGHT)
putFood(gameMap, snake, WEIGHT, HEIGHT)
direction = 'UP'
dirDict = {
  'w': 'UP',
  's': 'DOWN',
  'a': 'LEFT',
  'd': 'RIGHT',
}
while True:
  os.system('clear')
  render(gameMap, snake)
  status = '平安'
  keyCode = input()
  if keyCode in dirDict.keys():
    direction = keyCode
  elif keyCode == 'exis':
    break
  status = snakeMove(gameMap, snake, direction)
  if status != '平安':
    print(status)
    break
