main:
	fontforge -lang=py -script import_glyphs.py
	#flatpak run org.fontforge.FontForge -lang=py -script import_glyphs.py

clean:
	rm build/honchokomono.sfd

