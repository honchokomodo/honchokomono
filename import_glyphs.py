import os
import fontforge

with open(r'agl-aglfn/aglfn.txt', 'r') as f:
    lines = f.read().split('\n')
    valid = filter(lambda line: line != '' and line[0] != '#', lines)
    entries = map(lambda line: line.split(';'), valid)
    glyphtable: dict = {name: int(code, 16) for code, glyph, name in entries}


variations: list = [
        'normal-light', 'italic-light',
        'normal-regular', 'italic-regular',
        'normal-bold', 'italic-bold'
        ]

for variation in variations:
    form, weight = variation.split('-')
    font = fontforge.open(r'emptytemplate.sfd')
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
        glyph.simplify(1)
        glyph.width = 400

    font.fontname = f"honchokomono-{variation}"
    font.fullname = f"honchokomono-{form}{weight}"
    font.familyname = f"honchokomono-{form}"
    font.weight = weight
    font.os2_weight = {'light': 300, 'regular': 400, 'bold': 700}[weight]
    font.appendSFNTName('English (US)', 'Preferred Styles', f'{form}{weight}')
    font.appendSFNTName('English (US)', 'WWS Family', f'honchokomono')
    font.appendSFNTName('English (US)', 'WWS Subfamily', f'{form}{weight}')
    if form == 'italic':
        font.italicangle = -12
    font.save(f'build/honchokomono_{variation}.sfd')
    font.generate(f'build/honchokomono-{variation}.otf')
    font.close()

