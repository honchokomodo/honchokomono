THETEXT=" !\"#$%&'()*+,-./ ->
0123456789:;<=>?
@ABCDEFGHIJKLMNO
PQRSTUVWXYZ[\]^_
\`abcdefghijklmno
pqrstuvwxyz{|}~ "

echo ""
echo -e "\e[0m\e[4mNormal\e[0m\n$THETEXT\e[0m\n"
echo -e "\e[3m\e[4mItalic\e[0m\e[3m\n$THETEXT\e[0m\n"
echo -e "\e[1m\e[4mBold\e[0m\e[1m\n$THETEXT\e[0m\n"
echo -e "\e[3m\e[1m\e[4mBold Italic\e[0m\e[3m\e[1m\n$THETEXT\e[0m\n"
