import os
import fontforge

with open(r'agl-aglfn/aglfn.txt', 'r') as f:
    lines = f.read().split('\n')
    valid = filter(lambda line: line != '' and line[0] != '#', lines)
    entries = map(lambda line: line.split(';'), valid)
    glyphtable: dict = {name: int(code, 16) for code, glyph, name in entries}

os.mkdir(r'build')

weights: list = [
        (40, 'light'),
        (80, 'regular'),
        (120, 'bold') ]
for form in os.listdir(r'src'):
    for weight, weightname in weights:
        print(f'populating build/{weightname}-{form}')
        os.mkdir(f'build/{weightname}-{form}')
        for filename in os.listdir(f'src/{form}'):
            infile: str = f'src/{form}/{filename}'
            outfile: str = f'build/{weightname}-{form}/{filename}'

            with open(infile, 'r') as instroke:
                contents: str = instroke.read()
                contents = contents.replace('stroke-width:120', f'stroke-width:{weight + 40}')
                contents = contents.replace('stroke-width:70', f'stroke-width:{weight}')

                with open(outfile, 'w') as outstroke:
                    outstroke.write(contents)

variations: list = [
        ('light-normal', 'Light'),
        ('regular-normal', 'Regular'),
        ('bold-normal', 'Bold'),
        ('light-italic', 'Light Italic'),
        ('regular-italic', 'Italic'),
        ('bold-italic', 'Bold Italic')
        ]

for dirname, name in variations:
    createdtbl: dict = {}

    weight, form = dirname.split('-')
    font = fontforge.open(r'emptytemplate.sfd')
    print(f'importing build/{dirname}')
    for filename in os.listdir(f'build/{dirname}'):
        print(f'importing build/{dirname}/{filename}')
        unicode_name: str = filename.split('.')[0]
        codepoint: int = glyphtable[unicode_name]

        glyph = font.createChar(codepoint)
        createdtbl.update({glyph.glyphname: glyph})

        glyph.importOutlines(f'build/{dirname}/{filename}')
        glyph.width = 500
        glyph.removeOverlap()
        glyph.simplify(1)
        glyph.addExtrema("all")

    font.addLookup('ligatures', 'gsub_ligature', None, (("liga",(("DFLT",("dflt")),("latn",("dflt")),)),))
    font.addLookupSubtable('ligatures', 'ligatures-1')
    for filename in os.listdir(f'build/{dirname}-liga'):
        print(f'importing build/{dirname}-liga/{filename}')
        names: list = filename.split('.')[0].split('_')
        liganame = names.pop(0)
        # liganame += '.ligature'

        glyph = font.createChar(-1, liganame)
        glyph.glyphclass = 'baseligature'
        glyph.glyphname = liganame + '.ligature'
        glyph.addPosSub('ligatures-1', names)
        createdtbl.update({glyph.glyphname: glyph})

        glyph.importOutlines(f'build/{dirname}-liga/{filename}')
        glyph.width = 500 * len(names)
        glyph.removeOverlap()
        glyph.simplify(1)
        glyph.addExtrema("all")

    for filename in os.listdir(f'build/{dirname}-cont'):
        print(f'importing build/{dirname}-cont/{filename}')
        contname = filename.replace('.svg', '')
        glyph = font.createChar(-1, contname)
        glyph.glyphname = contname
        createdtbl.update({glyph.glyphname: glyph})

        glyph.importOutlines(f'build/{dirname}-cont/{filename}')
        glyph.width = 500
        glyph.removeOverlap()
        glyph.simplify(1)
        glyph.addExtrema("all")

    font.addLookup('caltrules', 'gsub_contextchain', None, (("calt",(("DFLT",("dflt")),("latn",("dflt")),)),))
    with open('caltrules.txt', 'r') as crfile:
        crlines = crfile.read().split('\n')
        for crline in filter(lambda line: line != '', crlines):
            contname, prenames, rule = crline.split(':')
            font.addLookup(contname, 'gsub_single', None, (("aalt",(("DFLT",("dflt")),("latn",("dflt")),)),))
            font.addLookupSubtable(contname, contname + '-1')
            for name in prenames.split(' '):
                preglyph = createdtbl[name]
                preglyph.addPosSub(contname + '-1', contname)
            rule = rule.replace('!', f'[{prenames}] @<{contname}>')
            font.addContextualSubtable('caltrules', contname, 'coverage', rule)

    font.removeOverlap()
    font.correctDirection()
    font.fontname = f'honchokomono-{dirname}'
    font.fullname = f'honchokomono {name}'
    font.familyname = f'honchokomono-{form}'
    font.weight = weight
    font.os2_weight = {'light': 300, 'regular': 400, 'bold': 700}[weight]
    font.appendSFNTName('English (US)', 'Preferred Styles', f'{name}')
    font.appendSFNTName('English (US)', 'WWS Family', f'honchokomono')
    font.appendSFNTName('English (US)', 'WWS Subfamily', f'{name}')
    if form == 'italic':
        font.italicangle = -12
    font.save(f'build/honchokomono_{dirname}.sfd')
    font.generate(f'build/honchokomono-{dirname}.otf')
    font.close()

