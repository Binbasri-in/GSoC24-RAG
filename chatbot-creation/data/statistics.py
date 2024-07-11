import csv
count = 0

tag_count = {}
with open("gsoc_organizations_ideas_link.csv", 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        count += 1
        tech_tags = row["tech_tags"].split(',')
        for tag in tech_tags:
            tag = str(tag).lower().strip()
            tag_count[tag] = tag_count.get(tag, 0) + 1

print("Skill, frequency")  
print(sorted(tag_count.values()))
for key, value in tag_count.items():
    if value > 3:
        print(f"{key}, {value}")
        
print(f"total organizations: {count}")

'''
rust, 11
typescript, 18
ai, 4
c, 26
c++, 52
python, 87
go, 11
qt, 8
javascript, 52
java, 30
android, 7
docker, 7
linux, 8
gtk, 4
mysql, 4
kubernetes, 6
assembly, 5
c/c++, 9
php, 7
jupyter, 4
react, 8
artificial intelligence, 4
django, 9
machine learning, 7
postgresql, 4
kotlin, 5
llvm, 4
flutter, 8
nodejs, 5
opengl, 4
numpy, 5
css, 4
swift, 5
'''

# similarly for ideas
count2 = 0

tag_count2 = {}
with open("ideas_data.csv", 'r') as f:
    data = csv.DictReader(f)
    for row in data:
        tech_tags = row["skills"]
        count2 += 1
        tech_tags = tech_tags[1:]
        tech_tags = tech_tags[:-1]
        for tag in tech_tags.split(","):
            tag = tag.strip()
            tag = tag[1:]
            tag = tag[:-1]
            tag = tag.lower().strip()
            tag_count2[tag] = tag_count2.get(tag, 0) + 1

print("Skill, frequency")  
print(sorted(tag_count2.values()))
for key, value in tag_count2.items():
    if value > 8:
        print(f"{key}, {value}")
        
print(f"total organizations: {count2}")

'''
c, 24
python, 91
git, 31
javascript, 45
node.js, 9
c++, 40
c/c++, 11
docker, 15
java, 31
typescript, 12
react, 13
rust, 20
communication, 16
unit testing, 14
nan, 24
system programming, 10
software development, 15
gsoc, 9
opencv, 10
tutorial creation, 10
video production, 10
doxygen documentation, 9
r, 11
sql, 11
spring, 13
rest, 9
'''