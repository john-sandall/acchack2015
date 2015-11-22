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

out = [[
    'AnswerDate',
    'AnsweringBody',
    'QuestionStatus',
    '_about',
    'answer',
    'answeringDeptId',
    'answeringDeptShortName',
    'answeringDeptSortName',
    'creator_about',
    'creator_label',
    'creator_writtenParliamentaryQuestion',
    'date',
    'dateTabled',
    'hansardHeading',
    'houseId',
    'humanIndexable',
    'indentifier',
    'legislature',
    'parliamentNumber',
    'published',
    'questionFirstAnswered',
    'questionText',
    'registeredInterest',
    'session',
    'sessionNumber',
    'tablingMember_about',
    'tablingMember_label',
    'tablingMember_writtenParliamentaryQuestion',
    'tablingMemberConstituency',
    'tablingMemberPrinted',
    'title',
    'type',
    'uin',
    'version',
    'writtenParliamentaryQuestionType'
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
        row['AnswerDate']['_value'],
        '|'.join(x['_value'] for x in row['AnsweringBody']),
        row.get('QuestionStatus', {}).get('_value', ""),
        row['_about'],
        row['answer'],
        row['answeringDeptId']['_value'],
        row['answeringDeptShortName']['_value'],
        row['answeringDeptSortName']['_value'],
        row['creator']['_about'],
        row['creator']['label']['_value'],
        '|'.join(x for x in row['creator'].get('writtenParliamentaryQuestion', [])),
        row['date']['_value'],
        row['dateTabled']['_value'],
        row.get('hansardHeading', {}).get('_value', ""),
        row.get('houseId', {}).get('_value', ""),
        row['humanIndexable']['_value'],
        row['identifier']['_value'],
        '|'.join(x for x in row['legislature']),
        row['parliamentNumber']['_value'],
        row['published']['_value'],
        '|'.join(x['_value'] for x in row['questionFirstAnswered']),
        row['questionText'],
        row['registeredInterest']['_value'],
        '|'.join(x for x in row['session']),
        row['sessionNumber']['_value'],
        row['tablingMember']['_about'],
        row['tablingMember']['label']['_value'],
        '|'.join(x for x in row['tablingMember'].get('writtenParliamentaryQuestion', [])),
        row.get('tablingMemberConstituency', {}).get('_value', ""),
        '|'.join(x['_value'] for x in row['tablingMemberPrinted']),
        row['title'],
        row['type'],
        row['uin'],
        row.get('version', ""),
        row['writtenParliamentaryQuestionType']
    ])

write_to_csv(out, 'answeredquestions-full.csv')
