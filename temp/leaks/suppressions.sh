#!/bin/zsh

#executable name
NAME="bla"
# valgrind location
VAL=~/goinfre/brew/bin/valgrind


#generate clean main file
MAINFILE="clean_main.c"
echo "int main(void) {return 1;}" > $MAINFILE
#compile the executable
MAINCLEAR=mainclear
gcc $MAINFILE -o $MAINCLEAR
#name of the suppressions file
FILENAME="val_sup.txt"
#temp file
TEMP="tempfile.txt"
# generate file
$VAL --gen-suppressions=all --leak-check=full --show-leak-kinds=all ./$MAINCLEAR 2>./$TEMP
# delete all == and --
cat $TEMP | grep -v "==" | grep -v "\-\-" | grep -v "warning" > $FILENAME
# delete temp files
rm $TEMP
rm $MAINCLEAR
rm $MAINFILE
#clear

# use valgrind again, with the suppressions file
#$VAL --suppressions=./$FILENAME ./$NAME

# delete text file
#rm $FILENAME
