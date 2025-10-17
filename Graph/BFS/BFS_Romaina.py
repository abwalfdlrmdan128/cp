{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Romania Problem\n",
    "\n",
    "![](https://images.slideplayer.com/36/10602451/slides/slide_3.jpg)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "graph = {\n",
    "    \"Arad\":[(\"Timisoara\",118),(\"Sibiu\",140),(\"Zerind\",75)],\n",
    "    \"Zerind\":[(\"Arad\",75),(\"Oradea\",71)],\n",
    "    \"Oradea\":[(\"Zerind\",71),(\"Sibiu\",151)],\n",
    "    \"Sibiu\":[(\"Arad\",140),(\"Rimnicu Vilcea\",80),(\"Fagaras\",99),(\"Oradea\",151)],\n",
    "    \"Fagaras\":[(\"Sibiu\",99),(\"Bucharest\",211)],\n",
    "    \"Rimnicu Vilcea\":[(\"Sibiu\",80),(\"Pitesti\",97),(\"Craiova\",146)],\n",
    "    \"Pitesti\":[(\"Rimnicu Vilcea\",97),(\"Bucharest\",101),(\"Craiova\",138)],\n",
    "    \"Craiova\":[(\"Pitesti\",138),(\"Rimnicu Vilcea\",146),(\"Dobreta\",120)],\n",
    "    \"Dobreta\":[(\"Craiova\",120),(\"Mehadia\",75)],\n",
    "    \"Mehadia\":[(\"Dobreta\",75),(\"Lugoj\",70)],\n",
    "    \"Lugoj\":[(\"Mehadia\",70),(\"Timisoara\",111)],\n",
    "    \"Timisoara\":[(\"Lugoj\",111),(\"Arad\",118)],\n",
    "    \"Bucharest\":[(\"Fagaras\",211),(\"Pitesti\",101),(\"Giurgiu\",90),(\"Urziceni\",85)],\n",
    "    \"Giurgiu\":[(\"Bucharest\",90)],\n",
    "    \"Urziceni\":[(\"Bucharest\",85),(\"Hirsova\",98),(\"Vaslui\",142)],\n",
    "    \"Hirsova\":[(\"Urziceni\",98),(\"Eforie\",86)],\n",
    "    \"Eforie\":[(\"Hirsova\",86)],\n",
    "    \"Vaslui\":[(\"Urziceni\",142),(\"Iasi\",92)],\n",
    "    \"Iasi\":[(\"Vaslui\",92),(\"Neamt\",87)],\n",
    "    \"Neamt\":[(\"Iasi\",87)]\n",
    "}\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Solving Romania Problem using <b>Breadth-First Search</b>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def bfs(start,goal):\n",
    "    visited = []\n",
    "\n",
    "    # The frontier is a queue\n",
    "    # fronter = [ (City, Path) ]\n",
    "\n",
    "    fronter = [ (start,[start]) ]\n",
    "    while len(fronter)>0:\n",
    "        curr_city,curr_path = fronter.pop(0)\n",
    "        if curr_city==goal:\n",
    "            return curr_path\n",
    "        if curr_city not in visited:\n",
    "            visited.append(curr_city)\n",
    "            # Get curr neighboors\n",
    "            neighboors = graph[curr_city]\n",
    "            for city,cost in neighboors:\n",
    "                fronter.append( (city,curr_path+[city]) )\n",
    "    return \"No Solution found!\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Calculate Cost <b>(Optional)</b>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Calculate the path cost\n",
    "def cal_cost(sol):\n",
    "    sum = 0\n",
    "    for i in range(len(sol)-1):\n",
    "        ns = graph[sol[i]]\n",
    "        for j in ns:\n",
    "            if j[0]==sol[i+1]:\n",
    "                sum+=j[1]\n",
    "                break\n",
    "    return sum\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Execution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Arad', 'Sibiu', 'Fagaras', 'Bucharest', 'Urziceni', 'Vaslui', 'Iasi', 'Neamt']\n",
      "Total Cost = 856\n"
     ]
    }
   ],
   "source": [
    "sol = bfs(\"Arad\",\"Neamt\")\n",
    "print(f\"{sol}\\nTotal Cost = {cal_cost(sol)}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.7"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "25315d184ae1b5b53fe6a801e38c6d8641bbebdfe68235db31e99f74c3473e8e"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
