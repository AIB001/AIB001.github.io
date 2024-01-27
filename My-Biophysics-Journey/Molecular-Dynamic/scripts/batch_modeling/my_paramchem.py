# A script to get CGenFF str file. Usage: paramchem.py -u zjuhjx -p abcd1234% -c benzene.mol2
# modified by Xufan Gao
# Usage: scgenff xxx.mol2. try not to add prefix before the file to be uploaded

from xml.dom import minidom
import mechanize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username")
parser.add_argument("-p", "--password")
parser.add_argument("-c", "--conf")
args = parser.parse_args()
# debug
# args = parser.parse_args("-u gxf1212 -p 123465acB% -c ./paramchem/ligandrm.pdb".split())  # drawing_3D.mol2

# initialize the browser
br = mechanize.Browser()
br.set_handle_robots(False)  # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Firefox.')]
br.set_handle_redirect(mechanize.HTTPRedirectHandler)

# login fill-in form and submit
url = "https://cgenff.silcsbio.com/userAccount/userLogin.php"
response = br.open(url)
br.form = list(br.forms())[0]
usrName = br.form.find_control("usrName")
curPwd = br.form.find_control("curPwd")
usrName.value = args.username
curPwd.value = args.password
response = br.submit()
if response.wrapped.code == 200:
    print("Login successful")
else:
    print("Login failed")

# upload the file to parametrize, parse xml output
filename = args.conf
br.form = list(br.forms())[0]
br.form.add_file(open(filename), 'text/plain', filename)
response = br.submit()
xml = response.read().strip()
# print (xml)
dom = minidom.parseString(xml)
log = dom.getElementsByTagName('errinfo')[0].firstChild.data
if 'skipped molecule' in log:
    print(log)
    exit()
path = dom.getElementsByTagName('path')[0]
# inputf = dom.getElementsByTagName('mol2')[0] # huangjianxiang not working; COMMENTED
outputf = dom.getElementsByTagName('output')[0]

# save output
pathd = path.firstChild.data
strname = outputf.firstChild.data
url = "https://cgenff.silcsbio.com/initguess/filedownload.php?file={}/{}".format(pathd, strname)
# print (url)
response = br.open(url)
topology = response.read()
open(outputf.firstChild.data, "w").writelines(bytes.decode(topology))

mol2name = strname[:-4]+'.mol2'   # remove .str
url = "https://cgenff.silcsbio.com/initguess/filedownload.php?file={}/{}".format(pathd,mol2name)
# print (url)
response = br.open(url)
coordinates = response.read()
open(strname+'.mol2', "w").writelines(bytes.decode(coordinates))  # if upload mol2, should not overwrite
print("Files retrieved")
