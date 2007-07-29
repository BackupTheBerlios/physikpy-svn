#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tool Info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#|  Name:       Hebel Berechung                                           |#
#|  Autor:      Christoph Heer (Christoph.Heer@googlemail.com)            |#
#|  Version:    0.1                                                       |#
#|  Datum:      29.07.2007                                                |#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import physikpy
import sys

if len(sys.argv) < 2:
	print '~~~~~~~~~~~~~~~~~~~~ PhysikPy Tool ~~~~~~~~~~~~~~~~~~~~'
	print '|Hebel Berechung 0.1                                   |'
	print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
	print 'Bitte gebe denn Variablen einen Wert oder setze ein ?'
	print 'um die Variable fuer die Berechung zu setzen'
	F1 = str(raw_input('Wie lautet der Wert von F1: '))
	l1 = str(raw_input('Wie lautet der Wert von l1: '))
	F2 = str(raw_input('Wie lautet der Wert von F2: '))
	l2 = str(raw_input('Wie lautet der Wert von l2: '))
	if F1 != '?':
            F1 = int(F1)
        if l1 != '?':
            l1 = int(l1)
        if F2 != '?':
            F2 = int(F2)
        if l2 != '?':
            l2 = int(l2)
        kraft = physikpy.kraefte()
        ergebnis = str(kraft.hebel(F1, l1, F2, l2))
        print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        if ergebnis == 'None':
            print 'Die Berechung hat nichts ergeben da alle Variablen'
            print 'gefuellt waren.'
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            sys.exit()
        else:
            print 'Das Ergebnis ist ' + ergebnis
            print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
            sys.exit()
if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	# hole sys.argv[1], aber ohne die ersten beiden Zeichen
	if option == 'version':
	    print 'Version 0.1',
	elif option == 'c':
            F1 = str(sys.argv[2])
            l1 = str(sys.argv[3])
            F2 = str(sys.argv[4])
            l2 = str(sys.argv[5])
            if F1 != '?':
                F1 = int(F1)
            if l1 != '?':
                l1 = int(l1)
            if F2 != '?':
                F2 = int(F2)
            if l2 != '?':
                l2 = int(l2)
            kraft = physikpy.kraefte()
            ergebnis = str(kraft.hebel(F1, l1, F2, l2))
            if ergebnis == 'None':
                print 'ERROR: Die Berechung hat nichts ergeben da alle Variablen gefuellt waren.'
                sys.exit()
            else:
                print ergebnis
                sys.exit()
	elif option == 'hilfe':
	    print '''\

Dieses Programm ist fuer die Berechnung vom Hebelgesetz.
Dabei wir die PhysikPy Class verwendet die auf Voraussetzung
ist um die Berechung durch zu fuehren.
Als Optionen koennen angegeben werden:
  --version : Gibt die Versionsnummer aus
  
  --hilfe   : Gibt diese Hilfe aus
  
  --c       : Nach Angabe dieser Option einfach F1 l1 F2 l2 angeben
              eine muss aber ein ? um zu vermittel das diese Ausgerechnet
              werden soll
              
              Beispiel: python hebel.py --c 5 2 5 ?'''
	else:
		print 'Unbekannte Option.'
	sys.exit()
