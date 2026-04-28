import pytest
from tree import Tree
from node import Node

@pytest.fixture
def tree():
    tree = Tree()
    nodes = [10, 5, 15, 3, 7]
    for n in nodes:
        tree.add(n)
    return tree

def test_root(tree):
    result = tree.find(10)
    assert result is not None
    assert result.data == 10

def test_last(tree):
    result = tree.find(3)
    assert result is not None
    assert result.data == 3

def test_missing_elem(tree):
    result = tree.find(99)
    assert result is None

def test_empty_tree():
    empty_tree = Tree()
    result = empty_tree.find(10)
    assert result is None

def test_node_type(tree):
    result = tree.find(15)
    assert isinstance(result, Node)