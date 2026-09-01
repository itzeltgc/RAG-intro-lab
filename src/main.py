from preprocess import prepare_data

DATASET_PATH = r'/Users/itzeltgc/Documents/DataScienceGirlypop/Courses/RAG_intro/data/all-data.csv'

records = prepare_data(DATASET_PATH)

print(f"✅ Ingesta completada con éxito.")
print(f"📊 Total de noticias procesadas: {len(records)}")
print(f"🔍 Muestra del primer registro: {records[0]}")