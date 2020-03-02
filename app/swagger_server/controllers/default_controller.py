import connexion
import six
from pymongo import MongoClient

from swagger_server.models.people import People  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.person_data import PersonData  # noqa: E501
from bson.objectid import ObjectId


client = MongoClient('mongodb', 27017)

def people_add(person):  # noqa: E501
    """Add a person to the database

     # noqa: E501

    :param person: 
    :type person: dict | bytes

    :rtype: Person
    """

    client.titanic.titanic.insert_one(person)
    
    return 'Person added!'


def people_list():  # noqa: E501
    """Get a list of all people

     # noqa: E501


    :rtype: People
    """
    return str(list(client.titanic.titanic.find({})))


def person_delete(uuid):  # noqa: E501
    """Delete this person

     # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: None
    """
    client.titanic.titanic.delete_one({"_id": ObjectId(uuid)})

    return 'Person deleted!'


def person_get(uuid):  # noqa: E501
    """Get information about one person

     # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: Person
    """

    return str(client.titanic.titanic.find_one({"_id": ObjectId(uuid)}))


def person_update(uuid, person):  # noqa: E501
    """Update information about one person

     # noqa: E501

    :param uuid: 
    :type uuid: 
    :param person: 
    :type person: dict | bytes

    :rtype: Person
    """

    client.titanic.titanic.update_one({"_id": ObjectId(uuid)},{"$set": person})
    return 'Person updated!'
