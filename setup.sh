pip3 install --upgrade pip

pip3 install pynput && pip3 install termcolor && pip3 install pyfiglet

echo ""
echo -e "text in email subject.txt: "
read text
rm subject.txt 
echo "$text" > subject.txt
echo "your subject text has been added to subject.txt"