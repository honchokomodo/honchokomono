THETEXT="  ! \" # $ % & ' ( ) * + , - . / -> ++ <= >= == !=
0 1 2 3 4 5 6 7 8 9 : ; < = > ?
@ A B C D E F G H I J K L M N O
P Q R S T U V W X Y Z [ \ ] ^ _
\` a b c d e f g h i j k l m n o
p q r s t u v w x y z { | } ~  "

echo ""
echo -e "\e[0m\e[4mNormal\e[0m\n$THETEXT\e[0m\n"
echo -e "\e[3m\e[4mItalic\e[0m\e[3m\n$THETEXT\e[0m\n"
echo -e "\e[1m\e[4mBold\e[0m\e[1m\n$THETEXT\e[0m\n"
echo -e "\e[3m\e[1m\e[4mBold Italic\e[0m\e[3m\e[1m\n$THETEXT\e[0m\n"
