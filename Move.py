class Move:
    def __init__(self, wektor, jump):
        self.wektor = wektor # Na które pole względem obecnego wykonać ruch
        self.jump = jump # 1 czy 2 pola
        self.tile_number: int  # Numer pola na które zostanie wykonany ruch
        self.tile: int # Indeks pola w liście "plansza" na który zostanie wykonany ruch
        self.player: int # Do którego gracza należy pole na które zostanie wykonany ruch