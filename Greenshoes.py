import psycopg2
myConnection = psycopg2.connect(port="6773",host="51.140.33.76", user="dev001", password="EV5gy2pQPDhC4H&fg3$5qzWL*9P4=D2K8ta9x&Qr2", dbname="testdb")
cur = myConnection.cursor()

cur.execute("SELECT attname FROM pg_attribute,pg_class WHERE attrelid=pg_class.oid AND relname='tbl_profiles' AND attstattarget <>0;")
tbl_profiles_names = cur.fetchall()

cur.execute("SELECT attname FROM pg_attribute,pg_class WHERE attrelid=pg_class.oid AND relname='tbl_due_listing' AND attstattarget <>0;")
tbl_due_listing_names = cur.fetchall()

cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = 'tbl_profiles';")
tbl_profiles_properties = cur.fetchall()

cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = 'tbl_due_listing';")
tbl_due_listing_properties = cur.fetchall()

cur.execute( "SELECT * FROM tbl_profiles;")
list_tbl_profiles = cur.fetchall()

cur.execute( "SELECT * FROM tbl_due_listing;")
list_tbl_due_listing = cur.fetchall()

cur.execute("SELECT * FROM pg_catalog.pg_tables;")
list_database_table_properties = cur.fetchall()

myConnection.close()

print "Using psycopg2...\n"

print "Names for fields in table tbl_profiles"
for all in tbl_profiles_names:
    print all 
print "\n\n\n\n\n"

print "Names for fields in table tbl_due_listing"
for all in tbl_due_listing_names:
    print all 
print "\n\n\n\n\n"

print "Properties for table tbl_profiles"
for all in tbl_profiles_properties:
    print all 
print "\n\n\n\n\n"

print "Properties for tbl_due_listing"
for all in tbl_due_listing_properties:
    print all 
print "\n\n\n\n\n"

print "Values for table tbl_profiles"
for all in list_tbl_profiles:
    print all 
print "\n\n\n\n\n"

print"Values for table tbl_due_listing"
for all in list_tbl_due_listing:
    print all 
print "\n\n\n\n\n"

print "Tables"
for all in list_database_table_properties:
    print all[1]
