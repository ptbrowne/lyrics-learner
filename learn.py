#-*-coding: utf-8 -*-

import os
import os.path as osp
from random import randint
import argparse

def ask(question):
    res = None
    while not res:
        res = raw_input(question + ' ')
    return res

def group_until(arr, sep):
    def _group_until(arr, sep):
        group = []
        for item in arr:
            if item == sep:
                yield group
                group = []
            else:
                group.append(item)
        yield group

    return list(_group_until(arr, sep))

def transform(line, hide_words):
    if hide_words:
        line = ' '.join(map(lambda word: '*' * len(word) if randint(0, 0) == 1 else word, line.split(' ')))
    return line


def flatten(arr):
    return [i for g in arr for i in g]


def learn(lyrics, nb_lines, hide_words=False):
    lines = [l for l in lyrics.split('\n') if len(l) > 0 and not l.startswith('#')]
    groups = group_until(lines, '---')

    if len(groups) > 1:
        for i, g in enumerate(groups):
            print i, g[0]
        print

        chosen_groups = map(int, ask('Part of the song to learn (comma for several) ?').split(','))
    else:
        chosen_groups = [0]

    lines = flatten(map(lambda i: groups[i], chosen_groups))

    while True:
        r = randint(0, len(lines) - nb_lines - 1)
        print transform(lines[r], hide_words),
        raw_input()
        for offset in range(1, nb_lines):
            print lines[r + offset],
            raw_input()
        print
        print


def learn_from_file(filename, *args, **kwargs):
    with open(filename) as l:
        lyrics = l.read()
        learn(lyrics, *args, **kwargs)


def choose_file(question, directory=osp.abspath(osp.dirname(__file__))):
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    for i, filename in enumerate(files):
        print '%i) %s' % (i + 1, filename)
    n = int(raw_input(question))
    return osp.join(directory, files[n - 1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    parser.add_argument('--nb-lines', default=2, type=int)
    args = parser.parse_args()
    if not args.filename:
        filename = choose_file('Which lyrics do you want to learn ? ')
    else:
        filename = args.filename
    print 'Learning %s' % filename
    print
    try:
        learn_from_file(filename, args.nb_lines, hide_words=True)
    except KeyboardInterrupt:
        print('\nGood job 👍 See you later !')
