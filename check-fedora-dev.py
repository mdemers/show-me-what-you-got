import requests,urllib,os,subprocess

fedoraMail = 'cd /home/ubuntu && echo "Subject: Fedora is down!" | /usr/sbin/sendmail  mikedemersjr@gmail.com'
solrMail = 'cd /home/ubuntu && echo "Subject: Solr is down!" | /usr/sbin/sendmail  mikedemersjr@gmail.com'
iiifMail = 'cd /home/ubuntu && echo "Subject: Cantaloupe is down!" | /usr/sbin/sendmail mikedemersjr@gmail.com'
iiifMail2 = 'cd /home/ubuntu && echo "Subject: Cantaloupe requires restart!" | /usr/sbin/sendmail mikedemersjr@gmail.com'

def fedoraDown(url='http://ec2-34-205-22-110.compute-1.amazonaws.com:8080/fedora', timeout=10):
	try:
		_ = requests.get(url, timeout=timeout)
		return False
	except requests.ConnectionError:
		return True

def solrDown(url='http://ec2-34-205-22-110.compute-1.amazonaws.com:8080/solr', timeout=10):
    try:
        _ = requests.get(url, timeout=timeout)
        return False
    except requests.ConnectionError:
        return True

def iiifDown(url='http://ec2-34-205-22-110.compute-1.amazonaws.com:8182', timeout=10):
    try:
        _ = requests.get(url, timeout=timeout)
        return False
    except requests.ConnectionError:
        return True

def iiifDown2(url='http://localhost/iiif/2/islandora:2105709/info.json', timeout=10):
    try:
        _ = requests.get(url, timeout=timeout)
        return False
    except requests.ConnectionError:
        return True

if fedoraDown():
	subprocess.run(fedoraMail, shell=True)
if solrDown():
	subprocess.run(solrMail, shell=True)
if iiifDown():
	subprocess.run(iiifMail, shell=True)
if iiifDown2():
    subprocess.run(iiifMail2, shell=True)
