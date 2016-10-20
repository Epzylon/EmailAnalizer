#/usr/bin/env python
import argparse
from email import message_from_file as open_efile
from TokenAnalizer.Trace.received import Received


pname = 'emailanalizer'
pdesc = "Analize email headers"

parser = argparse.ArgumentParser(description=pdesc,prog=pname)

parser.add_argument('-T','--tracert',help="Show the trace path of the email")
parser.add_argument('-f','--file',dest='mail_file',
                    action='store',help='Email file')

args = parser.parse_args()

if args.mail_file == None:
    print("You must provide a email file")
    exit(1)
else:
    e = open_efile(open(args.mail_file))
    reclist = e.get_all('Received')
    reclist.reverse()
    for H in reclist:
        r = Received(H)
        print(r)
