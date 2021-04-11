

# Press the green button in the gutter to run the script.
import csv
import community_report
import maskMandateScraper
import restaurantStatusScraper

us_state_abbrev = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

if __name__ == '__main__':
    mainFile = open('CountyData.csv', 'w', newline='')
    csv_writer = csv.writer(mainFile)
    csv_writer.writerow(["County", "State", "Mask Mandate", "Case per 100k", "Case Change", "Death Change",
                         "Positivity Rate", "Restaurant Status"])

    mask_orders = maskMandateScraper.get_mask_orders()
    restaurant_status = restaurantStatusScraper.food_scrape()
    counties = community_report.get_counties()
    cases_per_100k = community_report.get_cases_per_100k()
    case_increase = community_report.case_increase()
    death_increase = community_report.death_increase()
    infectivity = community_report.infectivity_rate()
    state = community_report.get_state()
    for i in range(1, 3273):
        currentState = us_state_abbrev.get(state[i])
        csv_writer.writerow([counties[i].replace(',',' '), currentState, mask_orders.get(currentState), cases_per_100k[i], case_increase[i],
                             death_increase[i], infectivity[i], restaurant_status.get(currentState)])