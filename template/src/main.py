def test_container():
    from sklearn import datasets
    from sklearn import svm

    iris = datasets.load_iris()
    digits = datasets.load_digits()
    print(digits.data)

    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(digits.data[:-1], digits.target[:-1])
    print(clf.predict(digits.data[-1:]))

if __name__=="__main__":
    test_container()