# Cours POO et Classes

[Slides](Cours09-POO.pdf)</br>
Introduction à la programmation orientée objet et application des classes à l'algo, particulièrement en Python.

## Exercices

### Level 1
- [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/)
- [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

### Level 2
- [No Space Left On Device](https://adventofcode.com/2022/day/7)
- [Monkey in the Middle](https://adventofcode.com/2022/day/11)

### Level 3
- [Optimisation de distribution hydraulique](https://www.isograd-testingservices.com//FR/solutions-challenges-de-code?cts_id=86) (Exo 4)
- [Advent of Code 2015 - day 7](https://adventofcode.com/2015/day/7) (La 2ème partie teste la robustesse de votre méthode)

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
