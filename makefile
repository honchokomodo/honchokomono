main:
	flatpak run org.fontforge.FontForge -lang=py -script import_strokes.py

clean:
	rm -r build
