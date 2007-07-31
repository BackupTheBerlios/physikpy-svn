import pyformel
import sys

def read(filename):
    pyf = pyformel.pyformel(filename)
    print "~~~~~~~~~~~~~~~~~~ For File Inhalt 0.2 ~~~~~~~~~~~~~~~~~"
    print "Name:            " + pyf.name,
    print "Grundformel:     " + pyf.grundformel,
    print "Erstellt mit:    " + pyf.version,
    print "Wikipedia Link:  " + pyf.wikilink
    print "Beschreibung:    " + pyf.beschreibung,
    print "--------------------------------------------------------"
    wiederholungen = pyf.var_anzahl + 1
    for i in range(1, wiederholungen):
        i = str(i)
        exec "print '|' + i + '| ' + pyf.var" + i + " + '  (' + pyf.for" + i + " + ')'"
    print "--------------------------------------------------------"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# das Skript beginnt hier
if len(sys.argv) < 2:
	print 'Es wurden keine Parameter uebergeben.'
	sys.exit()

if sys.argv[1].startswith('--'):
	option = sys.argv[1][2:]
	# hole sys.argv[1], aber ohne die ersten beiden Zeichen
	if option == 'version':
		print 'Version 1.2'
	elif option == 'hilfe':
		print '''\
Dieses Programm gibt Dateien auf der Standardausgabe aus.
Es kann eine beliebige Anzahl von Dateien angegeben werden.
Als Optionen koennen angegeben werden:
  --version : Gibt die Versionsnummer aus
  --hilfe   : Gibt diese Hilfe aus'''
	else:
		print 'Unbekannte Option.'
	sys.exit()
else:
	for dateiname in sys.argv[1:]:
		read(dateiname)
