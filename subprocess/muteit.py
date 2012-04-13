#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
def main():
    a='静夜思 李白床前明月光，疑似地上霜。举头望明月，低头思故乡。'.decode('utf-8')
    print a
    list_str = defaultdict(list)
    for pos,v in enumerate(a):
        list_str[pos%6].append(v)

    for k,v in list_str.items():
        print '|'.join(reversed(v))

if __name__ == '__main__':
    main()
