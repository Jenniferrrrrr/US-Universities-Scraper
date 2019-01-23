import requests,time
from bs4 import BeautifulSoup
import csv

universities = ['Princeton University', 'Harvard University', 'Columbia University', 'Massachusetts Institute of Technology', 'University of Chicago', 'Yale University', 'Stanford University', 'Duke University', 'University of Pennsylvania', 'Johns Hopkins University', 'Northwestern University', 'California Institute of Technology', 'Dartmouth College', 'Brown University', 'Vanderbilt University', 'Cornell University', 'Rice University', 'University of Notre Dame', 'University of California--Los Angeles', 'Washington University in St. Louis', 'Emory University', 'Georgetown University', 'University of California--Berkeley', 'University of Southern California', 'Carnegie Mellon University', 'University of Virginia', 'Tufts University', 'University of Michigan--Ann Arbor', 'Wake Forest University', 'New York University', 'University of California--Santa Barbara', 'University of North Carolina--Chapel Hill', 'University of California--Irvine', 'University of Rochester', 'Brandeis University', 'Georgia Institute of Technology', 'University of Florida', 'Boston College', 'College of William and Mary', 'University of California--Davis', 'University of California--San Diego', 'Boston University', 'Case Western Reserve University', 'Northeastern University', 'Tulane University', 'Pepperdine University', 'University of Georgia', 'University of Illinois--Urbana-Champaign', 'Rensselaer Polytechnic Institute', 'University of Texas--Austin', 'University of Wisconsin--Madison','Villanova University', 'Lehigh University', 'Syracuse University', 'University of Miami', 'Ohio State University--Columbus', 'Purdue University--West Lafayette', 'Rutgers University--New Brunswick', 'Pennsylvania State University--University Park', 'Southern Methodist University', 'University of Washington', 'Worcester Polytechnic Institute', 'George Washington University', 'University of Connecticut', 'University of Maryland--College Park', 'Brigham Young University--Provo', 'Clark University', 'Clemson University', 'Texas A&M University--College Station', 'Florida State University', 'Fordham University', 'Stevens Institute of Technology', 'University of California--Santa Cruz', 'University of Massachusetts--Amherst', 'University of Pittsburgh', 'University of Minnesota--Twin Cities', 'Virginia Tech', 'American University', 'Baylor University', 'Binghamton University--SUNY', 'Colorado School of Mines', 'North Carolina State University--Raleigh', 'Stony Brook University--SUNY', 'Texas Christian University', 'Yeshiva University', 'Michigan State University', 'University of California--Riverside', 'University of San Diego', 'Howard University', 'Indiana University--Bloomington', 'Loyola University Chicago', 'Marquette University', 'University at Buffalo--SUNY', 'University of Delaware', 'University of Iowa', 'Illinois Institute of Technology', 'Miami University--Oxford', 'University of Colorado--Boulder', 'University of Denver', 'University of San Francisco', 'University of Vermont', 'Clarkson University', 'Drexel University', 'Rochester Institute of Technology', 'University of Oregon', 'New Jersey Institute of Technology', 'Saint Louis University', 'SUNY College of Environmental Science and Forestry', 'Temple University', 'University of Arizona', 'University of New Hampshire', 'University of South Carolina', 'University of the Pacific', 'University of Tulsa', 'Arizona State University--Tempe', 'Auburn University', 'Rutgers University--Newark', 'University of Tennessee', 'DePaul University', 'Duquesne University', 'Iowa State University', 'Seton Hall University', 'University of Utah', 'University of Oklahoma', 'University of South Florida', 'University of St. Thomas', 'San Diego State University', 'University of Dayton', 'The Catholic University of America', 'University of Alabama', 'University of Illinois--Chicago', 'University of Kansas', 'University of Missouri', 'University of Nebraska--Lincoln', 'University of Texas--Dallas', 'George Mason University', 'Michigan Technological University', 'University of California--Merced', 'University of La Verne', 'Colorado State University', 'Hofstra University', 'Louisiana State University--Baton Rouge', 'Mercer University', 'Oregon State University', 'University at Albany--SUNY', 'Washington State University', 'Adelphi University', 'Kansas State University', 'The New School', 'University of Cincinnati', 'University of Kentucky', 'St. John Fisher College', "St. John's University", 'Union University', 'University of Arkansas', 'University of Mississippi', 'Biola University', 'Missouri University of Science & Technology', 'Oklahoma State University', 'University of Alabama--Birmingham', 'University of Hawaii--Manoa', 'University of Massachusetts--Lowell', 'University of Rhode Island', 'Virginia Commonwealth University', 'Edgewood College', 'University of Central Florida', 'University of Idaho', 'University of Maryland--Baltimore County', 'Montclair State University', 'Seattle Pacific University', 'Ball State University', 'Illinois State University', 'Ohio University', 'Rowan University', 'University of Houston', 'University of Louisville', 'Florida Institute of Technology', 'Maryville University of St. Louis', 'Mississippi State University', 'Pace University', 'Suffolk University', 'University of Maine', 'Immaculata University', 'Lesley University', 'Robert Morris University', 'University of Wyoming', 'Florida International University', 'Georgia State University', 'Texas Tech University', 'University of New Mexico', 'Kent State University', 'Nova Southeastern University', 'University of Massachusetts--Boston', 'Andrews University', 'East Carolina University', 'Indiana University-Purdue University--Indianapolis', 'Lipscomb University', 'University of Hartford', 'University of North Carolina--Charlotte', 'Widener University', 'Regent University', 'University of Montana', 'University of Nevada--Reno', 'University of North Carolina--Greensboro', 'Azusa Pacific University', 'California State University--Fresno', 'Central Michigan University', 'Montana State University', 'University of Colorado--Denver', 'University of North Dakota', 'Utah State University', 'Wayne State University', 'Western Michigan University', 'West Virginia University', 'Bowling Green State University', 'North Dakota State University', 'Old Dominion University', 'Shenandoah University', 'University of Alaska--Fairbanks', 'University of Massachusetts--Dartmouth', 'Benedictine University', 'California State University--Fullerton', 'Dallas Baptist University', 'New Mexico State University', 'University of Texas--Arlington', 'South Dakota State University', 'Southern Illinois University--Carbondale', 'University of Missouri--St. Louis', 'University of South Dakota', 'American International College', 'Ashland University', 'Augusta University', 'Barry University', 'Boise State University', 'Cardinal Stritch University', 'Clark Atlanta University', 'Cleveland State University', 'Eastern Michigan University', 'East Tennessee State University', 'Florida A&M University', 'Florida Atlantic University', 'Gardner-Webb University', 'Georgia Southern University', 'Grand Canyon University', 'Indiana State University', 'Indiana University of Pennsylvania', 'Jackson State University', 'Kennesaw State University', 'Lamar University', 'Liberty University', 'Lindenwood University', 'Louisiana Tech University', 'Middle Tennessee State University', 'Morgan State University', 'National Louis University', 'North Carolina A&T State University', 'Northern Arizona University', 'Northern Illinois University', 'Oakland University', 'Portland State University', 'Prairie View A&M University', 'Sam Houston State University', 'San Francisco State University', 'Spalding University', 'Tennessee State University', 'Tennessee Technological University', 'Texas A&M University--Commerce', 'Texas A&M University--Corpus Christi', 'Texas A&M University--Kingsville', 'Texas Southern University', 'Texas State University', "Texas Woman's University", 'Trevecca Nazarene University', 'Trinity International University', 'University of Akron', 'University of Alabama--Huntsville', 'University of Arkansas--Little Rock', 'University of Louisiana--Lafayette', 'University of Louisiana--Monroe', 'University of Maryland--Eastern Shore', 'University of Memphis', 'University of Missouri--Kansas City', 'University of Nebraska--Omaha', 'University of Nevada--Las Vegas', 'University of New Orleans', 'University of Northern Colorado', 'University of North Texas', 'University of South Alabama', 'University of Southern Mississippi', 'University of Texas--El Paso', 'University of Texas--Rio Grande Valley', 'University of Texas--San Antonio', 'University of the Cumberlands', 'University of Toledo', 'University of West Florida', 'University of West Georgia', 'University of Wisconsin--Milwaukee', 'Valdosta State University', 'Wichita State University', 'Wilmington University']
number=[]
temp1,temp2=[],[]
html = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_university_affiliation")
soup = BeautifulSoup(html.content, 'html.parser')
result = soup.find('table')
results = result.find("tbody").find_all("tr")
for r in results:
    search=r.find_all("td")
    if search:
        if search[1].find("a") and search[1].find("a").get_text().strip() != "" and search[2].find("img"):
                if search[2].find("img").get("alt") =="United States":
                    temp1.append(search[1].find("a").text.encode('ascii', 'ignore').decode('ascii'))
                    temp2.append(search[3].get_text().strip().encode('ascii', 'ignore').decode('ascii'))
        if search[0].find("a") and search[0].find("a").get_text().strip() != "" and search[1].find("img"):
                if search[1].find("img").get("alt") =="United States":
                    temp1.append(search[0].find("a").text.encode('ascii', 'ignore').decode('ascii'))
                    temp2.append(search[2].get_text().strip().encode('ascii', 'ignore').decode('ascii'))
tables = soup.find_all("table",attrs={"class":"wikitable"})[35:]
temp=[]
for table in tables:
    search = table.find("tbody").find_all("tr")
    for s in search:
        results = s.find_all("td",attrs={"colspan":"4"})
        for result in results:
                if result.find("a",attrs={"title":"United States"}):
                    temp.append(result.get_text().strip())
                    temp.append(result.find_next("td",attrs={"colspan":"4"}).get_text().strip())
for i in range(len(temp)):
    if ", United States" in temp[i]:
        temp[i]=temp[i][:temp[i].find(", United States")]
        temp1.append(temp[i])
    else:
        temp[i]=temp[i][7:9]
        temp2.append(temp[i])

html = requests.get("https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_university_affiliation_II")
soup = BeautifulSoup(html.content, 'html.parser')
contents = soup.find_all("table",attrs={"class":"wikitable"})
tables = contents[:12]
temp=[]
for table in tables:
    search = table.find("tbody").find_all("tr")
    for s in search:
        results = s.find_all("td",attrs={"colspan":"4"})
        for result in results:
            if result:
                if result.find("a",attrs={"title":"United States"}):
                    temp.append(result.get_text().strip().encode('ascii', 'ignore').decode('ascii'))
                    temp.append(result.find_next("td",attrs={"colspan":"4"}).get_text().strip().encode('ascii', 'ignore').decode('ascii'))
                elif "United States" in result.get_text().strip().encode('ascii', 'ignore').decode('ascii'):
                    temp.append(result.get_text().strip().encode('ascii', 'ignore').decode('ascii'))
                    temp.append(result.find_next("td",attrs={"colspan":"4"}).get_text().strip().encode('ascii', 'ignore').decode('ascii'))

for i in range(len(temp)):
    if ", United States" in temp[i]:
        temp[i]=temp[i][:temp[i].find(", United States")]
        temp1.append(temp[i])
    else:
        temp[i]=temp[i][7:9]
        temp2.append(temp[i])

others = contents[12:]
value = 5
for other in others:
    search = other.find("tbody").find_all("tr")
    for s in search:
        results = s.find_all("td",attrs={"colspan":"4"})
        for result in results:
            if result:
                if result.find("a",attrs={"title":"United States"}):
                    temp1.append(result.get_text().strip().encode('ascii', 'ignore').decode('ascii'))
                    temp2.append(value)
                elif "United States" in result.get_text().strip().encode('ascii', 'ignore').decode('ascii'):
                    temp1.append(result.get_text().strip().encode('ascii', 'ignore').decode('ascii'))
                    temp2.append(value)
    value -= 1
for i in range(len(temp1)):
    if ", United States" in temp1[i]:
        temp1[i]=temp1[i][:temp1[i].find(", United States")]



# big=[universities,quora]
# big=list(map(list, zip(*big)))
# with open('Quora.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name","Quora Link"])
#     writer.writerows(big)


