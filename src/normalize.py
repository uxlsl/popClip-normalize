#!/usr/bin/env python3
import sys
import unicodedata


def main():
    text = sys.stdin.read()
    text = unicodedata.normalize('NFKC', text)
    print(text)


if __name__ == '__main__':
    main()
