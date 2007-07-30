#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Tool Info ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#|  Name:       Grundgesetze Reader                                       |#
#|  Autor:      Christoph Heer (Christoph.Heer@googlemail.com)            |#
#|  Version:    0.1                                                       |#
#|  Datum:      29.07.2007                                                |#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
import physikpy
import sys
physik = physikpy.physikpy()

def grundgesetz_info(name):
    gesetz = physik.grundgesetze_dic[name]
    print '~~~~~~~~~~~~~~~~~~~~ PhysikPy Tool ~~~~~~~~~~~~~~~~~~~~'
    print '|Grundgesetze aus PhysikPy                            |'
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 'Das Gesetz fuer deine Anfrage ' + name + ' ist:'
    print gesetz
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'

def grundgesetz_info_text(name):
    gesetz = physik.grundgesetze_dic[name]
    print gesetz
    
if len(sys.argv) < 2:
    print 'ERROR: Es wurde keine Ausgabe Art gewaehlt'
    sys.exit()
if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	# hole sys.argv[1], aber ohne die ersten beiden Zeichen
	if option == 'version':
	    print 'Version 0.1',
	elif option == 'name':
	    grundgesetz_info(sys.argv[2])
	elif option == 'name-text':
	    grundgesetz_info_text(sys.argv[2])
	elif option == 'list-text':
	    for name, gesetz in physik.grundgesetze_dic.items():
                name = name + " " * (35 - len(name))
                print name + gesetz
	elif option == 'list':
	    physik.grundgesetze()
	elif option == 'hilfe':
	    print '''\

Dieses Programm verarbeit das Dic aus der PhysikPy Class und
gibt diese Formatiert aus.
  --list                : Zeigt eine Fortmatierte Liste der Gesetze an
  --list-text           : Zeigt eine nicht Fortmatierte List an
  --name [name]         : Zeigt eine Fortmatierte Ausgabe der Formel
                          mit dem angegebenen Namen
  --name-text [name]    : Zeigt eine nicht Fortmatierte Ausgabe der
                          Formel mit dem angegebenen Namen
  --version             : Gibt die Versionsnummer aus
  --hilfe               : Gibt diese Hilfe aus'''
	else:
		print 'Unbekannte Option.'
	sys.exit()
