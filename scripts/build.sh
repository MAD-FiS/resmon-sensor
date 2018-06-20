#!/bin/bash

echo "ResMon builder"
echo "----------------------"
echo ""

rm -f `find . -name '*.pyc'`
rm -rf `find . -name  '__pycache__'`

cat ./scripts/install.template > install-sensor.sh
echo "ARCHIVE_DATA:" >> install-sensor.sh
echo "- Install file is created"

ELEMENTS=`cat ./data/elements.txt`
tar -czvf tmp.tar.gz $ELEMENTS >> /dev/null
cat tmp.tar.gz >> install-sensor.sh
rm tmp.tar.gz
echo "- Required data is compressed and included"

chmod 770 install-sensor.sh
echo "- File ./install-sensor.sh is ready to be used"
