main: glyphs builddirs
	#fontforge -lang=py -script import_glyphs.py
	flatpak run org.fontforge.FontForge -lang=py -script import_glyphs.py

clean:
	rm -r build

glyphs: builddirs
	./convert_strokes.sh

builddirs:
	mkdir -p build
	mkdir -p build/nl
	mkdir -p build/nr
	mkdir -p build/nb
	mkdir -p build/il
	mkdir -p build/ir
	mkdir -p build/ib
