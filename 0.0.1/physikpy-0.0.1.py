#!/usr/bin/python

# Name:			PhysikPy Modull
# Beschreibung:		Ein Modull mit Funktionen zum Berechnen von Physikalischen Gesetzen
# Autor:		Christoph Heer (Christoph.Heer@googlemail.com)

version = '0.1'
autor = 'Christoph Heer (Christoph.Heer@googlemail.com)'
gesetze = ['Hebelgesetz','Flaschenzug Zugkraft', 'Flaschenzug Seilzug']

def hebelgesetz(Fk=None, ak=None, Fl=None, al=None):
	# Ueberpruefung ob es eine Variable gibt die errechnet werden soll
	if Fk == None:
		# Orginal Umgestellte Formel Kraft = Last * Lastarm / Kraftarm
		Fk = 0
		Fk = float(Fk)
		Fl = float(Fl)
		al = float(al)
		ak = float(ak)
		Fk = Fl * al / ak
		return Fk
	if ak == None:

		# Orginal Umgestellte Formel Kraftarm = Last * Lastarm / Kraftarm
		ak = 0
		Fk = float(Fk)
		Fl = float(Fl)
		al = float(al)
		ak = float(ak)
		ak = Fl * al / Fk
		return ak
	if Fl == None:
		# Orginal Umgestellte Formel Last = Kraft * Kraftarm / Lastarm
		Fl = 0
		Fk = float(Fk)
		Fl = float(Fl)
		al = float(al)
		ak = float(ak)
		Fl = Fk * ak / al
		return Fl
	if al == None:
		# Orginal Umgestellte Formel Lastarm = Kraft * Kraftarm / Last
		al = 0
		Fk = float(Fk)
		Fl = float(Fl)
		al = float(al)
		ak = float(ak)
		al = Fk * ak / Fl
		return al

def flaschenzug_zugkraft(Fz=None, n=None, Fl=None):
	# Ueberpruefung ob es eine Variable gibt die errechnet werden soll
	if Fz == None:
		# Orginal Umgestellte Formel Kraft = 1 / Seile * Last
		Fz = 0
		Fz = float(Fz)
		n = float(n)
		Fl = float(Fl)
		Fz = 1 / n * Fl
		return Fz
	if n == None:
		# Orginal Umgestellte Formel Seile = Last / Kraft
		n = 0
		Fz = float(Fz)
		n = float(n)
		Fl = float(Fl)
		n = Fl / Fk
		return n
	if Fl == None:
		# Orginal Umgestellte Formel Last = Seile * Kraft
		Fl = 0
		Fz = float(Fz)
		n = float(n)
		Fl = float(Fl)
		Fl = n * Fz
		return Fl

def flaschenzug_seilzug(sz=None, n=None, sl=None):
	# Ueberpruefung ob es eine Variable gibt die errechnet werden soll
	if sz == None:
		# Orginal Umgestellte Formel GesamteSeillaenge = Anzahl * EinzelSeillaenge
		sz = 0
		sz = float(sz)
		n = float(n)
		sl = float(sl)
		sz = n * sl
		return sz
	if n == None:
		# Orginal Umgestellte Formel Anzahl = GesamteSeillaenge / EinzelSeillaenge
		n = 0
		sz = float(sz)
		n = float(n)
		sl = float(sl)
		n = sz / sl
		return n
	if sl == None:
		# Orginal Umgestellte Formel GesamteSeillaenge = EinzelSeillaenge / Anzahl
		sl = 0
		sz = float(sz)
		n = float(n)
		sl = float(sl)
		sl = sz / n
		return sl

