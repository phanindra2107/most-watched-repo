import sys
import requests
import json

tem_str = sys.argv

ind = tem_str.index("--org")
a = tem_str[ind+1]

org_name = str(a)
api_url = 'https://api.github.com/orgs/%s/repos?per_page=100' % org_name
repos = requests.get(api_url + "&page=" + str(1))

if repos != None and repos.status_code == 200 and len(repos.json()) > 0:

    data=json.loads(repos.text)
    #print(data)
    dict = {}

    for d in data:

        repo = d['name']
        watchers_c = d['watchers_count']
        dict.update({repo: watchers_c})

    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)

    high_repo = sorted_dict[0][0]
    high_wat_count = sorted_dict[0][1]


    all_contributors = list()
    page_count = 1

    high_api_url = "https://api.github.com/repos/" + a + "/" + high_repo + "/stats/contributors"

    contributors = requests.get(high_api_url)

    data1=json.loads(contributors.text)

    dict1={}

    for d in data1:

        user= d['author']['login']
        total_contributions = d['total']

        dict1.update({user:total_contributions})

    sorted_dict1 = sorted(dict1.items(), key=lambda kv: kv[1],reverse=True)


    ind = tem_str.index("--top")

    try:
        rng = int(tem_str[ind + 1])
        if rng > 0:
            print(''.join(("Top ", str(rng)," Contributors for the repo ", str(high_repo)," are:")))
            for i in range(0,rng):
                print(sorted_dict1[i][0])
        else:
            print("Error: Contributors value should be greater than 0")
    except:
        print("Error: Contributors should be an integer")

else:
    print("Error: Invalid Organisation Name")
