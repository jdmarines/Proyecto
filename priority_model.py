import joblib

# Carga modelo si es necesario
model = joblib.load("models/priority_model.pkl")

def predict_priority(text):
    # Preprocesa y predice
    return model.predict([text])[0]
