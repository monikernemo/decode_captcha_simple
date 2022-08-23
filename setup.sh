#!/bin/bash 

rm -r testcases
mkdir testcases
pushd testcases 
curl -o sampleCaptchas.zip 'http://hr-testcases.s3.amazonaws.com/2587/assets/sampleCaptchas.zip' 
unzip sampleCaptchas.zip 
rm -r sampleCaptchas.zip
popd