main:
	#fontforge -lang=py -script import_glyphs.py
	flatpak run org.fontforge.FontForge -lang=py -script import_glyphs.py

clean:
	rm -r build

glyphs: builddirs
	./convert_strokes.sh

builddirs:
	mkdir -p build
	mkdir -p build/normal-light
	mkdir -p build/normal-regular
	mkdir -p build/normal-bold
	mkdir -p build/italic-light
	mkdir -p build/italic-regular
	mkdir -p build/italic-bold
