# Kidney-Disease-Classification-DVC-MLFlow

## Workflows
1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/SUMITDHAKAD0/Kidney-Disease-Classification-DVC-MLFlow.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n envname python=3.8 -y
```

```bash
conda activate envname
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command 
python main.py
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

