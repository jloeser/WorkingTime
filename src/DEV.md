# Development

Example code for working time handling:
```
db = Datebase()
days = db.load()
print(days)
> [<day: 1>, <day: 2>, ... ]
day = days.get("2023-04-06")
day.start = "10:00"
day1 = days.get("2023-02-05")
del(day1)
days.delete("2023-02-04")
db.save(days)
```
