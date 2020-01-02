# digital archive monitor scripts

## check-fedora-dev.py
Checks status at endpoints for fedora,solr,and cantaloupe image server. Sends email notification if service is unreachable. 
Image server runs two checks. One against backend server, the other locally. This is because cantalouple can crap out without 
actually going down.

Run every ten minutes by cron.

## imperium.py
Same as check-fedora but instead of sending notifications we attempt to use systemctl to ssh into backend server and restart service.

Also run by cron, but under root. This is necessary because backend services require sudo.
