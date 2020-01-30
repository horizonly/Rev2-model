# Rev2-model
Repetition code and bug patch

This folder contains the data and code for the paper "REV2: Fraudulent User Prediction in Rating Platforms", published at WSDM 2018.
This readme file contains the description of the codes and the data files.
The project website is at: https://cs.stanford.edu/~srijan/rev2/

Please cite the paper if you use the data or code in your research:
@inproceedings{kumar2018rev2,
  title={Rev2: Fraudulent user prediction in rating platforms},
  author={Kumar, Srijan and Hooi, Bryan and Makhija, Disha and Kumar, Mohit and Faloutsos, Christos and Subrahmanian, VS},
  booktitle={Proceedings of the Eleventh ACM International Conference on Web Search and Data Mining},
  pages={333--341},
  year={2018}, 321、
  organization={ACM}
}

************** Debug ******************

Add requirements.txt

Transform python2 to python3

import detect ---> from chardet import detect

inconsistent indentation problem:maybe this problem only in pycharm

Fill in missing sections and comment

Add formula annotation

************** DATA ******************

The data folder has 4 dataset folders, one for each dataset: alpha, otc, amazon, and epinions. We are unable to release similar data for the Flipkart network used in the paper as it is under a non-disclosure agreement.

Each dataset folder has the following data files:
data_network.csv: This is the original network. Format is: source id, destination id, edge weight, timestamp 
data_gt.csv: This is the file with the ground truth labels. Format is: node id, label (+1 (benign) or -1 (fraudulent)).

We also provide processed files that we use in the code:
data_network.pkl: This is the pickle file of the data_network.csv file, created for faster access.
data_birdnest_user.pkl: This is the BIRDNEST anomaly score given to each user (edge generator) by running the BIRDNEST algorithm (Hooi et al., SDM 2016).
data_birdnest_product.pkl: This is the BIRDNEST anomaly score given to each product (edge recipient) by running the BIRDNEST algorithm (Hooi et al., SDM 2016).
data_edge_birdnest.pkl: This is the BIRDNEST anomaly score for each edge (rating)
data_edge_map.pkl: This is the mapping between the edges in the network and the scores


************** CODE *******************

The code folder has the following files:
rev2code.py: This is the main file that runs the rev2 algorithm for an input parameter setting. It outputs a fairness score and goodness score for each node. 
run-rev2-all-params.sh: This file runs rev2 on all combinations of input parameter settings. 
evaluate-individual.py: This file calculates the average precision score for fraudulent and benign user prediction. This uses the output of the rev2 code for one parameter setting.
evaluate-combined.py: This file calculates the mean average precision score for fraudulent and benign user prediction. This uses the outputs of the rev2 code for all parameter settings.
evaluate-combined-supervised.py: This file calculates the AUC score for the fraudulent user prediction. This uses all outputs of the rev2 code for all parameter settings. 



