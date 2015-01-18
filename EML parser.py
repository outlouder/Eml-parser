import os
import re

from eml_parser import eml_parser
from email import utils

for files in os.listdir('.'):
    if files[-3:] == "eml":

        m = eml_parser.decode_email(files,include_attachment_data=True)
        date= m['header']['date']
        #dateraw = m['header']['x-received']
        #dateraw1 = dateraw.split(";",1)[1]

        #year = utils.parsedate_tz(dateraw1)[0]
        #month = utils.parsedate_tz(dateraw1)[1]
        #day = utils.parsedate_tz(dateraw1)[2]

        #date =  "%d-%d-%d" % (year,month,day)
        exp= m['header']['from']
        dest= m['header']['to']
        subject = m['header']['subject'] 

        print date.strftime("%Y-%m-%d")+' '+exp+' '+dest[0]+' ('+subject+')'
