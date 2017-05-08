import psycopg2
myConnection = psycopg2.connect(port="6773",host="51.140.33.76", user="dev001", password="EV5gy2pQPDhC4H&fg3$5qzWL*9P4=D2K8ta9x&Qr2", dbname="testdb")
cur = myConnection.cursor()

dict_data = {}

cur.execute("SELECT attname FROM pg_attribute,pg_class WHERE attrelid=pg_class.oid AND relname='tbl_profiles' AND attstattarget <>0;")
dict_data["tbl_profiles_names"] = cur.fetchall()

cur.execute("SELECT attname FROM pg_attribute,pg_class WHERE attrelid=pg_class.oid AND relname='tbl_due_listing' AND attstattarget <>0;")
dict_data["tbl_due_listing_names"] = cur.fetchall()

cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = 'tbl_profiles';")
dict_data["tbl_profiles_properties"] = cur.fetchall()

cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = 'tbl_due_listing';")
dict_data["tbl_due_listing_properties"] = cur.fetchall()

cur.execute( "SELECT * FROM tbl_profiles;")
dict_data["list_tbl_profiles"] = cur.fetchall()

cur.execute( "SELECT * FROM tbl_due_listing;")
dict_data["list_tbl_due_listing"] = cur.fetchall()

cur.execute("SELECT * FROM pg_catalog.pg_tables;")
dict_data["list_database_table_properties"] = cur.fetchall()

myConnection.close()

print "Using psycopg2...\n"

Titles = {"tbl_profiles_names" : "Names for fields in table tbl_profiles", "tbl_due_listing_names" : "Names for fields in table tbl_due_listing", "tbl_profiles_properties" : "Properties for table tbl_profiles", "tbl_due_listing_properties" : "Properties for tbl_due_listing", "list_tbl_profiles" : "Values for table tbl_profiles", "list_tbl_due_listing" : "Values for table tbl_due_listing", "list_database_table_properties" : "Tables"}
for keys, values in dict_data.items():
    print Titles[keys]
    for each in values:
        print each
    print "\n\n\n\n\n"
