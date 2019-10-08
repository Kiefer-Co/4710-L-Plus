import re
import sys

replacements = {
    r'\\integer': r'ℤ',
    r'\\not_in': r'∉',
    r'\\in': r'∈',
    r'\\union': r'⋃',
    r'\\intersection': r'⋂',
    r'=>': r'⇒',
    r'>=': r'≥',
    r'<=': r'≤',
    r'!=': r'≠',
    r'\\empty_set': r'Ø',
    r'\\empty_string': r'ε',
    r'\\all': r'∀',
    r'\\for_all': r'∀',
    r'\\exists': r'∃',
    r'\\delta': r'δ',
    r'\\Sigma': r'Σ',
    r'\\Pi': r'Π',
    r'{}': r'\{\}',
    r'\^\*': r'^\*',
    r'\\page_break': r'<div style="page-break-after: always;"></div>',
    r'_(.*?)([ ,\n\)\^}:])': r'<sub>\1</sub>\2',
    r'\^(.*?)([ ,\n\)}:])': r'<sup>\1</sup>\2'
}

if __name__ == '__main__':
    try:
        source_file = sys.argv[1]
        target_file = sys.argv[2]
    except IndexError:
        source_file = 'test.md'
        target_file = 'new.md'

    with open(source_file, 'r') as file:
        text = file.read()

        for key, value in replacements.items():
            text = re.sub(key, value, text)

    with open(target_file, 'w+', encoding='UTF-8') as file:
        file.write(text)
