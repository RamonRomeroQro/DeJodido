'''
$directory = "../path/to/photos_directory/";

$images = glob($directory . "*.jpg");

foreach($images as $image)
{
    $name = explode('_',$image);
    $name = 'photos/' . $name[0];
    $sql = mysql_query("SELECT id FROM table WHERE photo1='$name' OR photo2='$name'");
    if(mysql_num_rows($sql) == 0)
        unlink($directory . $image);
}
'''

import os
import psycopg2


# Open a file
path = "./media/imagen"
dirs = os.listdir( path )

# This would print all the files and directories
exist=[]
for file in dirs:
   f='imagen/'+file
   exist.append(f)


#!/usr/bin/python2.4
#
# Small script to show PostgreSQL and Pyscopg together
#


try:

    conn = psycopg2.connect("dbname='deajodido' user='postgres' host='localhost' password='postgres'")

    cur = conn.cursor()

    for f in exist:
        cur.execute("SELECT imagen from lugares_imagen WHERE imagen='"+f+"'")
        rows = cur.fetchall()
        if (len(rows)) == 0:
            print ('no en base datos ' + f + ' BORRAR')
            os.remove('./media/'+f)

        else:
            for row in rows:
                print ('si en base de datos '+ row [0]+ '  vs  ' + f +' NO BORRAR')



except Exception as e:
    print (str(e)+'\n')

    print ('no')