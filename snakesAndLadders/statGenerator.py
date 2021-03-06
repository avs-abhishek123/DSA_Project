from minThrows3 import modifiedDijkstra as modifiedDijkstraImproved
from minThrows import modifiedDijkstra, createBoard
from minThrows2 import sequenceSolver
import os
import time
import matplotlib.pyplot as plt

if __name__ == "__main__":
	algo1 = []
	algo2 = []
	algo3 = []
	files = []
	x = 1
	for file in os.listdir("./100x100inputs"):
		if file.endswith(".txt"):
			print file[5:file.index('.')]
			files.append(int(file[5:file.index('.')]))
			start = time.time()
			board = createBoard(10001)
			modifiedDijkstra(10001, board, False)
			timeTaken = time.time() - start
			algo1.append(timeTaken)
			start = time.time()
			board = createBoard(10001)
			sequenceSolver(10001, board, False)
			timeTaken = time.time() - start
			algo2.append(timeTaken)
			start = time.time()
			board = createBoard(10001)
			modifiedDijkstraImproved(10001, board, False)
			timeTaken = time.time() - start
			algo3.append(timeTaken)
			x = x + 1
		if x==1000:
			break
	print "Average time for Modified Dijkstra: " + str(reduce(lambda x, y: x + y, algo1) / len(algo1))
	print "Average time for Sequential Solver: " + str(reduce(lambda x, y: x + y, algo2) / len(algo2))
	print "Average time for improved Dijkstra: " + str(reduce(lambda x, y: x + y, algo3) / len(algo3))
	algo1 = [x for (y,x) in sorted(zip(files, algo1))]
	algo2 = [x for (y,x) in sorted(zip(files, algo2))]
	algo3 = [x for (y,x) in sorted(zip(files, algo3))]
	files.sort()
	plt.plot(files, algo1, '-ro', label="Modified Dijkstra")
	plt.plot(files, algo2, '-go', label="Sequential Solver")
	plt.plot(files, algo3, '-bo', label="Modified Dijkstra Improved")
	plt.legend()
	plt.show()