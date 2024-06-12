#!/bin/sh

inkscape_command="flatpak run org.inkscape.Inkscape"
for d in src/*; do
	for i in $d/*.svg; do
		o=$(echo $i | sed "s/src/build/")
		${inkscape_command} \
		--actions="select-all:all;object-stroke-to-path" \
		--export-filename="$o" "$i"
	done
done

