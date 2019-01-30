#!/bin/bash

#read -p "Enter The Image name: "  username
#echo "Welcome $username!"


echo $1
docker run -v /home/sanjkrao/looklearnpost/medium-show-and-tell-caption-generator:/opt/app -e PYTHONPATH=$PYTHONPATH:/opt/app -it medium-show-and-tell-caption-generator  python3 /opt/app/medium_show_and_tell_caption_generator/inference.py --model_path /opt/app/etc/show-and-tell.pb --input_files /opt/app/imgs/$1 --vocab_file /opt/app/etc/word_counts.txt > out.txt 


#echo "Hello"

