santa = {'x':0, 'y':0}
robot = {'x':0, 'y':0}
visited = {}

def updateSanta(c):
	if c == '^':
		santa['y'] += 1
	elif c == 'v':
		santa['y'] -= 1
	elif c == '<':
		santa['x'] -= 1
	elif c == '>':
		santa['x'] += 1

def updateRobot(c):
	if c == '^':
		robot['y'] += 1
	elif c == 'v':
		robot['y'] -= 1
	elif c == '<':
		robot['x'] -= 1
	elif c == '>':
		robot['x'] += 1

def addSanta():
	if not visited.has_key(santa['x']):
		visited[santa['x']] = [santa['y']]
	elif not santa['y'] in visited[santa['x']]:
		visited[santa['x']].append(santa['y'])

def addRobot():
	if not visited.has_key(robot['x']):
		visited[robot['x']] = [robot['y']]
	elif not robot['y'] in visited[robot['x']]:
		visited[robot['x']].append(robot['y'])

def printRes():
	ret = 0
	for x in visited:
		ret += len(visited[x])
	print(ret)

def main():
	f = open('input', 'r')
	addSanta()
	i = True
	for l in f:
		for c in l:
			if i:
				updateSanta(c)
				addSanta()
			else:
				updateRobot(c)
				addRobot()
			i = not i
	printRes()

main()
