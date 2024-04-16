import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.008
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: False
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '0.5*math.log((1-p)/p)'

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.5275
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = "No"

    # type: explain_string
    answers['Explain'] = "Alan's coin-flipping method doesn't offer a true prediction; it's random with no actual insight into the stock market. Effective ensemble methods require models with real predictive power, not chance"
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "no"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Both classifiers C1 and C2 have their TPR equal to their FPR, which means they both lie on the random guess line of an ROC curve and neither is better than the other."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "Classifier C2 is preferred for its superior recall, yet this overlooks the issue of false positives. Considering both true positive and false positive rates provides a more comprehensive evaluation, particularly when the presence of false positives is a concern."

    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 is the better classifier among the two because it has a higher F1-measure, indicating a better balance between precision and recall. While C1 has a lower FPR, it significantly sacrifices recall, leading to many positive instances going undetected."


    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "The precision-recall-F1-Measure is the appropriate metric pair as it accounts for the balance between the classifier’s ability to correctly identify positive cases and its precision, i.e., how many of the positive predictions were actually positive. It is particularly important when dealing with imbalanced classes or when both false positives and false negatives carry a significant cost."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3"

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C3 is the preferred classifier because it offers the highest precision, which means it is most accurate when it predicts a positive class. Its F1-measure is also better than C1’s, indicating a better balance between precision and recall than C1 and a similar FPR. While C2 has a higher recall, its FPR is significantly higher, which might be costly depending on the application."

    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = "1/10"

    # type: eval_float
    answers['(a) recall for C0'] = "p"

    # type: eval_float
    answers['(b) F-measure of C0'] = "(2 * p/10)/(p + 1/10)" 

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = "unknown"

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] = {
        'recall': 0.533,  
        'precision': 0.615, 
        'F-measure': 0.571,  
        'accuracy': 0.88 }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = "F-measure"

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = "accuracy"

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "The F-measure is the best metric because it combines both precision and recall, providing a balanced view of the classifier's performance on the positive class, which is crucial in the context of imbalanced classes. Accuracy is the worst metric in this scenario because it can be misleading in the presence of imbalanced class distributions; a high accuracy might not reflect true predictive performance on the less frequent class."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "F1"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The F1 measure is generally more appropriate when the costs of false positives and false negatives are comparable and when there is an interest in maintaining a balance between precision and recall."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In a scenario where the disease is rare, the cost of unnecessary treatment from false positives is high,or the psychological impact of false positives is severe, the TPR/FPR ratio would be preferred to reduce false alarms. Conversely, in a scenario where failing to detect the disease is significantly risky, the F1 score would be prioritized to ensure a balanced approach to identifying true positives."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
