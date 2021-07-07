from abc import ABC, abstractmethod


class Converter(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def read_header(self):
        pass

    @abstractmethod
    def record_value(self):
        pass

    @abstractmethod
    def record_to_file(self):
        pass
















