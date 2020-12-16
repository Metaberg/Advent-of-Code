import collections
import re

input_file = open("../src/d7-input.txt", "r")
rules = [l.rstrip('\n') for l in input_file]
input_file.close()

bags = collections.defaultdict(list)
inner_bags = collections.defaultdict(set)

for rule in rules:
    color = str(re.match('(^.*) bags contain', rule)[1])
    for no, inner_bag in re.findall("(\d+) (.+?) bags?[,.]", rule):
        inner_bags[inner_bag].add(color)
        bags[color].append((int(no), inner_bag))

golden_bags = set()


def solver(solve_color):
    for i in inner_bags[solve_color]:
        golden_bags.add(i)
        solver(i)


solver('shiny gold')
print(len(golden_bags))
