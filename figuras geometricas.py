class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

        def __str__(self):
            return f'alto: {self.alto}, ancho: {self.ancho}'
        def get_alto(self):
            return self.alto
        def set_alto(self, alto):
            self.alto = alto
        def set_ancho(self, ancho):
            self.ancho = ancho
        class Cuadrado(FiguraGeometrica):
            def __init__(self, lado):
                super().__init__(lado, lado)
            def area(self):
                return self.alto * self.ancho
            def __str__(self):
                return f"Cuadrado de lado {self.alto}, área: {self.área()}"

        class Rectangulo(FiguraGeometrica):
            def __init__(self, alto, ancho):
                super().__init__(alto, ancho)
            def area(self):
                return self.alto * self.ancho
            def __str__(self):
                return f"Rectangulo de alto {self.alto}, ancho {self.ancho}, área: {self.area()}"
        #Crear un cuadrado de lado 5
        cuadrado = Cuadrado(5)
        print(cuadrado) #Cuadrado de lado 5, área: 25

        # Crear un rectángulo de alto 4 y ancho 6
        rectangulo = Rectangulo(4,6)
        print(rectangulo)  # Rectangulo de alto 4, ancho: 6 área: 24