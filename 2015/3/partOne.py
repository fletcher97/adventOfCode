santa = {'x':0, 'y':0}
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

def addSanta():
	if not visited.has_key(santa['x']):
		visited[santa['x']] = [santa['y']]
	elif not santa['y'] in visited[santa['x']]:
		visited[santa['x']].append(santa['y'])

def printRes():
	ret = 0
	for x in visited:
		ret += len(visited[x])
	print(ret)

def main():
	f = open('input', 'r')
	addSanta()
	for l in f:
		for c in l:
			updateSanta(c)
			addSanta()
	printRes()

main()
