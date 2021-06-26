import mysql.connector
import json
import csv

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database = "thingiverse"
)

cursor = db.cursor()

# # user_homepage
# with open('../users.json') as f:
#     users = json.load(f)
# for user in users["hits"]:
#     sql = "INSERT INTO user_homepage (user_id,username ,firstName,lastName,numOfFollowers ,numOfFollowing,numOfDesigns, url)"\
#           " VALUES  (%s,%s,%s,%s,%s,%s,%s,%s);"
#     val = (user["id"],user["name"],user["first_name"],user["last_name"],user["count_of_followers"],user["count_of_following"],user["count_of_designs"],
#     user["public_url"])
#     # print(val)
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("-------------------------------")
#
#
# #user_details
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     sql = "INSERT INTO user_details (user_id,username ,location,about, skill, numOfFavourites,numOfLikes, numOfMakes, numOfCollections,dateRegistered)"\
#           " VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     val = (user["id"],user["name"],user["location"],user["bio"], user["skill_level"],
#            user["favorite_count"],user["like_count"],user["make_count"],user["collection_count"],user["registered"])
#     # print(val)
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("-------------------------------")
#
# #social_media_chanels
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     if (user["twitter"]):
#         sql = "INSERT INTO user_social_media_channels (user_id, website, twitter_account_name, twitter_url)" \
#               " VALUES  (%s,%s,%s,%s);"
#         val = (user["id"],user["website"],user["twitter"]["account_name"], user["twitter"]["account_url"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
#     else:
#         sql = "INSERT INTO user_social_media_channels (user_id, website, twitter_account_name, twitter_url)" \
#               " VALUES  (%s,%s,%s,%s);"
#         val = (user["id"], user["website"], None, None)
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
#
# db.commit()
# print("-------------------------------")
#
#
# #status
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     usre_id = user["id"]
#     for type in (user["types"]):
#         sql = "INSERT INTO user_status (status_id, user_id, statusName)" \
#               " VALUES  (%s,%s,%s);"
#         val = (type["id"],user["id"],type["name"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("-------------------------------")
#
#
# #printers
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     usre_id = user["id"]
#     for printer in (user["printers"]):
#         sql = "INSERT INTO user_printers (printer_id, user_id, printerName, printerUrl)" \
#               " VALUES  (%s,%s,%s,%s);"
#         val = (printer["id"],user["id"],printer["name"], printer["public_url"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("-------------------------------")
#
#
# #programs
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     usre_id = user["id"]
#     for program in (user["programs"]):
#         sql = "INSERT INTO user_programs (program_id, user_id, programName)" \
#               " VALUES  (%s,%s,%s);"
#         val = (program["id"],user["id"],program["name"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("user_homepage-------------------------------")
#
#
# #groups
# with open('../user_details.json') as f:
#     users = json.load(f)
# for user in users:
#     usre_id = user["id"]
#     for group in (user["groups"]):
#         sql = "INSERT INTO user_group_names (group_id, user_id, groupName, groupUrl)" \
#               " VALUES  (%s,%s,%s,%s);"
#         val = (group["id"],user["id"],group["name"], group["public_url"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("user_details-------------------------------")
#
# #designs
# with open('../designs.json') as f:
#     designs = json.load(f)
# for design in designs:
#     sql = "INSERT INTO designs (design_id, user_id, title, numOfComments, numOfLikes,url,dateCreated)" \
#                       " VALUES  (%s,%s,%s,%s,%s,%s,%s);"
#     val = (design["id"], design["creator"]["id"], design["name"], design["comment_count"], design["like_count"], design["public_url"], design["created_at"])
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("designs-------------------------------")
#
#
# #design_details
# with open('../things/things.json') as f:
#     things = json.load(f)
# for thing in things:
#     sql = "INSERT INTO design_details (design_id, user_id, title, numOfFiles, numOfMakes,numOfRemixTo, numOfApps," \
#             "numOfDownloads, numOfViews, summary, instructions, licence, category_url, files_url,image_url)"\
#            " VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
#     val = (thing["id"], thing["creator"]["id"],thing["name"],thing["file_count"], thing["make_count"],
#           thing["remix_count"], thing["app_count"],thing["download_count"], thing["view_count"],
#           thing["description"], thing["instructions"], thing["license"], thing ["categories_url"],
#           thing["files_url"], thing["images_url"])
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("thing_details-------------------------------")
#
# #tags
# with open('../designs.json') as f:
#     designs = json.load(f)
# for design in designs:
#     for tag in (design["tags"]):
#         sql = "INSERT INTO tags(name, design_id, tagName, url)" \
#               " VALUES  (%s,%s,%s,%s);"
#         val = (tag["name"],design["id"],tag["tag"],tag["absolute_url"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("tags-------------------------------")
#
# #tcategories
# with open('../catagories.json') as f:
#     categories = json.load(f)
# for catagory in categories:
#       sql = "INSERT INTO categories (category_id, design_id, name, count, slug)" \
#             " VALUES  (%s,%s,%s,%s,%s);"
#       val = (catagory["id"], catagory["design_id"], catagory["name"], catagory["count"], catagory["slug"])
#       cursor.execute(sql, val)
#       print(cursor.rowcount, "record inserted.")
# db.commit()
# print("categories-------------------------------")
# #
# #
# with open('../root_comment.json') as f:
#     comments = json.load(f)
# for comment in comments:
#     sql = "INSERT INTO design_root_comments(comment_id, design_id, user_id, username, comment, datePosted)" \
#           " VALUES  (%s,%s,%s,%s,%s,%s);"
#     if comment["user"]:
#         val = (comment["id"],comment["target_id"],comment["user"]["id"],comment["user"]["name"],comment["body"],comment["added"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
#     else:
#         val = (comment["id"], comment["target_id"], None, None, comment["body"],
#                comment["added"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("comments-------------------------------")
#
# with open('../replies.json') as f:
#     replies = json.load(f)
# for reply in replies:
#     sql = "INSERT INTO design_comment_replies(reply_id, parent_comment_id, design_id, user_id, username, comment, datePosted)" \
#           " VALUES  (%s,%s,%s,%s,%s,%s,%s);"
#     if reply["user"]:
#         val = (reply["id"], reply["parent_id"],reply["target_id"],reply["user"]["id"],reply["user"]["name"],reply["body"],reply["added"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
#     else:
#         val = (reply["id"], reply["parent_id"], reply["target_id"], None, None, reply["body"],
#                reply["added"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("replies-------------------------------")
#
# #remix_from
# with open('../things/things.json') as f:
#     things = json.load(f)
# for thing in things:
#     for ancestor in (thing["ancestors"]):
#         sql = "INSERT INTO remix_from(remix_from_id, design_id)" \
#               " VALUES  (%s,%s);"
#         val = (ancestor["id"], thing["id"])
#         cursor.execute(sql, val)
#         print(cursor.rowcount, "record inserted.")
# db.commit()
# print("remix_from-------------------------------")
#
# #remix_to
# with open('../remixto.json') as f:
#     remixes = json.load(f)
# for  remix in remixes:
#     sql = "INSERT INTO remix_to(remix_to_id, design_id)" \
#           " VALUES  (%s,%s);"
#     val = (remix["id"], remix["design_id"])
#     cursor.execute(sql, val)
#     print(cursor.rowcount, "record inserted.")
# db.commit()
# print("remix_from-------------------------------")

#makes
with open('../copies.json') as f:
    makes = json.load(f)
for make in makes:
    sql = "INSERT INTO makes(make_id, source_thing_id, made_by_id, made_by_name, title, description, datePosted, numOfLikes, numOfComments)" \
          " VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    if make["maker"] and make["thing"]:
        val = (make["id"],make["thing"]["id"], make["maker"]["id"], make["maker"]["name"], make["thing"]["name"],
               make["description"], make["added"], make["like_count"], make["comment_count"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
    else:
        val = (make["id"], None, None, None, None,
               make["description"], make["added"], make["like_count"], make["comment_count"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
db.commit()
print("makes-------------------------------")

with open('../make_details.csv', newline='') as csvfile:
    make_details = csv.DictReader(csvfile)
    for  make in make_details:
        sql = "INSERT INTO make_details(make_id,numOfShares, numOfViews, category, printerBrand" \
              ",printer, rafts, supports, resolution, infill, filament, sourceLikes, sourceCollects, sourceComments)" \
              " VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        val = (make["make_id"], make["shares"], make["views"], make["category"], make["printerBrand"],make["printer"],
                 make["rafts"], make["support"], make["resoulution"], make["infill"], make["filament"],
                 make["sourceLikes"], make["sourceCollects"], make["sourceComments"])
        cursor.execute(sql, val)
        print(cursor.rowcount, "record inserted.")
db.commit()

print("make_details-------------------------------")
