#!/bin/bash 

rm -r testcases
mkdir testcases
pushd testcases 
curl -o sampleCaptchas.zip 'http://hr-testcases.s3.amazonaws.com/2587/assets/sampleCaptchas.zip' 
unzip sampleCaptchas.zip 
echo YMB1Q > output/output100.txt
echo CL69V > output/output21.txt
rm -r sampleCaptchas.zip
rm -r input/*.txt
popd
python3 knn_model.py 
