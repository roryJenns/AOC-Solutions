from collections import defaultdict
from typing import List, DefaultDict, Tuple
import os
 
 
def read_and_init(fn) -> Tuple[DefaultDict[complex, int], List[complex], List[str]]:
    dots = []
    folds = []
    paper = defaultdict(int)
    with open(fn, 'r') as fo:
        lines = fo.read().splitlines()
    for line in lines:
        if line:
            if 'fold' in line:
                folds.append(line.split()[2])
            else:
                x, y = list(map(int, line.split(',')))
                dots.append(x+1j*y)
    return paper, dots, folds
 
 
def transform(paper: DefaultDict[complex, int], fold: str) -> DefaultDict[complex, int]:
    axis, val = fold.split('=')
    new_paper = defaultdict(int)
    if axis == 'x':
        # vertical fold
        x_max = int(val)
        y_max = int(max(key.imag for key in paper))
        for y in range(y_max + 1):
            for x in range(x_max):
                loc = x+1j*y
                mirror_loc = (2*x_max-x)+1j*y
                new_paper[loc] = paper[loc] | paper[mirror_loc]
    else:
        # horizontal fold
        y_max = int(val)
        x_max = int(max(key.real for key in paper))
        for y in range(y_max):
            for x in range(x_max + 1):
                loc = x+1j*y
                mirror_loc = x+1j*(2*y_max-y)
                new_paper[loc] = paper[loc] | paper[mirror_loc]
    return new_paper
 
 
def part1(paper: DefaultDict[complex, int], dots: List[complex], folds: List[str]):
    for dot in dots:
        paper[dot] = 1
    fold = folds[0]
    paper = transform(paper, fold)
    return sum(paper.values())
 
 
def part2(paper: DefaultDict[complex, int], dots: List[complex], folds: List[str]):
    for dot in dots:
        paper[dot] = 1
    for fold in folds:
        paper = transform(paper, fold)
    display = []
    for y in range(int(max(k.imag for k in paper)) + 1):
        line = []
        for x in range(int(max(k.real for k in paper)) + 1):
            if paper[x+1j*y]:
                line.append('#')
            else:
                line.append(' ')
        display.append(''.join(line))
    for line in display:
        print(line)
 
 
p, d, f = read_and_init("input.txt")
result = part1(p, d, f)
print('Part 1:', result)
part2(p, d, f)