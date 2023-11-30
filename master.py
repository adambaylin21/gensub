# -*- coding: utf-8 -*-
import datetime
import json

with open("data.json", "r") as f:
    data = json.load(f)

full = data['data']['edit']['subtitles']['tracks']
for kw in full:
	items = full[kw]['items']

def tformat(td):
    minutes, seconds = divmod(td.seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

def t2format(td):
	d = '{:.3f}'.format(float(str(td).split(':')[2]))
	d = d.split('.')[1]
	return d

def wresult(data):
    with open('result.srt', 'a') as ccfb:
        ccfb.write(data + '\n')

start = 1
for item in items:
	a = datetime.timedelta(seconds=items[item]['from'])
	b = datetime.timedelta(seconds=items[item]['to'])
	c = ' '.join([w['value'] for w in items[item]['words']])
	s1 = str(tformat(a)) +','+ t2format(a)
	s2 = str(tformat(b)) +','+ t2format(b)

	wresult(str(start))
	time = '{} --> {}'.format(s1,s2)
	wresult(time)
	wresult(c + '\n')
	start += 1
	

