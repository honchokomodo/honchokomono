#!/bin/sh

inkscape_command="flatpak run org.inkscape.Inkscape"
for d in src/*; do
	for i in $d/*.svg; do
		o=$(echo $i | sed "s/src/build/")
		echo converting $i 
		${inkscape_command} \
		--actions="select-all:all;object-stroke-to-path" \
		--export-filename="$o" "$i"
		#--actions="select-all:all;object-stroke-to-path;select-all:all;path-union" \
	done
done

