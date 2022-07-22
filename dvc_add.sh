#!/usr/bin/bash
#!/usr/local/bin/bash

declare -A model_names=(
  ['catboost']="baseline ext_text_process labse_emb"
  ['keras']="labse_emb"
)
git add notebooks
git add submissions
dvc add data
for model_name in ${!model_names[@]}; do
  for experiment_name in ${model_names[$model_name]}; do
    git add submissions/$model_name/$experiment_name.csv
    dvc add oof_pred/$model_name/$experiment_name.pkl
    dvc add test_pred/$model_name/$experiment_name.pkl
    dvc add checkpoints/$model_name/$experiment_name
  done
done

