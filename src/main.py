import pandas as pd

#from sklearn.naive_bayes import MultinomialNB

# Загружаем базу данных

df = pd.read_csv(
    "data/SMSSpamCollection.csv",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Размер таблицы
#print("Размер базы", df.shape)

#model = MultinomialNB()