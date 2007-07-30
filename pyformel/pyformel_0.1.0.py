version = '0.1.0'

class pyformel():
    def __init__(self, forfile=None):
        if forfile == None:
            pyformel.forfile = forfile
        
        else:
            pyformel.forfile = forfile
            pyformel.f = file(pyformel.forfile, 'r')
            pyformel.name = str(pyformel.f.readline())
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
            pyformel.f.close()
            del pyformel.f
            del self.wiederholungen
            del self.i
            del self.for_name
            del self.var_name

    def reader(self):
        '''Ein einfache Funktion um den Inhalt der vorher angegeben "for" Datei lesbar auszugeben'''
        if pyformel.forfile == None:
            print "~~~~~~~~~~~ Error ~~~~~~~~~~~"
            print "Diese Instanz der Class"
            print "PyFormel wurde ohne Angabe"
            print "einer 'for' Datei ausgefuehrt"
            print "deshalb kann diese Funktion"
            print "nicht ausgefuehrt werden."
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        else:
            print "~~~~~~~~~~~~~~~~~~~~~~ Reader 0.2 ~~~~~~~~~~~~~~~~~~~~~~"
            print "Name: " + pyformel.name,
            print "Grundformel: " + pyformel.grundformel,
            print "--------------------------------------------------------"
            self.wiederholungen = pyformel.var_anzahl + 1
            for self.i in range(1, self.wiederholungen):
                self.i = str(self.i)
                exec "print '|' + self.i + '| ' + pyformel.var" + self.i + " + '  (' + pyformel.for" + self.i + " + ')'"
            print "--------------------------------------------------------"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            del self.i
            del self.wiederholungen

    def forcreator(self):
        import sys
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ for Creator ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        filename = str(raw_input('Wie soll die Datei heissen: '))
        for_file = file(filename, 'w')
        name = str(raw_input('Wie heisst die Formel mit Namen: '))
        for_file.write(name + '\n')
        grundformel = str(raw_input('Wie heisst die Grundformel: '))
        for_file.write(grundformel + '\n')
        var_anzahl = int(raw_input('Wie viele Variablen hat die Formel: '))
        if var_anzahl < 3:
            sys.exit()
        var_anzahl_str = str(var_anzahl) + ' \n'
        for_file.write(var_anzahl_str)
        wiederholungen = var_anzahl + 1
        t1 = "'"
        t2 = "' \n"
        print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        print "|Variablen Abfrage"
        print "--------------------------------------------------------"
        for i in range(1, wiederholungen):
            i = str(i)
            exec "var" + i + " = str(raw_input('|" + i + ". Variable | '))"
            exec "for_file.write(t1 + var" + i + " + t2)"
        print "--------------------------------------------------------"
        print "|Formel Abfrage"
        print "|Gebe die Formel zu den Variablen an"
        print "--------------------------------------------------------"
        for i in range(1, wiederholungen):
            i = str(i)
            exec "for" + i + " = str(raw_input('Wie heisst die Formel fuer ' + var" + i + "+ ': '))"
            exec "for_file.write(t1 + for" + i + " + t2)" 

    def for2py(self, pyfile=None):
        if pyformel.forfile == None:
            print "~~~~~~~~~~~ Error ~~~~~~~~~~~"
            print "Diese Instanz der Class"
            print "PyFormel wurde ohne Angabe"
            print "einer 'for' Datei ausgefuehrt"
            print "deshalb kann diese Funktion"
            print "nicht ausgefuehrt werden."
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        elif pyfile == None:
            print "~~~~~~~~~~~ Error ~~~~~~~~~~~"
            print "Es wurde keine 'py' Datei als"
            print "Ziel angeben"
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        else:
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
            status = 'Erfolg'
            return status
