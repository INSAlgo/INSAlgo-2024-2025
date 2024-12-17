# Cours Libraries

[Slides](Cours08-PythonLibraries.pdf)</br>
Découverte et explications sur des librairies python utiles.

## Exercices

### Level 1
- [Learn to use counter](https://www.hackerrank.com/challenges/collections-counter/problem)
- [Battledev nov 2020 Ex 1](https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=70) (à faire avec re)
- [Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters/problem) (à faire avec re)

### Level 2
- [AOC 21 Day 03](https://adventofcode.com/2021/day/3)
- [Letter case permutation](https://leetcode.com/problems/letter-case-permutation/) (à faire avec itertools)
- [AOC 24 Day 03](https://adventofcode.com/2024/day/3)
- [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/)

### Level 3
- [AOC 21 Day 14](https://adventofcode.com/2021/day/14)

### Commentaires

Les exos AOC (Advent Of Code) nécessitent de lire un fichier texte au lieu de l'input, voici une fonction qui prend le nom du fichier texte et renvoi une liste de strings correspondant aux lignes d'input :
```python
def read(path: str) -> list[str]:
    file = open(path, "r")
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip("\n")
    print(lines)
    return lines
```

Ou depuis le terminal :
```python
lines = []
s = input()
while s != "":
    lines.append(s)
    s = input()

print(lines)
```
