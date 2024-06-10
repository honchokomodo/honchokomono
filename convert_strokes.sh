#!/bin/sh

inkscape_command="flatpak run org.inkscape.Inkscape"
for d in $(ls src); do
	for i in $(ls src/$d); do
		${inkscape_command} \
		--actions="select-all:all;object-stroke-to-path" \
		--export-filename=build/$d/$i src/$d/$i
	done
done

