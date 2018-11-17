# -*- coding: utf-8 -*-

VERSION = "1.4"


OVERVIEW = '''
PyCM is a multi-class confusion matrix library written in Python that
supports both input data vectors and direct matrix, and a proper tool for
post-classification model evaluation that supports most classes and overall
statistics parameters.
PyCM is the swiss-army knife of confusion matrices, targeted mainly at
data scientists that need a broad array of metrics for predictive models
and an accurate evaluation of large variety of classifiers.
'''

DOCUMENT_ADR = "http://www.shaghighi.ir/pycm/doc/index.html#"

PARAMS_DESCRIPTION = {
    "TPR": "sensitivity, recall, hit rate, or true positive rate",
    "TNR": "specificity or true negative rate",
    "PPV": "precision or positive predictive value",
    "NPV": "negative predictive value",
    "FNR": "miss rate or false negative rate",
    "FPR": "fall-out or false positive rate",
    "FDR": "false discovery rate",
    "FOR": "false omission rate",
    "ACC": "accuracy",
    "F1": "F1 Score - harmonic mean of precision and sensitivity",
    "MCC": "Matthews correlation coefficient",
    "BM": "Informedness or Bookmaker Informedness",
    "MK": "Markedness",
    "LR+": "Positive likelihood ratio",
    "LR-": "Negative likelihood ratio",
    "DOR": "Diagnostic odds ratio",
    "TP": "true positive/hit",
    "TN": "true negative/correct rejection",
    "FP": "false positive/Type 1 error/false alarm",
    "FN": "false negative/miss/Type 2 error",
    "P": "Condition positive or Support",
    "N": "Condition negative",
    "TOP": "Test outcome positive",
    "TON": "Test outcome negative",
    "POP": "Population",
    "PRE": "Prevalence",
    "G": "G-measure geometric mean of precision and sensitivity",
    "RACC": "Random Accuracy",
    "F0.5": "F0.5 Score",
    "F2": "F2 Score",
    "ERR": "Error Rate",
    "RACCU": "Random Accuracy Unbiased",
    "J": "Jaccard index",
    "NIR": "No Information Rate",
    "IS": "Information Score",
    "CEN": "Confusion Entropy",
    "MCEN": "Modified Confusion Entropy",
    "AUC": "Area under the ROC curve",
    "dInd": "Distance index",
    "sInd": "Similarity index",
    "DP":"Discriminant power"}

PARAMS_LINK = {
    "TPR": "TPR--(sensitivity,-recall,-hit-rate,-or-true-positive-rate)",
    "TNR": "TNR-(specificity-or-true-negative-rate)",
    "PPV": "PPV-(precision-or-positive-predictive-value)",
    "NPV": "NPV-(negative-predictive-value)",
    "FNR": "FNR-(miss-rate-or-false-negative-rate)",
    "FPR": "FPR-(fall-out-or-false-positive-rate)",
    "FDR": "FDR-(false-discovery-rate)",
    "FOR": "FOR-(false-omission-rate)",
    "ACC": "ACC-(accuracy)",
    "F1": "FBeta-Score",
    "F0.5": "FBeta-Score",
    "F2": "FBeta-Score",
    "MCC": "MCC-(Matthews-correlation-coefficient)",
    "BM": "BM-(Informedness-or-Bookmaker-Informedness)",
    "MK": "MK-(Markedness)",
    "LR+": "PLR-(Positive-likelihood-ratio)",
    "LR-": "NLR-(Negative-likelihood-ratio)",
    "DOR": "DOR-(Diagnostic-odds-ratio)",
    "TP": "TP-(True-positive-/-hit)",
    "TN": "TN-(True-negative/correct-rejection)",
    "FP": "FP-(False-positive/false-alarm/Type-I-error)",
    "FN": "FN-(False-negative/miss/Type-II-error)",
    "P": "P-(Condition-positive)",
    "N": "N-(Condition-negative)",
    "POP": "POP-(Population)",
    "TOP": "TOP-(Test-outcome-positive)",
    "TON": "TON-(Test-outcome-negative)",
    "G": "G-(G-measure-geometric-mean-of-precision-and-sensitivity)",
    "ERR": "ERR(Error-rate)",
    "RACC": "RACC(Random-accuracy)",
    "RACCU": "RACCU(Random-accuracy-unbiased)",
    "PRE": "PRE-(Prevalence)",
    "Overall_ACC": "Overall_ACC",
    "Kappa": "Kappa-(Nominal)",
    "Overall_RACC": "Overall_RACC",
    "Strength_Of_Agreement(Landis and Koch)": "SOA1-(Strength-of-"
    "Agreement,-Landis-and-Koch-benchmark)",
    "Strength_Of_Agreement(Fleiss)": "SOA2-(Strength-of-"
    "Agreement,-:-Fleiss%E2%80%99-benchmark)",
    "Strength_Of_Agreement(Altman)": "SOA3-(Strength-of-"
    "Agreement,-Altman%E2%80%99s-benchmark)",
    "Strength_Of_Agreement(Cicchetti)": "SOA4-(Strength-of-"
    "Agreement,-Cicchetti%E2%80%99s-benchmark)",
    "TPR_Macro": "TPR_Macro",
    "PPV_Macro": "PPV_Macro",
    "TPR_Micro": "TPR_Micro",
    "PPV_Micro": "PPV_Micro",
    "Scott_PI": "Scott's-pi-(Nominal)",
    "Gwet_AC1": "Gwet's-AC1",
    "Bennett_S": "Bennett-et-al.'s-S-score-(Nominal)",
    "Kappa 95% CI": "Kappa-95%-CI",
    "Kappa Standard Error": "Kappa-95%-CI",
    "Chi-Squared": "Chi-Squared",
    "Phi-Squared": "Phi-Squared",
    "Cramer_V": "Cramer's-V",
    "Chi-Squared DF": "Chi-Squared-DF",
    "95% CI": "95%-CI",
    "Standard Error": "95%-CI",
    "Response Entropy": "Response-Entropy",
    "Reference Entropy": "Reference-Entropy",
    "Cross Entropy": "Cross-Entropy",
    "Joint Entropy": "Joint-Entropy",
    "Conditional Entropy": "Conditional-Entropy",
    "KL Divergence": "Kullback-Liebler-(KL)-divergence",
    "Lambda B": "Goodman-and-Kruskal's-lambda-B",
    "Lambda A": "Goodman-and-Kruskal's-lambda-A",
    "Kappa Unbiased": "Kappa-Unbiased",
    "Overall_RACCU": "Overall_RACCU",
    "Kappa No Prevalence": "Kappa-No-Prevalence",
    "Mutual Information": "Mutual"
                          "-Information",
    "J": "J-(Jaccard-index)",
    "Overall_J": "Overall_J",
    "Hamming Loss": "Hamming-Loss",
    "Zero-one Loss": "Zero-one-Loss",
    "NIR": "NIR-(No-Information-Rate)",
    "P-Value": "P-Value",
    "IS": "IS-(Information-Score)",
    "CEN": "CEN-(Confusion-Entropy)",
    "Overall_CEN": "Overall_CEN",
    "MCEN": "MCEN-(Modified-Confusion-Entropy)",
    "Overall_MCEN": "Overall_MCEN",
    "Overall_MCC": "Overall_MCC",
    "RR": "RR-(Global-Performance-Index)",
    "CBA": "CBA-(Class-Balance-Accuracy)",
    "AUC": "AUC-(Area-Under-The-ROC-Curve)",
    "AUNU": "AUNU",
    "AUNP": "AUNP",
    "sInd": "sInd-(Similarity-Index)",
    "dInd": "dInd-(Distance-Index)",
    "RCI": "Relative-Classifier-Information",
    "DP":"DP-(Discriminant-Power)"}

BENCHMARK_COLOR = {
    "Poor": "Red",
    "Fair": "Orange",
    "Good": "Green",
    "Excellent": "Green",
    "Intermediate to Good": "Green",
    "Substantial": "Green",
    "Almost Perfect": "Green",
    "Moderate": "Green",
    "Slight": "Orange",
    "None": "White",
    "Very Good": "Green"}
