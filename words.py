#!/usr/bin/env python3
"""Retrieve and prints words from a URL

Usage:
    python3 words.py <URL>

"""
from urllib.request import urlopen
from sys import argv

def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: the URL of a URF-8 text document

    Returns:
        A list of string containing the words from the document.
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    if len(argv) > 1:
        url = argv[1]
    else:
        url = "http://sixty-north.com/c/t.txt"
    main(url)