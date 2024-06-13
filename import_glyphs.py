import os
import fontforge

with open(r'agl-aglfn/aglfn.txt', 'r') as f:
    lines = f.read().split('\n')
    valid = filter(lambda line: line != '' and line[0] != '#', lines)
    entries = map(lambda line: line.split(';'), valid)
    glyphtable: dict = {name: int(code, 16) for code, glyph, name in entries}

font = fontforge.open(r'emptytemplate.sfd')

variations: list = [
        'regular',
        ]

for variation in variations:
    dir_name: str = f'build/{variation}'
    dir_contents: list = os.listdir(dir_name)
    svg_files = filter(lambda filename: filename[-4:] == '.svg', dir_contents)
    for filename in svg_files:
        print(f'importing {filename}')
        glyph_name, extension = filename.split('.')
        code: int = glyphtable[glyph_name]
        glyph = font.createChar(code)
        glyph.importOutlines(f'{dir_name}/{filename}', r'correctdir')

        glyph.removeOverlap()
        glyph.correctDirection()
        glyph.simplify(1)
        glyph.round()
        glyph.removeOverlap()
        glyph.addExtrema("all")
        glyph.width = 400

font.save('build/honchokomono.sfd')

