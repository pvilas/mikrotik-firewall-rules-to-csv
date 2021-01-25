# -*- coding: utf-8 -*-

import csv,re

# format each rule in one single line and append it to flines

flines = []
cad = ''
n = 1
with open('firewall.rsc') as fp:
    for line in fp:
        line = line.strip()
        if line.endswith('\\'):
            # continuation
            cad += line[:-1]
            continue

        cad += line
        # print cad
        if cad.startswith('#') or cad.startswith('/'):
            print "{} ERROR: {}".format(n, cad)
        else:
            flines.append(cad)
        cad = ''
        n += 1
print flines
rules = []
n = 1
in_quoted_str = False
for l in flines:
    l = l.split(' ')
    print "{} Analyzing {}".format(n, l)
    n += 1
    token_segments = []
    in_quoted_str = False
    tokens = []
    # for each token in list    
    for t in l:
        # if the token has double quotes, we find the closing
        if (t.count('"') == 1):
            in_quoted_str = not in_quoted_str

        token_segments.append(t)
   
        if not in_quoted_str:
            # finalize token
            token = ' '.join(token_segments)
            print "\t{}".format(token)
            tokens.append(token)
            token_segments = []
 

    rules.append([n, l, tokens])
    n += 1

# extract different labels
labels = {}
for r in rules:
    for t in r[2]:  # for each property
        if '=' in t:
            g = t.split('=')
            # save the key value
            # we use a dictionary to avoid duplicated values
            labels[g[0]] = 1

# print all possible labels
print "Labels -----"
labels = labels.keys()
labels.insert(0, 'rule')
for l in labels:
    print l

# create the csv
with open('mk-out.csv', 'wb') as csvfile:
    w = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # write header
    w.writerow(labels)

    # for each line
    for r in rules:
        # initialize void line
        line = []
        for l in labels:
            line.append('')
        # first column is always rule number
        line[0] = r[0]
        # for each rule
        for t in r[2]:
            if '=' in t:
                g = t.split('=')
                line[labels.index(g[0])] = re.sub(r'"$', '', re.sub(r'^"', '', g[1]))
        w.writerow(line)
