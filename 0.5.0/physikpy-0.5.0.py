# -*- coding: iso-8859-15 -*-
r""" Ein Modul welches Physik Gesetze als Funktionen bereitstellt

Dieses Modul soll Physik in Python integrieren um einfache aber
dennoch efektive Funktionen f�r Physikalische Berechnungen
bereitzustellen. Diese Gesetze sind in mehren Classes aufgeteilt
die fuer ein Thema stehen um weiter �bersicht zu haben.

F�r weitere Formel oder Fragen wurde eine kleine Projekt Seite
auf dem Blog des Entwicklsers erstellt.
http://physikpy.ubuntux.net

Achtung auf die Richtigkeit der Formeln und Erkl�rungen wird keine
Gewehr gegeben. Der Entwickler w�rde sich �ber Verbesserungen oder
Kritik sehr freuen.
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modul Info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#|  Name:       PhysikPy Class                                            |#
#|  Autor:      Christoph Heer (Christoph.Heer@googlemail.com)            |#
#|  Version:    0.5                                                       |#
#|  Datum:      21.07.2007                                                |#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from __future__ import division
class physikpy:
    # Allgemeine Infomationen �ber das Modul
    version = '0.5.0'
    relase = '21.07.2007'
    def info(self):
        """Anzeige der Infomationen von Version und Realase Datum der Class"""
        print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modul Info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"
        print "#||  Name:       ||    PhysikPy Class"
        print "#||  Autor:      ||    Christoph Heer (Christoph.Heer@googlemail.com)"
        print "#||  Version:    ||    " + physikpy.version
        print "#||  Relase:     ||    " + physikpy.relase
        print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"
    
    # Grundgesetze
    grundgesetze_dic = {
        # Kr�fte und ihre Wirkung
        'Gewichtskraft' : 'F = m * g',
        'Flaschenzug Seilzug' : 'sz = n * sl',
        'Flaschenzug Zugkraft' : 'Fz = 1 / n * Fl',
        'Hebel' : 'F1 * l1 = F2 * l2',
        #Arbeit
        'Arbeit' : 'W = F * s',
        'Beschreunigungsarbeit' : 'W = m * a * s',
        'Hubarbeit' : 'W = m * g * h',
        'Verformungsarbeit' : 'W = 0.5 * Fe * s'
        }
    def grundgesetze(self):
        """Duch das Dic grundgesetze_dic wird eine anschauliche
        Liste aller Grundgesetze erstellt."""
        print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Grundgesetze ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"
        print "|| Folgende Formel sind aktuell in der PhysikPy Class " + physikpy.version
        print "|| ==========================================================================="
        for name, gesetz in physikpy.grundgesetze_dic.items():
            name = name + " " * (35 - len(name))
            print '|| %s ||  %s' % (name, gesetz)
        print "|| ==========================================================================="
        print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"

class kraefte:
    """Class Erkl�rung
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Die Einheit fur Physikalische Kraft ist N und gibt
    an wie start zwei K�rper aufeinander einwirken."""
    def gewichtskraft(self, F, m, g=9.81):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        1N ist die Kraft die auf einem K�rper wirkt der
        eine Masse von 100g hat und von der Erde an gezogen
        wird.

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        F = Wirkende Kraft
        m = Masse des K�rpers
        g = Ortsfaktor"""
        if F == '?':
		F = m * g
		return F
	if m == '?':
		m = F / g
		return m
	if g == '?':
		g = F / m
		return g
	    
    def flaschenzug_seilzug(self, sz, n, sl):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Der Seilzug vom Flaschenzug ist von den
        einzelen L�ngen der Seile abh�nig.

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sz = Gesamter Seilzug
        n = Anzahl von Seilen
        sl = Einzelne L�ngen"""
	if sz == '?':
		sz = n * sl
		return sz
	if n == '?':
		n = sz / sl
		return n
	if sl == '?':
		sl = sz / n
		return sl

    def flaschenzug_zugkraft(self, Fz, n, Fl):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Die Zugkraft ist von der Gewichtskraft
        und der Anzahl der Zeilen abh�nig. Um
        so mehr Seile um so weniger wird
        Zugkraft gebraucht

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Fz = Gesamte Zugkraft
        n = Anzahl von Seilen
        Fl = Gewichtskraft"""
	if Fz == '?':
		Fz = 1 / n * Fl
		return Fz
	if n == '?':
		n = Fl / Fk
		return n
	if Fl == '?':
		Fl = n * Fz
		return Fl

    def hebel(self, F1, l1, F2, l2):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Der Hebel wird aus 4 Variablen berechnet F1,
        l1, F2, l2 die F Werte bezeichnen die Kraft
        auf einer Seite des Hebels. Die l Werte
        beichnet die Arm L�nge daraus kann man die
        einzelnen Werten berechnen.

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        F1 = Kraft auf Arm 1
        l1 = L�nge des Arm 1
        F2 = Kraft auf Arm 2
        l2 = L�nge des Arm 2"""
	if F1 == '?':
		F1 = F2 * l2 / l1
		return F1
	if l1 == '?':
		l1 = F2 * l2 / F1
		return l1
	if F2 == '?':
		F2 = F1 * l1 / l2
		return F2
	if l2 == '?':
		l2 = F1 * l1 / F2
		return l2

class arbeit:    
    def arbeit(self, W, F, s):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Die Mechanische Arbeit wird beim einwirken
        einer Kraft ausge�bt z.B. beim Verformen oder
        bewegenen eines Gegenstandes.

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        F = Die wirkende Kraft
        s = Der Weg der zur�ckgelegt wird"""
	if W == '?':
		W = F * s
		return W
	if F == '?':
		F = W / s
		return F
	if s == '?':
		s = W / F
		return s

    def beschleunigungsarbeit(self, W, m, s, a):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Beim Beschleunigen eines K�rpers wird
        Arbeit verrichtet.

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        m = Masse des K�rpers
        s = Der Weg der zur�ckgelegt wird
        a = Die Geschwindigkeit"""
	if W == '?':
		W = m * a * s
		return W
	if m == '?':
                m = W / a / s
                return m
       	if s == '?':
                s = W / m / a
                return s
       	if a == '?':
                a = W / m / s
                return a

    def hubarbeit(self, W, m, h, g=9.81):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Beim Heben eines K�rpers wird auch Kraft
        auf einen K�rper angewendet.

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        m = Masse des K�rpers
        h = H�he
        g = Ortsfaktor"""
        self.hubarbeit_W = W
        self.hubarbeit_m = m
        self.hubarbeit_h = h
        self.hubarbeit_g = g
	if W == '?':
		W = m * g * h
		return W
	if m == '?':
                m = W / g / h
                return m
       	if g == '?':
                g = W / m / h
                return g
        if h == '?':
                h = W / g / m
                return h
            
    def verformungsarbeit(self, W, Fe, s):
        """Funktions Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Wenn eine Feder verformt wird dann wird
        auf die Feder auch Kraft angewendet

        Einheiten Erkl�rung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        Fe = Kraft die auf die Feder wirkt
        s = Die L�nge die hinzu kommt"""
	if W == '?':
		W = 0.5 * Fe * s
		return W
	if Fe == '?':
                Fe = W / 0.5 / s
                return Fe
       	if s == '?':
                s = W / 0.5 / Fe
                return s
