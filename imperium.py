import requests,urllib,os,subprocess

iiifRestart = 'systemctl --host root@ec2-34-205-22-110.compute-1.amazonaws.com restart cantaloupe.service'
tomcatRestart = 'systemctl --host root@ec2-34-205-22-110.compute-1.amazonaws.com restart fedora.service'

def fedoraDown(url='http://ec2-34-205-22-110.compute-1.amazonaws.com:8080/fedora', timeout=25):
    try:
        _ = requests.get(url, timeout=timeout)
        return False
    except requests.ConnectionError:
        return True

def solrDown(url='http://ec2-34-205-22-110.compute-1.amazonaws.com:8080/solr', timeout=25):
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
    subprocess.run(tomcatRestart, shell=True)
if solrDown():
    subprocess.run(tomcatRestart, shell=True)
if iiifDown():
    subprocess.run(iiifRestart, shell=True)
if iiifDown2():
    subprocess.run(iiifRestart, shell=True)
