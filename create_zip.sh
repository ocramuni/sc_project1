#!/bin/bash
folder_name="Agrate_Bibalo_DeNardi_Giunta"
archive_name="ProgettoSocCom1_Agrate_Bibalo_DeNardi_Giunta.zip"

tmp_folder=$(mktemp -d --tmpdir=.)

mkdir ${tmp_folder}/${folder_name} 

cp -rl Relazione.pdf graphs html ProgettoSocCom1.ipynb data/twitter_data.json ${tmp_folder}/${folder_name}

pushd $tmp_folder
zip -r ../${archive_name} ${folder_name}
popd

rm -rf ${tmp_folder}
