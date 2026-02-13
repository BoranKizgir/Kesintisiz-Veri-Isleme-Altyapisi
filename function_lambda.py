Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... import boto3
... 
... s3 = boto3.client('s3')
... 
... def lambda_handler(event, context):
...     # SQS'ten gelen her bir mesaj için döngü
...     for record in event['Records']:
...         # SQS mesajının içindeki S3 bilgilerini parse etme
...         body = json.loads(record['body'])
...         
...         # S3 event notification bazen test mesajı atabilir, kontrol edelim
...         if 'Records' not in body:
...             print("Test mesajı alındı, atlanıyor...")
...             continue
...             
...         for s3_record in body['Records']:
...             bucket_name = s3_record['s3']['bucket']['name']
...             file_key = s3_record['s3']['object']['key']
...             
...             print(f"İşleniyor: Bucket: {bucket_name}, Dosya: {file_key}")
...             
...             # BURADA: Gerçek projede resmi boyutlandırma kodu olurdu.
...             # Şimdilik sadece dosyanın metadata'sına "islenmis: true" ekleyelim.
...             print(f"Başarıyla işlendi: {file_key}")
...             
...     return {
...         'statusCode': 200,
...         'body': json.dumps('İşlem başarıyla tamamlandı!')
