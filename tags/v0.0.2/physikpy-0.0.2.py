#!/usr/bin/python

# Name:			PhysikPy Modull
# Beschreibung:		Ein Modull mit Funktionen zum Berechnen von Physikalischen Gesetzen
# Autor:		Christoph Heer (Christoph.Heer@googlemail.com)

version = '0.0.2'
autor = 'Christoph Heer (Christoph.Heer@googlemail.com)'
gesetze = ['Hebelgesetz','Flaschenzug Zugkraft', 'Flaschenzug Seilzug', 'Hubkraft']

from __future__ import division

def hebelgesetz(Fk=None, ak=None, Fl=None, al=None):
	if Fk == None:
		Fk = Fl * al / ak
		return Fk
	if ak == None:

		ak = Fl * al / Fk
		return ak
	if Fl == None:
		Fl = Fk * ak / al
		return Fl
	if al == None:
		al = Fk * ak / Fl
		return al

def flaschenzug_zugkraft(Fz=None, n=None, Fl=None):
	if Fz == None:
		Fz = 1 / n * Fl
		return Fz
	if n == None:
		n = Fl / Fk
		return n
	if Fl == None:
		Fl = n * Fz
		return Fl

def flaschenzug_seilzug(sz=None, n=None, sl=None):
	if sz == None:
		sz = n * sl
		return sz
	if n == None:
		n = sz / sl
		return n
	if sl == None:
		sl = sz / n
		return sl

def hubkraft(whub=None, Fg=None, h=None):
	if whub == None:
		whub = Fg * h
		return whub
	if Fg == None:
		Fg = whub / h
		return Fg
	if h == None:
		h = whub / Fg
		return h