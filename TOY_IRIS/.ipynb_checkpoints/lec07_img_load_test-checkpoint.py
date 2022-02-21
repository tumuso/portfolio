import matplotlib.image as img
import matplotlib.pyplot as plt

fileName = "./logo.png"
ndarray = img.imread(fileName)
plt.imshow(ndarray)
plt.show()

from sklearn.metrics import confusion_matrix, f1_score
정답지 = df["target"]
문제지 = df.drop(["target"],axis=1)

f1_score(y_val, pred, average='binary')

confusion_matrix()
model = RandomForestClassifier(random_state=1414)
from sklearn.metrics import confusion_matrix
# from IPython.display import Image
# Image(filename = './logo.png')

