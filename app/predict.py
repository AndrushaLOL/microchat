import pickle
import os


def predict(x):
    """
    :param x: array shape [4] - input for model
    :return: scalar - predicted class of iris
    """
    path_to_model = os.path.join(os.path.dirname(__file__), 'ml', 'model.pkl')
    with open(path_to_model, 'rb') as f:
        model = pickle.loads(f.read())
        preds = model.predict([x])
    return preds[0]

print(predict([1, 10, 3, 4]))