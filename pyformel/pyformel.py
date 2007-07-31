r"""Eine Klasse fuer die Verwendung von .for Dateien

Diese Klasse liest die .for Datei ein und stellt weitere
Tools um die Datei zu verwendung oder zu Bearbeiten zur
verfuegung.
"""
version = '0.1.0'
version_unix = 010

class pyformel():
    """Haupt Klasse von PyFormel"""
    def __init__(self, forfile):
        pyformel.forfile = forfile
        pyformel.f = file(pyformel.forfile, 'r')
        pyformel.id = int(pyformel.f.readline())
        pyformel.name = str(pyformel.f.readline())
        pyformel.version = str(pyformel.f.readline())
        pyformel.grundformel = str(pyformel.f.readline())
        pyformel.var_anzahl = int(pyformel.f.readline())
        self.wiederholungen = pyformel.var_anzahl + 1
        for self.i in range(1, self.wiederholungen):
            self.i = str(self.i)
            self.var_name = str(pyformel.f.readline())
            exec "pyformel.var" + self.i + " = " + self.var_name
        for self.i in range(1, self.wiederholungen):
            self.i = str(self.i)
            self.for_name = str(pyformel.f.readline())
            exec "pyformel.for" + self.i + " = " + self.for_name
        pyformel.beschreibung = str(pyformel.f.readline())
        pyformel.wikilink = str(pyformel.f.readline())
        pyformel.f.close()
        del pyformel.f
        del self.wiederholungen
        del self.i
        del self.for_name
        del self.var_name

    def for2py(self, pyfile):
        '''Diese Funktion wird benutzt wenn man eine .for Datei zu einer funktionsfaehigen
        Python Funktion umwandeln moechte.'''
        if pyformel.forfile == None:
            return "ERROR: Class wurde nicht richtig initalisiert"
        elif pyfile == None:
            return "ERROR: Funktion wurde ohne Py File Angabe gestartet"
        else:
            status = 'Fehler'
            funk_start = "def calko("
            wiederholungen = pyformel.var_anzahl
            for i in range(1, wiederholungen):
                i = str(i)
                exec "var_" + i + " = " + "pyformel.var" + i + " + '=None,'"
                exec "funk_start = funk_start + var_" + i
            i = str(wiederholungen)
            exec "var_" + i + " = " + "pyformel.var" + i + " + '=None):'"
            exec "funk_start = funk_start + var_" + i
            wiederholungen = wiederholungen + 1
            zeile1_a = "     if "
            zeile1_b = " == None: \n"
            zeile2_a = "         "
            zeile2_b = " \n"
            zeile3_a = "         return "
            zeile3_b = " \n"
            for i in range(1, wiederholungen):
                i = str(i)
                exec "zeile" + i + "_1 = zeile1_a + pyformel.var" + i + " + zeile1_b"
                exec "zeile" + i + "_2 = zeile2_a + pyformel.for" + i + " + zeile2_b"
                exec "zeile" + i + "_3 = zeile3_a + pyformel.var" + i + " + zeile3_b"
            newfile = file(pyfile, 'w')
            newfile.write("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# \n")
            newfile.write("#This File was createt with the PyFormel Class \n")
            newfile.write("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# \n")
            newfile.write(funk_start + ' \n')
            for i in range(1, wiederholungen):
                i = str(i)
                exec "zeile" + i + "_1 = zeile" + i + "_1"
                exec "zeile" + i + "_2 = zeile" + i + "_2"
                exec "zeile" + i + "_3 = zeile" + i + "_3"
                exec "newfile.write(zeile" + i + "_1)"
                exec "newfile.write(zeile" + i + "_2)"
                exec "newfile.write(zeile" + i + "_3)"
            newfile.write("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# \n")
            newfile.write("# powerd by physikpy.berlios.de \n")
            newfile.write("#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# \n")
            status = 'Erfolg'
            return status
