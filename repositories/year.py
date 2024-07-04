from models import Session, Year

class YearRepository():

    # Inicializa repositório
    def __init__(self, session: Session):
        self.__session = session

    # Método create do repositório
    def create(self, year_string: str) -> Year:
        existent_year = self.exist_year(year_string)

        if existent_year:
            return existent_year

        year = Year(year_string)
        self.__session.add(year)
        return year

    # Método read do repositório
    def read(self) -> [Year]:
        existent_years = self.__session.query(Year).all()
        return existent_years

    # Método exist do repositório
    def exist_year(self, year_string: str) -> Year:
        existent_years = self.read()

        for year in existent_years:
            if year.year == year_string:
                return year
        
        return