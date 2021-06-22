import mysql.connector
import json

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "thingiverse"
)

cursor = db.cursor()

# with open('../users.json') as f:
#     users = json.load(f)
# for user in users["hits"]:
#     sql = "INSERT INTO user_homepage (user_id,username ,firstName,lastName,numOfFollowers ,numOfFollowing,numOfDesigns)"\
#           " VALUES  (%s,%s,%s,%s,%s,%s,%s);"
#     val = (user["id"],user["name"],user["first_name"],user["last_name"],user["count_of_followers"],user["count_of_following"],user["count_of_designs"])
#     # print(val)
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("-------------------------------")
#
#
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     sql = "INSERT INTO user_details (user_id,username ,location,about, skill, numOfFavourites,numOfLikes, numOfMakes, numOfCollections,dateRegistered)"\
#           " VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     val = (user["id"],user["name"],user["location"],user["bio"],user["skill_level"],
#            user["favorite_count"],user["like_count"],user["make_count"],user["collection_count"],user["registered"])
#     # print(val)
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("-------------------------------")


with open('../user_details.json') as f:
    users = json.load(f)
for user in users:
    usre_id = user["id"]
    for type in (user["types"]):
        sql = "INSERT INTO status (status_id, user_id, statusName)" \
              " VALUES  (%s,%s,%s);"
        val = (type["id"],user["id"],type["name"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
db.commit()
print("-------------------------------")


with open('../user_details.json') as f:
    users = json.load(f)
for user in users:
    usre_id = user["id"]
    for printer in (user["printers"]):
        sql = "INSERT INTO printers (printer_id, user_id, printerName, printerUrl)" \
              " VALUES  (%s,%s,%s,%s);"
        val = (printer["id"],user["id"],printer["name"], printer["public_url"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
db.commit()
print("-------------------------------")

with open('../user_details.json') as f:
    users = json.load(f)
for user in users:
    usre_id = user["id"]
    for program in (user["programs"]):
        sql = "INSERT INTO programs (program_id, user_id, programName)" \
              " VALUES  (%s,%s,%s);"
        val = (program["id"],user["id"],program["name"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
db.commit()
print("-------------------------------")

with open('../user_details.json') as f:
    users = json.load(f)
for user in users:
    usre_id = user["id"]
    for group in (user["groups"]):
        sql = "INSERT INTO group_names (group_id, user_id, groupName, groupUrl)" \
              " VALUES  (%s,%s,%s,%s);"
        val = (group["id"],user["id"],group["name"], group["public_url"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
db.commit()
print("-------------------------------")


