main: glyphs builddir
	#fontforge -lang=py -script import_glyphs.py
	flatpak run org.fontforge.FontForge -lang=py -script import_glyphs.py

clean:
	rm -r build

glyphs: builddir
	./convert_strokes.sh

builddir:
	mkdir -p build
	mkdir -p build/regular
