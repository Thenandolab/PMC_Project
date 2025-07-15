#!/bin/bash

subjects=("100307" "102311" "115017" "118831" "120010" "121719" "122822" "128127" 
          "133625" "135528" "144832" "146129" "147636" "147737" "148032" "148133" 
          "150625" "150726" "151021" "151223" "151324" "151728" "158338" "162228" 
          "162935" "183337" "185846" "202113" "283543" "286347" "322224" "392447" 
          "557857" "715647" "774663" "832651" "878877" "987983" "993675" "996782")

for subject in "${subjects[@]}"
do
  cd /Users/nando/Desktop/HCP/subjects/$subject/code

  # Ensure the script is executable
  chmod +x filter_tractography_by_roi.sh
  ./filter_tractography_by_roi.sh
  
  ipython create_wmc.py
  ipython convert_tck2trk.py
  ipython streamline_count_ROI.py
done
