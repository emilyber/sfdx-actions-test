from datetime import datetime,timedelta
import json

data_hora_atual = datetime.now() - timedelta(hours=3,minutes=00)
hora = data_hora_atual.hour
print(data_hora_atual)
print(hora)

# 2022-06-24T12:02:000Z

jsonFile= {
  "totalSize" : 3,
  "done" : "true",
  "records" : [ {
    "attributes" : {
      "type" : "Account",
      "url" : "/services/data/v53.0/sobjects/Account/0010b00002VTDj4AAH"
    },
    "CreatedDate" : "2020-02-18T00:21:42.000+0000",
    "Id" : "0010b00002VTDj4AAH",
    "Name" : "Bluebeards Grog House"
  }, {
    "attributes" : {
      "type" : "Account",
      "url" : "/services/data/v53.0/sobjects/Account/0010b00002VTEfHAAX"
    },
    "CreatedDate" : "2020-02-18T09:17:28.000+0000",
    "Id" : "0010b00002VTEfHAAX",
    "Name" : "Terrago Bulk Company"
  }, {
    "attributes" : {
      "type" : "Account",
      "url" : "/services/data/v53.0/sobjects/Account/0010b00002VTEfIAAX"
    },
    "CreatedDate" : "2020-02-18T09:17:28.000+0000",
    "Id" : "0010b00002VTEfIAAX",
    "Name" : "Idealis Bulk Company"
  } ]
}


conv_to_json = json.dumps(jsonFile)
print(conv_to_json)

l = len(jsonFile['records'])
print("conteudo de records: ", l)
last_param= jsonFile['records'][l-1]

print("Ultimo parametro do json:" , last_param)
entrance_hour = 10

create_date = datetime.strptime(last_param["CreatedDate"], "%Y-%m-%dT%H:%M:%S.%f%z")
print("created date:", create_date ," /hora: ", create_date.hour)
print("teste", l)
print(jsonFile["totalSize"])
resp = get_values(jsonFile,create_date,entrance_hour)

print("resp:" , resp)

def get_values(jsonFile, create_date, entrance_hour):
  limit=5
  while (create_date.hour < entrance_hour and jsonFile["totalSize"] > 0) : 
      if limit == 0:
        return jsonFile
        break
      
      limit = limit -1
      print(create_date.hour < entrance_hour)
      print(jsonFile["totalSize"] > 0)
      print(limit ==0)
      print("passa para a consulta a nova hora", limit)
      

