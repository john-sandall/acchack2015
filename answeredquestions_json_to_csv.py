#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import csv
import simplejson as json


def write_to_csv(mylist, filename, print_exceptions=False):
    """
    Turns a list of lists into a csv file
    """
    f = open(filename, 'wb')
    w = csv.writer(f, quoting=csv.QUOTE_ALL)
    for entry in mylist:
        try:
            w.writerow(entry)
        except UnicodeEncodeError:
            entry_utf8 = []
            for item in entry:
                entry_utf8.append(item.encode('utf8'))
            w.writerow(entry_utf8)
        except Exception:
            if print_exceptions:
                print entry
                pass
    f.close()
    return True


filename = './data/answeredquestions-all.json'

with open(filename) as f:
    data = json.loads(f.read())

out = [['id',
        'AnsweringBody',
        'answer',
        'answerText',
        'answeringMember',
        'answeringMemberConstituency',
        'answeringMemberPrinted',
        'dateOfAnswer',
        'isMinisterialCorrection',
        'date',
        'hansardHeading',
        'houseId',
        'questionText',
        'registeredInterest',
        'tablingMember',
        'tablingMemberConstituency',
        'tablingMemberPrinted',
        'version',
        ]]


i = 0
percent = 0
for row in data:
    i += 1
    p = 100*i/len(data)
    if p > percent:
        percent = p
        print "{}%".format(p)
    out.append([
        row['uin'],
        row['answer']['_about'],
        row['answer']['answerText']['_value'],
        row['answer']['answeringMember']['_about'],
        row['answer'].get('answeringMemberConstituency', {'_value': ''})['_value'],
        row['answer']['answeringMemberPrinted']['_value'],
        row['answer']['dateOfAnswer']['_value'],
        row['answer']['isMinisterialCorrection']['_value'],
        '|'.join(x['_value'] for x in row['AnsweringBody']),
        row['date']['_value'],
        row.get('hansardHeading', {}).get('_value', ""),
        row.get('houseId', {}).get('_value', ""),
        row['questionText'],
        row['registeredInterest']['_value'],
        row['tablingMember']['_about'],
        row.get('tablingMemberConstituency', {}).get('_value', ""),
        '|'.join(x['_value'] for x in row['tablingMemberPrinted']),
        row.get('version', ""),
    ])

write_to_csv(out, 'answeredquestions-full.csv')
