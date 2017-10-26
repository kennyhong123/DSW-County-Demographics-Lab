import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties:
        if c["County"] < first:
            first=c["County"]
    return first

def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    highestCounty = counties[0]["County"]
    highestState = counties[0]["State"]
    highestPercent = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highestPercent:
            highestCounty = c["County"]
            highestState = c["State"]
            highestPercent = c["Age"]["Percent Under 18 Years"]
    return highestCounty + "," + highestState
    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    highestPercent = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highestPercent:
            highestPercent = c["Age"]["Percent Under 18 Years"]
    return highestPercent
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    highestCounty = counties[0]["County"]
    highestState = counties[0]["State"]
    highestPercent = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] > highestPercent:
            highestCounty = c["County"]
            highestState = c["State"]
            highestPercent = c["Age"]["Percent Under 18 Years"]
    return highestCounty,highestState,highestPercent
    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    var = 0
    eachState = counties[0]["State"]
    dict1 = {}
    dict1[counties[0]["State"]] = var
    for c in counties:
        if c["State"] == eachState:
            var += 1
            dict1[eachState] = var
        else:
            eachState = c["State"]
            var = 0
    #Find the state in the dictionary with the most counties
    highestPercent = dict1["AL"]
    state = dict1["AL"]
    for i, t in dict1.items():
        if t > highestPercent:
            highestPercent = t
            state = i
    #Return the state with the most counties
    return state
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    highestCounty = counties[0]["County"]
    highestState = counties[0]["State"]
    highestAsian = counties[0]["Ethnicities"]["Asian Alone"]
    for c in counties:
        if c["Ethnicities"]["Asian Alone"] > highestPercent:
            highestCounty = c["County"]
            highestState = c["State"]
            highestAsian = c["Ethnicites"]["Asian Alone"]
    return highestCounty,highestState,highestAsian
if __name__ == '__main__':
    main()
