import sys
from bs4 import BeautifulSoup
from bs4.element import Tag
from typing import List


def get_xml_soup(xml_text: str):
    return BeautifulSoup(xml_text, 'lxml-xml')


def get_xml_depth(xml_text: str) -> int:
    """Returns depth of xml text."""
    xml_soup = get_xml_soup(xml_text)
    tags = xml_soup.find_all()
    depth = _recursive_depth_counter(tags) - 1
    return depth


def _recursive_depth_counter(tags: List[Tag]) -> int:
    if tags:
        a = [_recursive_depth_counter(tag.findChildren()) for tag in tags]
        return 1 + max(a)
    else:
        return 0


if __name__ == '__main__':
    text = sys.argv[1]
    depth = get_xml_depth(text)
    print(f'Your xml depth is {depth}.')
