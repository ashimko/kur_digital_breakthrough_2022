#!/usr/local/bin/bash
#!/usr/bin/bash

declare -A model_names=(
  ['catboost']="baseline"
)

for model_name in ${!model_names[@]}; do
  for experiment_name in ${model_names[$model_name]}; do
    git add submissions/$model_name/$experiment_name.csv
    dvc add oof_pred/$model_name/$experiment_name.pkl
    dvc add test_pred/$model_name/$experiment_name.pkl
    dvc add checkpoints/$model_name/$experiment_name
  done
done

