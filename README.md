# KNU_ResNet18
### Hydra template


In order to find the optimal batch size and lr, Hydra template is used to maximize the effect of the experiment.

Hydra Template Reference : https://github.com/ashleve/lightning-hydra-template

#### train
python src/train.py

python src/train.py -m hparams_search=cifat10_resnet18_optuna experiment=example  
(you can automatically train once for batch size and lr)

#### The results can be checked through the Wandb report.

https://api.wandb.ai/links/limseu0875/tmkndkjp
---
### Base line code
python main.py

python ensemble.py



