from lxml import html
import requests

def getPage(url):
  """ Fetch the content of the url, return an lxml html tree """
  page = requests.get(url)
  tree = html.fromstring(page.text)
  return tree

def parseTeam(tree):
  """ Get the text of the paragraphs containing caption information for the team """
  return tree.xpath("//span[@class='img-container caption']/p/text()")

def printTeam(team):
  """ Team is a list containing teammember names and descriptions
      
      Iterate over the list in twos because the teammember name and description
      are grouped together """
  for i in xrange(0,len(team), 2):
    name, description = team[i], team[i+1]
    print(name + ", " + description)

def main():
  tree = getPage("https://www.prism.com/about")
  team = parseTeam(tree)
  printTeam(team) 

if __name__ == "__main__":
  main()
