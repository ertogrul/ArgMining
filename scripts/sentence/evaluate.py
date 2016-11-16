import argparse
from argmining.sentence.loaders.THF_sentence_corpus_loader import load_dataset
import time
from sklearn.model_selection import GridSearchCV
import logging
import json
from argmining.pipelines.pipeline import pipeline
from argmining.strategies.strategies import STRATEGIES
from argmining.classifiers.classifier import get_classifier
from collections import OrderedDict

NJOBS = 1


def config_argparser():
    argparser = argparse.ArgumentParser(description='ArgMining')
    argparser.add_argument('-configfile', type=str, required=True, help='Name of the subtask')
    return argparser.parse_args()


if __name__ == '__main__':
    t0 = time.time()
    logger = logging.getLogger()
    arguments = config_argparser()
    # 1) Read settings file
    logger.info("Loading config file: {}".format(arguments.configfile))
    with open(arguments.configfile) as data_file:
        settings = json.load(data_file)
    # 2) Read datasets
    X_train, y_train = load_dataset(file_path='data/THF/sentence/subtask{}_train.json'.format(settings['subtask']))
    X_test, y_test = load_dataset(file_path='data/THF/sentence/subtask{}_test.json'.format(settings['subtask']))
    # 3) Load classifier with arguments
    # 4) Load features and set arguments
    # 5) Train classifier
    # 6) Predict the test set
    # 7) Print the confusion matrix
    # 8) Save the prediction into the file system

    logger.info("Total execution time in %0.3fs" % (time.time() - t0))
    logger.info("*****************************************")
