# mikrotik-firewall-rules-to-csv
Transform mikrotik firewall rules into a csv easy manageable with an spreadsheet

When you have a large number of rules on your firewall sometimes it's dificult to figure out what it is exactly doing. 

One solution would be to transform the rule list into a a spreadsheet and be able to order it by some field, change column order, etc. 

First, download the firewall rules to a file 

```
ip firewall filter export=firewall
```

Then download from files the file ```firewall.rsc``` on the same directory of the python script, next execute the program

``` 
python fw_mk.py
```

That will create ```mk-out.csv```.
