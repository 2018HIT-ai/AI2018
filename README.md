# AI2018
## README
问题5：找到所有的角落

在角落迷宫的四个角上面有四个豆。这个搜索问题要求找到一条访问所有四个角落的最短的路径。
完成searchAgents.py文件中的CornersProblem搜索问题，你需要重新定义状态，使其能够表示角落是否被访问。用以下命令测试你得code：
```seq
Python2 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
Python2 pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
提示：新的状态只包含吃豆人的位置和角落的状态。

问题6：角落问题（启发式）

构建合适的启发函数，完成searchAgents.py文件中的cornersHeuristic角落搜索问题。用以下命令测试你得code：
```seq
Python2 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

问题8：次最优搜索

定义一个优先吃最近的豆子函数是提高搜索速度的一个好的办法。补充完成searchAgents.py文件中的AnyFoodSearchProblem目标测试函数，
并完成searchAgents.py文件中的ClosestDotSearchAgent部分，在此Agent当中缺少一个关键的函数：找到最近豆子的函数。

用以下命令测试你得code：
```seq
Python2 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```
