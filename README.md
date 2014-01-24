thekraken
=========

I only wanted to create a project with this name, so I can say "release thekraken!"

![Release the kraken!](http://3.bp.blogspot.com/-lscCNrWlwLo/TdV6PzMYo-I/AAAAAAAAAJU/jJbnmypKzjw/s320/kraken.jpg)


A kraken has big tentacles, so you can specify `domains`, `machines`, `services` and `webpages`, and the kraken will check if they are up or down, notifying you by email if one of your targets is unreachable.

Just rename `settings.py.example` to `settings.py`, add your targets there, and run `summon.py`. I would recommend creating a cronjob that executes the latter script periodically.
