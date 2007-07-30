# -*- coding: iso-8859-15 -*-
r""" Ein Modul welches Physik Gesetze als Funktionen bereitstellt

Dieses Modul soll Physik in Python integrieren um einfache aber
dennoch efektive Funktionen fuer Physikalische Berechnungen
bereitzustellen. Diese Gesetze sind in mehren Classes aufgeteilt
die fuer ein Thema stehen um weiter Übersicht zu haben.

Fuer weitere Formel oder Fragen wurde eine kleine Projekt Seite
auf dem Projekt Hosting BerliOS eingerichtet diese ist unter
http://http://developer.berlios.de/projects/physikpy/
erreichbar die Homepage zum Projekt ist unter
physikpy.berlios.de zugaenglich.

Achtung auf die Richtigkeit der Formeln und Erklaerungen wird keine
Gewehr gegeben. Die Entwickler wuerde sich ueber Verbesserungen oder
Kritik sehr freuen.
"""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modul Info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#|  Name:       PhysikPy Class                                            |#
#|  Autoren:    Christoph Heer (Christoph.Heer@googlemail.com)            |#
#|              Patrick Bitter (patrick_bitter@yahoo.de)                  |#
#|  Version:    0.5.1                                                     |#
#|  Datum:      28.07.2007                                                |#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
from __future__ import division
import math
class physikpy:
    # Allgemeine Infomationen ueber das Modul
    version = '0.5.1'
    relase = '28.07.2007'
    def info(self):
        """Anzeige der Infomationen von Version und Realase Datum der Class"""
        print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Modul Info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"
        print "#||  Name:       ||    PhysikPy Class"
        print "#||  Autor:      ||    Christoph Heer (Christoph.Heer@googlemail.com)"
        print "#|               ||    Patrick Bitter (patrick_bitter@yahoo.de)"
        print "#||  Version:    ||    " + physikpy.version
        print "#||  Relase:     ||    " + physikpy.relase
        print "#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#"
    
    # Grundgesetze
    grundgesetze_dic = {
        # Kraefte und ihre Wirkung
        'Gewichtskraft' : 'F = m * g',
        'Flaschenzug Seilzug' : 'sz = n * sl',
        'Flaschenzug Zugkraft' : 'Fz = 1 / n * Fl',
        'Hebel' : 'F1 * l1 = F2 * l2',
        'Arbeit' : 'W = F * s',
        'Beschreunigungsarbeit' : 'W = m * a * s',
        'Hubarbeit' : 'W = m * g * h',
        'Verformungsarbeit' : 'W = 0.5 * Fe * s',
        'Wirkungsgrad' : 'n = en / E',
        'Mechanische Leistung' : 'P = W / t',
        'Druck' : 'p = F / a',
        'Dichte' : 'p = m / V'
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
    """Class Erklaerung
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Die Einheit fur Physikalische Kraft ist N und gibt
    an wie start zwei Koerper aufeinander einwirken."""
    def gewichtskraft(self, F, m, g=9.81):
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        1N ist die Kraft die auf einem Koerper wirkt der
        eine Masse von 100g hat und von der Erde an gezogen
        wird.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        F = Wirkende Kraft
        m = Masse des Koerpers
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
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Der Seilzug vom Flaschenzug ist von den
        einzelen Laengen der Seile abhaenig.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        sz = Gesamter Seilzug
        n = Anzahl von Seilen
        sl = Einzelne Laengen"""
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
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Die Zugkraft ist von der Gewichtskraft
        und der Anzahl der Zeilen abhaenig. Um
        so mehr Seile um so weniger wird
        Zugkraft gebraucht

        Einheiten Erklaerung
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
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Der Hebel wird aus 4 Variablen berechnet F1,
        l1, F2, l2 die F Werte bezeichnen die Kraft
        auf einer Seite des Hebels. Die l Werte
        beichnet die Arm Laenge daraus kann man die
        einzelnen Werten berechnen.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        F1 = Kraft auf Arm 1
        l1 = Laenge des Arm 1
        F2 = Kraft auf Arm 2
        l2 = Laenge des Arm 2"""
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
  
    def arbeit(self, W, F, s):
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Die Mechanische Arbeit wird beim einwirken
        einer Kraft ausgeuebt z.B. beim Verformen oder
        bewegenen eines Gegenstandes.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        F = Die wirkende Kraft
        s = Der Weg der zurueckgelegt wird"""
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
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Beim Beschleunigen eines Koerpers wird
        Arbeit verrichtet.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        m = Masse des Koerpers
        s = Der Weg der zurueckgelegt wird
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
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Beim Heben eines Koerpers wird auch Kraft
        auf einen Koerper angewendet.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        m = Masse des Koerpers
        h = Hoehe
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
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Wenn eine Feder verformt wird dann wird
        auf die Feder auch Kraft angewendet

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        W = Arbeit in Joule
        Fe = Kraft die auf die Feder wirkt
        s = Die Laenge die hinzu kommt"""
	if W == '?':
		W = 0.5 * Fe * s
		return W
	if Fe == '?':
                Fe = W / 0.5 / s
                return Fe
       	if s == '?':
                s = W / 0.5 / Fe
                return s
            
    def wirkungsgrad(self, n, En, E):
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Mit diesem Gesetz wird ermittelt welcher
        Anteil der eingesetzten Energie in nutzbare
        Energie umgewandelt wird.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        n = Eta (Angabe meistens in Prozent)
        En = nutzbare Energie
        E = eingesetze Energie"""
	if n == '?':
		n = En / E
		return n
	if En == '?':
		En = n * E
		return En
	if E == '?':
		E = En / n
		return E

    def mechanische_leistung(self, P, w, t):
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Miter Leistung wird gezeigt wie viel mechanische
        Arbeit in 1 sek verrichtet wird.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        p = Watt
        w = Mechanische Arbeit
        Zeit = Benoetigte Zeit"""
	if P == '?':
		P = w / t
		return P
	if w == '?':
		w = P * t
		return w
	if t == '?':
		t = w / P
		return t

    def druck(self, p, F, A):
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Der Druck kennzeichnet den Zustand einer
        Fluessigkeit oder eines Gases, der durch
        Zusammenpressen entsteht.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        p = Pascal (1Pa = !n/m2)
        F = Kraft
        A = Flaeche"""
	if p == '?':
		p = F / A
		return p
	if F == '?':
		F = p * A
		return F
	if A == '?':
		A = F / p
		return A

    def dichte(self, p, m, V):
        """Funktions Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Die Dichte p gibt an, welche Masse m
        (in g) 1cm3 eines Stoffes hat.

        Einheiten Erklaerung
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        p = Dichte (1g/cm3)
        m = Masse
        V = Volumen"""
	if p == '?':
		p = m / V
		return p
	if m == '?':
		m = p * V
		return m
	if V == '?':
		V = m / p
		return V

class optik:
    
    def brennweite(f,g,b,G,B):
        """f: Brennweite [m]
        g: Gegenstandsweite [m]
        b: Bildweite [m]
        G: Gegenstandsgroeße [m]
        B: Bildgroeße [m]
        Gegenstand (Groeße G) <---g---> Linse <---b---> Bild (Groeße B)"""
    
        if f == '?' and g == '?' and b == '?' and G == '?' and B == '?':
            print 'Fehler! Zu wenig Argumente'
        elif f != '?' and g == '?' and b == '?' and G == '?' and B == '?':
            print 'Fehler! Zu wenig Argumente'
        elif f == '?' and g != '?' and b == '?' and G == '?' and B == '?':
            print 'Fehler! Zu wenig Argumente'     
        elif f == '?' and g == '?' and b != '?' and G == '?' and B == '?':
            print 'Fehler! Zu wenig Argumente'
        elif f == '?' and g == '?' and b == '?' and G != '?' and B == '?':
            print 'Fehler! Zu wenig Argumente'
        elif f == '?' and g == '?' and b == '?' and G == '?' and B != '?':
            print 'Fehler! Zu wenig Argumente'
        elif f != '?' and g != '?' and b == '?' and G == '?' and B == '?':
            b1 = 1.0/f-1.0/g
            b = 1.0/b1
        elif f != '?' and g == '?' and b != '?' and G == '?' and B == '?':
            g1 = 1.0/f-1.0/b
            g = 1.0/g1
        elif f == '?' and g != '?' and b != '?' and G == '?' and B == '?':
            f1 = 1.0/g+1.0/b
            f = 1.0/f1
        elif f == '?' and g != '?' and b != '?' and G != '?' and B == '?':
            B = 1.0*b*G/g
            f1 = 1.0/g+1.0/b
            f = 1.0/f1
        elif f == '?' and g != '?' and b != '?' and G == '?' and B != '?':
            G = 1.0*g*B/b
            f1 = 1/g+1/b
            f = 1.0/f1
        elif f != '?' and g == '?' and b != '?' and G != '?' and B == '?':
            g1 = 1.0/f-1.0/g
            g = 1.0/g1
            B = 1.0*b*G/g
        elif f != '?' and g == '?' and b != '?' and G == '?' and B != '?':
            g1 = 1.0/f-1.0/g
            g = 1.0/g1
            G = 1.0*g*B/b
        elif f != '?' and g != '?' and b == '?' and G != '?' and B == '?':
            b1 = 1.0/f-1.0/g
            b = 1.0/b1
            B = 1.0*b*G/g
        elif f != '?' and g != '?' and b == '?' and G == '?' and B != '?':
            b1 = 1.0/f-1.0/g
            b = 1.0/b1
            G = 1.0*g*B/b
        else:
            print 'Fehler: \n Nicht beruecksichtigte Kombination von f,g,b,G,B!'
            
        print 'Brennweite: %s \n Gegenstandsweite: %s \n Bildweite: %s \n Gegenstandsgroesse: %s \n Bildgroesse: %s' %(f,g,b,G,B)
        print '\n\n Alle Angaben in [m]!'
    
class dynamik:
    def freierFall(endgeschw, strecke, fallzeit, startgeschw, beschl):
        """Methode um eine beschleunigte Bewegung zu berechnen.
        Bisher kann man nur nach Endgescwindigkeit, Strecke und Fallzeit fragen.
        Eine Erweiterung ist in Arbeit.
        
        Es werden die Folgenden Parameter benoetigt:
        endgeschw: Endgeschwindigkeit
        strecke: zurueckgelegte Strecke
        fallzeit: Zeit der Beschleunigung
        startgeschw: Anfangsgeschwindigkeit
        beschl: Beschleunigung
        Auf "0" gesetzte Parameter werden nachgefragt, d.h. sie gelten als unbekannt"""
        
        
        #interne Variablen
        time = 0  #Zeit
        velo = 0  #Geschwindigkeit
        velo0 = 0 #Anfangsgeschwindigkeit
        way = 0   #Weg
        hight = 0 #Hoehe
        g = beschl #(Erd-)Beschleunigung
        
        velo0 = startgeschw
        
        if (endgeschw != 0 and strecke == 0 and fallzeit == 0):
            velo = endgeschw
            time = (velo-velo0)/g
            way = g*time*time/2 + velo0*time
        elif (endgeschw == 0 and strecke != 0 and fallzeit == 0):
            way = strecke
            time = -velo0/g + math.sqrt((velo0/g)*(velo0/g) + way)
            velo = g*time + velo0
        elif (endgeschw == 0 and strecke == 0 and fallzeit != 0):
            time = fallzeit
            velo = g*time + velo0
            way = g*time*time/2 + velo0*time
        #Wenn man mehr als eine Groeße angibt, muss die Beschleunigung neu berechnet werden, da sonst die Werte nich immer passen.
        elif (endgeschw != 0 and strecke != 0 and fallzeit == 0):
            velo = endgeschw
            way = strecke
            time = 2*way/(velo+velo0)
            g = (velo-velo0)/time
        elif (endgeschw != 0 and strecke == 0 and fallzeit != 0):
            velo = endgeschw
            time = fallzeit
            g = (velo-velo0)/time
            way = g*time*time/2 + velo0*time
        elif (endgeschw == 0 and strecke != 0 and fallzeit != 0):
            time = fallzeit
            way = strecke
            g = 2*(way-velo0*time)/time
            velo = velo0 + g*time
        elif (endgeschw != 0 and strecke != 0 and fallzeit != 0):
            time = fallzeit
            way = strecke
            velo = endgeschw
            g=(velo-velo0)/time
            test = g*time*time/2 + velo0*time
            if test != way:
                print 'Diese Daten passen nicht zusammen!'
            
        else:
            print 'Zu wenig Argumente!'
            
        print 'Fallzeit: %s s \n Strecke: %s m \n Endgeschwindigkeit: %s m/s \n Bei g=%s \n\n' %(time,way,velo,g)

class konstanten:
    """Zusammenstellung wichtiger Naturkonstanten
    Beschreibung ist wie folgt zu lesen:
    Name der Konstante (Genauigkeit bezogen auf die letzte angegebene Ziffer) [Einheit]
    Bei Ergaenzungen bitte wie bisher Kommentieren."""
    def E(exp):
        return pow(10,exp)
    def __init__():
        c = 299792458 #Lichtgescwindigkeit im Vakuum (exakt) [m/s]
        epsilon_0 = 8.854187817*E(-12) #Influenzkonstante (exakt) [AsV^-1m^-1]
        mu_0 = 1.2566370614*E(-6) #Induktionskonstante (exakt) [VsA^-1m^-1]
        G = 6.673*E(-11) #Gravitationskonstante (+/-10) [Nm^2kg^-2]
        N_A = 6.0221420*E(23) #Avogadro-Konstante (+/-5) [mol^-1]
        V_mol = 22.41400*E(-3) #Molvolumen bei Normalbedingungen (+/-4) [m^3mol^-1]
        k = 1.380650*E(-23) #Boltzmann-Konstante (+/-2) [JK^-1]
        R = 8.31447 #Gaskonstante (+/-2) [JK^-1mol^-1]
        e = 1.60217646*E(-19) #Elementarladung (+/-6) [C]
        F = 9.648342*E(4) #Faraday-Konstante (+/-4) [Cmol^-1]
        m_p = 1.6726216*E(-27) #Ruhemasse Proton (+/-1) [kg]
        m_n = 1.6749272*E(-27) #Ruhemasse Neutron (+/-1) [kg]
        m_e = 9.1083819*E(-31) #Ruhemasse Elektron (+/-7) [kg]
        h = 6.6260688*E(-34) #Planck-Konstante Wirkungsquantum (+/-5) [Js]
        hbar = 1.05457160*E(-34) #h-quer = h/(2pi) (+/-8) [Js]
        sigma = 5.67040*E(-8) #Stefan-Boltzmann-Konstante (+/-4) [Wm^-2K^-4]
        a_0 = 0.529177208*E(-10) #Bohr-Radius (+/-2) [m]
        Ry = 10973731.56855 #Rydberg-Konstante (+/-8) [m^-1]
        mu_B = 9.2740090*E(-24) #Bohr-Magneton (+/-4) [JT^-1]
        _alpha = 137.0359998 #Feinstrukturkonstante^-1 (+/-5)
        alpha = 1/_alpha #Feinstrukturkonstante
        
class vector:
    #Initialisierung durch vector(x,y,z)
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def sprod(self, vec):
        #Berechnet das Skalarprodukt zweier 'vector'
        return vec.x*self.x + vec.y*self.y + vec.z*self.z
    def vprod(self, vec):
        #Berechnet das Kreuzprodukt zweier 'vector'
        a = self.y*vec.z-self.z*vec.y
        b = self.z*vec.x-self.x*vec.z
        c = self.x*vec.y-self.y*vec.x
        return vector(a,b,c)
    def printme(self):
        #Erzeugt einen String zur Ausgabe
        str  = '(%s , %s , %s)' % (self.x , self.y , self.z)
        return str
    def betrag(self):
        #Gibt den Betrag zurueck
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    def add(self, vec):
        #Addition eines 'vectors'
        return vector(self.x+vec.x,self.y+vec.y,self.z+vec.z)
    def smult(self, s):
        #Multiplikation mit einem Skalar
        return vector(self.x*s,self.y*s,self.z*s)
    def zerlegung(self):
        #Gibt die Zerlegung in Karthesischen Koordinaten als String aus.
        return '%s *_e1 + %s *_e2 + %s *_e3' % (self.x, self.y, self.z)
    def zerlegungzyl(self):
        #Gibt die Zerlegung in Zylinderkordinaten als String aus.
        rho = math.sqrt(self.x*self.x + self.y*self.y)
        rho1 = 0
        if rho%1 == 0:
            rho1 = rho
        else:
            i = rho*rho
            rho1 = 'sqrt(%s)' %(i)
        phi = math.atan(self.y/self.x)/math.pi
        return '%s *_erho + %s *pi*_ephi + %s *ez' % (rho1,phi,self.z)
    def zerlegungkug(self):
        #Gibt die Zerlegung in Kugelkoordinaten als String aus.
        r = self.betrag()
        r1 = 0
        if r%1 == 0:
            r1 = r
        else:
            i = r*r
            r1 = 'sqrt(%s)' %(i)
        phi = math.atan(self.y/self.x)/math.pi
        theta = math.atan(math.sqrt(self.x*self.x + self.y*self.y)/self.z)/math.pi
        return '%s *_er + %s *pi *_ephi + %s *pi *_etheta' % (r1,phi,theta)
