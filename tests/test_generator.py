from bbook.generator.script import *
from os import path
import filecmp

def test_markdown_exists():
    generator()
    assert path.exists("./generator/book/test.md") == True

def test_generator_ouput_exists():
    generator()
    assert path.exists("./generator/public/test.html") == True

def test_html_file():
    assert filecmp.cmp('./tests/test.html', './generator/public/test.html') == True

def test_public_directory_exists():
    assert path.exists("./generator/public") == True

def test_book_directory_exists():
    assert path.exists("./generator/book") == True