# _*_ coding:utf-8 _*_

from Person import ttypes


class PersonServiceImpl:
    def getPersonByUserName(self, username):
        print("got client param:" + username)

        person = ttypes.Person()
        person.username = username
        person.age = 20
        person.married = False
        return person

    def savePerson(self, person):
        print("got client param:")

        print(person.username)
        print(person.age)
        print(person.married)
