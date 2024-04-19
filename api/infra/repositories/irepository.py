from abc import ABC, abstractmethod


class Repository(ABC):
    """Abstract class to implement repositories"""

    @abstractmethod
    def get_all():
        """Function to get all data from the tables"""

    @abstractmethod
    def get_by_id(id):
        """Function to get data from a especific input from the tables"""

    @abstractmethod
    def insert():
        """Function to insert data into the tables"""

    @abstractmethod
    def delete(id):
        """Function to delete data from the tables"""

    @abstractmethod
    def update(id):
        """Function to update data on the tables"""
