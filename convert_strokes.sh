#!/bin/sh
set -e

inkscape_command="flatpak run org.inkscape.Inkscape"
for d in src/*; do
	for i in $d/*.svg; do
		echo converting $i 
		o=$(echo $i | sed "s/src/build/")
		o_l=$(echo $o | sed -E "s/(ormal|talic)/l/")
		o_r=$(echo $o | sed -E "s/(ormal|talic)/r/")
		o_b=$(echo $o | sed -E "s/(ormal|talic)/b/")
		cat "$i" | sed "s/stroke-width:70/stroke-width:40/" | \
			${inkscape_command} \
			--actions="select-all:all;object-stroke-to-path" \
			--export-filename="$o_l" -p
		cat "$i" | \
			${inkscape_command} \
			--actions="select-all:all;object-stroke-to-path" \
			--export-filename="$o_r" -p
		cat "$i" | sed "s/stroke-width:70/stroke-width:100/" | \
			${inkscape_command} \
			--actions="select-all:all;object-stroke-to-path" \
			--export-filename="$o_b" -p
	done
done

