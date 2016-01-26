people={
	'Alice':{'phone':'15285649896','addr':'gz'},
	'Beth':{'phone':'15285118013','addr':'nx'},
	'Cecil':{'phone':'15285679860','addr':'hz'}
	}
labels={'phone':'phone number','addr':'address'}

name=input('Name:')
request=input('Phone number(p) or Address(a)?')
if request=='p':key='phone'
if request=='a':key='addr'
if name in people:print("%s's %s is %s." % (name,labels[key],people[name][key]))
