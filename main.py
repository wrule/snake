#!/opt/homebrew/bin/python3

import os
from random import random

WIDTH = 30
HEIGHT = 13
DIR_DICT = { 'w': 'Y_UP', 's': 'Y_DOWN', 'a': 'X_LEFT', 'd': 'X_RIGHT' }

def initGameMap(snake):
  gameMap = [];
  for y in range(0, HEIGHT):
    gameMap.append([])
    for x in range(0, WIDTH):
      if xyIsInWall(x, y):
        gameMap[y].append(1)
      else:
        gameMap[y].append(0)
  putFood(gameMap, snake)
  return gameMap

def initSnake():
  snake = []
  initX = int(WIDTH / 2) + 1
  initY = int(HEIGHT / 2)
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

def xyIsInWall(x, y):
  return x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1

def xyIsFood(x, y, gameMap):
  return gameMap[y][x] == 2

def clearFood(
  gameMap,
):
  for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
      if gameMap[y][x] == 2:
        gameMap[y][x] = 0

def putFood(
  gameMap,
  snake,
):
  clearFood(gameMap)
  x = 0
  y = 0
  while True:
    x = 1 + int(random() * (WIDTH - 2))
    y = 1 + int(random() * (HEIGHT - 2))
    if not xyIsInBody(x, y, snake):
      break
  gameMap[y][x] = 2

def snakeMove(
  gameMap,
  snake,
  direction,
):
  head = snake[0]
  targetX = 0
  targetY = 0
  if direction == 'Y_UP':
    targetY = head['y'] - 1
    targetX = head['x']
  elif direction == 'Y_DOWN':
    targetY = head['y'] + 1
    targetX = head['x']
  elif direction == 'X_LEFT':
    targetY = head['y']
    targetX = head['x'] - 1
  elif direction == 'X_RIGHT':
    targetY = head['y']
    targetX = head['x'] + 1
  if xyIsInBody(targetX, targetY, snake):
    return '撞自己'
  if xyIsInWall(targetX, targetY):
    return '撞墙'
  newHead = { 'x': targetX, 'y': targetY }
  snake.insert(0, newHead)
  if xyIsFood(targetX, targetY, gameMap):
    putFood(gameMap, snake)
  else:
    snake.pop()
  return '平安'

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

def main():
  direction = 'Y_UP'
  status = '平安'
  snake = initSnake()
  gameMap = initGameMap(snake)
  while True:
    os.system('clear')
    render(gameMap, snake)
    keyCode = input('请输入（w上，s下，a左，d右，enter继续，exit退出）：')
    if keyCode in DIR_DICT.keys():
      newDirection = DIR_DICT[keyCode]
      if direction[0:2] != newDirection[0:2]:
        direction = newDirection
    elif keyCode == 'exit':
      status = '用户退出'
      break
    status = snakeMove(gameMap, snake, direction)
    if status != '平安':
      break
  print('游戏结束，原因：', status)  

main()
