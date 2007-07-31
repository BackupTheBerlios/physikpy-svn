    def forcreator(self):
        '''Dies ist ein kleiner Assistent der eine .for Datei erstellen kann.'''
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
