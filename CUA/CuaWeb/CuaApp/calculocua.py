def datos_sanitizados(self):
        datos = ['nombreapellido', 'codigofun','cua,''grado','departamento','estado']

        existe=True
        while existe:                               # Valida CUA unico  al generarlo
            numero_generado = random.randint(11111,99999)
            digito_generado = random.randint(1,9)
            cua_generado=str(numero_generado)+"-"+str(digito_generado)
            existe  self.miCua.set(cua_generado)
            sql="SELECT * FROM departamentos_cua WHERE cua='%s'" % cua_generado
            datos=self.run_query(sql)
            row_count = len(datos)
            if row_count == 0:    
                existe=True
            else:
                existe=False
        self.miCua.set(cua_generado)
        mayuscula=self.miNombre.get()
        self.miNombre.set(mayuscula.upper()) 