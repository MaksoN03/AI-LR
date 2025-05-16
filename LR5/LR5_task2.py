import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# 1. Завантаження даних
df = pd.read_csv(r'D:\renfe_small.txt')

# 2. Попередня обробка
df = df.dropna(subset=['price'])  # Видаляємо рядки без ціни
df['price'] = df['price'].astype(float)

# 3. Класифікація ціни
def categorize_price(price):
    if price < 30:
        return 'низька'
    elif price < 60:
        return 'середня'
    else:
        return 'висока'

df['price_class'] = df['price'].apply(categorize_price)

# 4. Кодування категоріальних змінних
features = ['origin', 'destination', 'train_type', 'train_class', 'fare']
X = df[features]
y = df['price_class']

encoders = {col: LabelEncoder() for col in features}
for col in features:
    X.loc[:, col] = encoders[col].fit_transform(X[col])

label_encoder_y = LabelEncoder()
y_encoded = label_encoder_y.fit_transform(y)

# 5. Розбиття на train/test
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# 6. Модель Наївного Байєса
model = CategoricalNB()
model.fit(X_train, y_train)

# 7. Оцінка
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=label_encoder_y.classes_))
