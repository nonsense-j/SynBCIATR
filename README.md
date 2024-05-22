# SynBCIATR

### Introduction
This repository hosts the codes and data for the paper "Fix the Tests: Augmenting LLMs to Repair Test Cases with Static Collector and Neural Reranker", which has been submitted to ISSRE 2024. The work introduces SynBCIATR for automated test repair using Language Models, where it augments LLM's capability by constructing precisely related contexts with static analysis and reranking.

### Approaches Overview
- **SynBCIATR**: A novel test repair approach with contexts based on LLMs. Running script: `run_update_ctx.py`.
- **NaiveLLM** (baseline): A naive test repair approach without contexts based on LLMs. Running script: `run_update_woctx.py`.
- **CEPROT** (baseline): A SOTA test repair approach without contexts based on CodeT5, which we replicate elsewhere. In this repository, we only provide the results of CEPROT.

### Repository Contents
- `dataset`: The benchmark dataset used for evaluating SynBCIATR against baselines.
- `logs`: Logs when running scripts.
- `outputs`: The output results of approaches and evaluation.
- `retriever`: The source codes of retriever for SynBCIATR, which is used to retrieve related contexts.
- `utils`: The source codes of utilities for SynBCIATR, which provides abilities of parser, formatter configs and etc. 
- `README.md`: This file.
- ***Jupyter Notebooks***: 
  - `dataset_setup.ipynb`: The notebook for setting up projects in the datasets (Before running SynBCIATR, all the projects should be downloaded locally).
  - `human_eval.ipynb`: The notebook for assisting human evaluation.
- ***Running Scripts***:
  - `run_update_ctx.py`: The script for running SynBCIATR.
  - `run_update_woctx.py`: The script for running NaiveLLM.
  - `run_evaluate.py`: The script for evaluation (RQ1) on CodeBLEU, DiffBLEU, and Accuracy.

### Run SynBCIATR

We provide a sample for testing SynBCIATR in `dataset/test_part.json`. By default, the scripts will repair the test case in `dataset/test_part.json`. Before running the scripts, make sure the environment has been set up correctly.

- Install the required packages (recommended to use a virtual environment):

  ```bash
  pip install -r requirements.txt
  ```

- Install [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html) locally.

- Download the Reranker Model ([bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3/tree/main))

- Add your custom configs in `utils/configs.py`.

- Download the repository locally for the dataset. Since we use `test_part.json` as the test dataset, we only need to download the corresponding project: Alluxio/Alluxio. You can finish this by `dataset_setup.ipynb`.

- Run SynBCIATR:

  ```bash
  python run_update_ctx.py
  ```
  The results will be saved in `outputs/SynBCIATR/test_part_all_ctx_wot.json`. The log is generated in `logs/run_update_ctx.log` (we also retain backups for reference). 

- Run NaiveLLM (optionally)
  ```bash
  python run_update_woctx.py
  ```
  The results will be saved in `outputs/NaiveLLM/test_part_woctx.json`. The log is in `logs/run_update_woctx.log` (we also retain backups for reference). 

- Notes: Due to the limitation of *multilsp*, the language server sometimes may not be correctly closed as expected. Therefore, remember to check it after running the script of SynBCIATR.
  ```bash
  # check
  ps aux | grep 'language_servers' | grep -v grep
  # kill
  ps aux | grep 'language_servers' | grep -v grep | awk '{print $2}' | xargs kill
  ```