#!/bin/bash

echo "ResMon builder"
echo "----------------------"
echo ""

rm -f `find -name '*.pyc'`
rm -rf `find -name  '__pycache__'`

cat ./scripts/install.template > install.sh
echo "ARCHIVE_DATA:" >> install.sh
echo "- Install file is created"

tar -czvf tmp.tar.gz src resmon-sensor README.md requirements resmon-sensor.env >> /dev/null
cat tmp.tar.gz >> install.sh
rm tmp.tar.gz
echo "- Required data is compressed and included"

chmod 770 install.sh
echo "- File ./install.sh is ready to be used"
