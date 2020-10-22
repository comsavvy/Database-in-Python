from dataclasses import dataclass, field


@dataclass
class Employee:
    """
        Employee(id, first_name, middle_name, surname, acct_balance)
    """
    id: int
    first_name: str
    middle_name: str
    surname: str
    acct_bal: int
    _email: str = field(repr=False, init=False)

    def __post_init__(self):
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.surname = self.surname.capitalize()
        self._email = f'{self.first_name.lower()}.{self.middle_name.lower()}@email.com'

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, other):
        self._email = other

    @staticmethod
    def insert(self: object, cursor: object, *emps: "Employee"):
        """
        Inserting the employees instance to the self database using the cursor

        :param self:
        :param cursor:
        :param emps:
        :return: None
        """
        for emp in emps:
            with self:
                cursor.execute("""
                            INSERT INTO employee (
                                    ID, First_name,
                                    Middle_name, Surname,
                                    Email, Balance
                            )              
                            VALUES (
                                :id, :first,
                                :mid, :sur,
                                :email, :acct                                                   
                            )
                        """, {'first': emp.first_name,
                              'mid': emp.middle_name,
                              'sur': emp.surname,
                              'email': emp.email,
                              'acct': emp.acct_bal, 'id': emp.id}
                           )

    @staticmethod
    def update(self, cursor, surname: str, firstname: str):
        """
        Updating the surname of the firstname rows using the cursor from the self database

        :param self:
        :param cursor:
        :param surname:
        :param firstname:
        :return: None
        """
        with self:
            cursor.execute(
                """
                UPDATE employee
                SET surname = :to_ 
                WHERE first_name = :where_
                """,
                {'to_': surname, 'where_': firstname}
            )

    @staticmethod
    def delete(self: object, cursor: object, firstname: str):
        """
        Deleting from the self database using the cursor to delete the rows with the firstname

        :param self:
        :param cursor:
        :param firstname:
        :return: None
        """
        with self:
            cursor.execute(
                """
                    DELETE FROM employee
                    WHERE first_name is :first
                """,
                {'first': firstname}
            )