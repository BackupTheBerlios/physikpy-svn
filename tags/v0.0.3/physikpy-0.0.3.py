#!/usr/bin/python

# Name:			PhysikPy Modull
# Beschreibung:		Ein Modull mit Funktionen zum Berechnen von Physikalischen Gesetzen
# Autor:		Christoph Heer (Christoph.Heer@googlemail.com)

version = '0.0.2'
autor = 'Christoph Heer (Christoph.Heer@googlemail.com)'
gesetze = ['Hebelgesetz','Flaschenzug Zugkraft', 'Flaschenzug Seilzug', 'Hubkraft']

from __future__ import division

def hebelgesetz(F1=None, l1=None, F2=None, l2=None):
	if F1 == None:
		F1 = F2 * l2 / l1
		return F1
	if l1 == None:

		l1 = F2 * l2 / F1
		return l1
	if F2 == None:
		F2 = F1 * l1 / l2
		return F2
	if l2 == None:
		l2 = F1 * l1 / F2
		return l2

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

def arbeit(W=None, F=None, s=None):
	if W == None:
		W = F * s
		return W
	if F == None:
		F = W / s
		return F
	if s == None:
		s = W / F
		return s

def kraft(F=None, m=None, a=None):
	if F == None:
		F = m * a
		return F
	if m == None:
		m = F / a
		return m
	if a == None:
		a = F / m
		return a

def gewichtskraft(F=None, m=None, g=None):
	if F == None:
		F = m * g
		return F
	if m == None:
		m = F / g
		return m
	if g == None:
		g = F / m
		return g

def drehmoment(M=None, r=None, F=None):
	if M == None:
		M = r * F
		return M
	if r == None:
		r = M / F
		return r
	if F == None:
		F = M / r
		return F