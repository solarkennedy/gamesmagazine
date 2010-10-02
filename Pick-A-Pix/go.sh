#!/bin/bash
echo '<html>
<body bgcolor=grey> ' > output.html


wget "http://www.conceptispuzzles.com/form.aspx" --post-data="action=login&requested=myconceptis%2Fprofile&username=cligon&password=gl4554"  --save-cookies cookies.txt --keep-session-cookies -O login.html
COUNTER=1
for EACH in `wget -q "http://www.conceptispuzzles.com/index.aspx?uri=myconceptis/channel/pap" --load-cookies cookies.txt --keep-session-cookies -O -  | grep cafurl | cut -f 4 -d '"' | cut -f 2-100 -d "=" | cut -f 1 -d "&"`
do
	wget  --load-cookies cookies.txt --keep-session-cookies http://www.conceptispuzzles.com/"$EACH"  -O img -t 1
	cp img $COUNTER.caf
	./parsexml.sh >> output.html
	rm img
	let COUNTER=$COUNTER+1
done

echo "</body></html" >> output.html


