#!/usr/bin/env python

from numpy.random import choice, seed
import sys
import time

def main(mode):

    seed(int(time.time()))
    class consonant(object):

        def __init__(self, placement, manner, letters):

            self.placement = placement
            self.manner = manner
            self.letters = letters

    b = consonant('labial', 'voiced stop', ['b', 'beta'])
    p = consonant('labial', 'voiceless stop', ['p', 'pi'])
    ph = consonant('labial', 'voiceless aspirated stop', ['p', 'phi'])
    m = consonant('labial', 'nasal', ['m', 'mu'])
    f = consonant('labio-dental', 'voiceless fricative', ['f'])
    v = consonant('labio-dental', 'voiced fricative', ['v'])

    t = consonant('dental', 'voiceless stop', ['t', 'tau'])
    d = consonant('dental', 'voiced stop', ['d', 'delta'])
    theta = consonant('dental', 'voiceless aspirated stop', ['theta'])
    th = consonant('dental', 'voicless/voiced fricative', 'modern th')
    n = consonant('dental', 'nasal', ['n', 'nu'])

    s = consonant('alveolar', 'sibilant', ['s', 'sigma'])
    l = consonant('alveolar', 'voiced lateral liquid', ['l', 'lambda'])
    r = consonant('alveolar', 'voiced liquid', ['r', 'rho'])
    ch = consonant('palato-alveolar', 'voiceless affricate', ['ch'])
    j = consonant('palato-alveolar', 'voiced affricate', ['j'])
    sh = consonant('palato-alveolar', 'voiceless fricative', ['sh'])
    zh = consonant('palato-alveolar', 'voiced fricative', ['zh'])

    i = consonant('palatal', 'approximant', ['i', 'y'])

    k = consonant('velar', 'unaspirated voiceless stop', ['k','c', 'kappa'])
    g = consonant('velar', 'voiced stop', ['g', 'gamma'])
    kh = consonant('velar', 'aspirated voiceless stop', ['chi'])
    ng = consonant('velar', 'nasal/fricative',
                   ['ng', 'gn', 'gamma+(chi|gamma|kappa)'])

    qu = consonant('labio-velar', 'voiceless approximant', ['qu'])

    h = consonant('glottal', 'voiceless fricative' ,
                  ['h', 'rough breathing mark'])

    deck = [b, p, ph, m, f, v, t, d, theta, th, n, s, l, r, ch, j, sh, zh,
            i, k, g, kh, ng, qu, h]

    for i in range(len(deck)):

        card = choice(deck, replace=False)
        if(mode == 'letter'):
            print('\n')
            print(card.letters)
            if(input()):
                print(card.placement)
                print(card.manner)

        if(mode == 'place'):
            print('\n')
            print(card.placement)
            print(card.manner)
            if(input()):
                print(card.letters)

    return

if(__name__ == '__main__'):
    if(len(sys.argv) < 2):
        sys.exit(1)
    main(sys.argv[1])
